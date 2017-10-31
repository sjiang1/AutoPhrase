#!/usr/bin/env bash
TOKENIZER="-cp .:tools/tokenizer/lib/*:tools/tokenizer/resources/:tools/tokenizer/build/ Tokenizer"
TEXT_TO_SEG=${TEXT_TO_SEG:-data/20newsgroups.txt} #huangweijing

./bin/segphrase_segment \
        --pos_tag \
        --thread 10 \
        --model results/segmentation.model \
		--highlight-multi 0.5 \
		--highlight-single 0.8

java $TOKENIZER -m segmentation -i $TEXT_TO_SEG -segmented tmp/tokenized_segmented_sentences.txt -o results/segmentation.txt -tokenized_raw tmp/raw_tokenized_text_to_seg.txt -tokenized_id tmp/tokenized_text_to_seg.txt -c N
