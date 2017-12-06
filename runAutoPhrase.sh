#!/bin/bash
rm tmp/*
rm results/*

INPUT_FILE=$1
corpusname=$( echo $1 | perl -lne 'print $1 if /.*\/(.*?)\./' ) #such as 20newsgroups, mathematics

bash auto_phrase.sh ${INPUT_FILE}
python filter.py
bash phrasal_segmentation.sh ${INPUT_FILE}
python prepare_for_topicmodeling.py


echo ${green}"after running AutoPhrase, the file for topic modeling is stored as results/input_forTopicModel.txt"${reset}
