#! /bin/bash


#BSUB -J madlab_recon_edits
#BSUB -o /home/data/madlab/scripts/freesurfer_scripts/run_recon_afteredits_out
#BSUB -e /home/data/madlab/scripts/freesurfer_scripts/run_recon_afteredits_err

for subj in "IRC04H_09F012"; do

#re-running it after control points have been made or (if both control points & pial edits have been made)
cmd="recon-all -subjid ${subj} -autorecon2-cp -autorecon3 -no-isrunning"

#re-running it after pial edits have been made
#cmd="recon-all -subjid ${subj} -autorecon-pial -autorecon3 -no-isrunning"

#re-running it after wm edits have been made
#cmd="recon-all -subjid ${subj} -autorecon2-wm -autorecon3 -no-isrunning"

echo `echo ${cmd}` | bsub -q PQ_madlab

done
