#!/usr/bin/env python

#BSUB -o /scratch/madlab/surfaces/run_recon_out
#BSUB -e /scratch/madlab/surfaces/run_recon_err

import os
from glob import glob

from nipype import Node, Function, Workflow, IdentityInterface
from nipype.interfaces.freesurfer import ReconAll
from nipype.interfaces.io import DataGrabber

#curr_dir_age = 'cmind_age00_raw'
#data_dir = '/home/data/madlab/data/mri/cmind/raw_data'

#sids = os.listdir('%s/%s' % (data_dir, curr_dir_age))
#sids = sids [:-1] 	#REMOVES THE .tar file
sids = ['783125', '783126', '783127', '783128', '783129', '783131', '783132', '783133']

info = dict(T1=[['subject_id']])

infosource = Node(IdentityInterface(fields=['subject_id']), name='infosource')
infosource.iterables = ('subject_id', sids)

# Create a datasource node to get the T1 file
datasource = Node(DataGrabber(infields=['subject_id'],outfields=info.keys()),name = 'datasource')
datasource.inputs.template = '%s/%s'
datasource.inputs.base_directory = os.path.abspath('/home/data/madlab/data/mri/seqtrd/')
datasource.inputs.field_template = dict(T1='%s/anatomy/T1_*.nii.gz')
datasource.inputs.template_args = info
datasource.inputs.sort_filelist = True

reconall_node = Node(ReconAll(), name='reconall_node')
reconall_node.inputs.openmp = 2
reconall_node.inputs.subjects_dir = os.environ['SUBJECTS_DIR']
reconall_node.inputs.terminal_output = 'allatonce'
reconall_node.plugin_args={'bsub_args': ('-q PQ_madlab -n 2'), 'overwrite': True}

wf = Workflow(name='fsrecon')

wf.connect(infosource, 'subject_id', datasource, 'subject_id')
wf.connect(infosource, 'subject_id', reconall_node, 'subject_id')
wf.connect(datasource, 'T1', reconall_node, 'T1_files')

wf.base_dir = os.path.abspath('/scratch/madlab/surfaces/seqtrd')
#wf.config['execution']['job_finished_timeout'] = 65

wf.run(plugin='LSF', plugin_args={'bsub_args': ('-q PQ_madlab')})

