#!/bin/bash

#BSUB -J madlab_seqtrd_dcm_convert
#BSUB -o /scratch/madlab/crash/dcm_convert_seqtrd_out
#BSUB -e /scratch/madlab/crash/dcm_convert_seqtrd_err

python dicomconvert2.py -d /home/data/madlab/dicoms/seqtrd -o /home/data/madlab/data/mri/seqtrd -f heuristic_seqtrd.py -wd multiple -q PQ_madlab -c dcm2nii -s 783134

