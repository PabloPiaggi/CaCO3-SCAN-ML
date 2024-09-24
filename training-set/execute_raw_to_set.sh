#!/bin/bash -l

dir=`pwd`/
for file in `find . -name "energy.raw"`
do
	file=${file%energy.raw}
	folder=${file##./}
	folder_full_path=$dir$folder
	echo $folder_full_path
	cd $folder_full_path
	#cd $folder/extracted-confs
	/home/ppiaggi/Programs/della-gpu/Software-deepmd-kit-2.1.3-2/deepmd-kit/data/raw/./raw_to_set.sh 20000
	pwd
	#cd ../../
done
cd $dir
