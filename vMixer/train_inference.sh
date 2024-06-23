#!/bin/bash


while getopts 'c:n:t:r:p' OPT; do
    case $OPT in
        c) cuda=$OPTARG;;
        n) name=$OPTARG;;
		t) task=$OPTARG;;
        r) train="true";;
        p) predict="true";;
        
    esac
done
echo $name	


if ${train}
then
	
	cd /home/daniya.kareem/vmixer/vmixer/
	CUDA_VISIBLE_DEVICES=${cuda} vmixer_train 3d_fullres vmixerTrainerV2_${name} ${task} 0
fi





