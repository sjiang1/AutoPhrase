MIN_SUPPORT=10
for i in {1..3} 
do
	#todo, remove emoji
	echo "==removing emojis from tweets======="
	python removeEmoji.py data/raw/sasatweets${i}.txt data/raw/sasatweets${i}.txt.tmp
	mv data/raw/sasatweets${i}.txt.tmp data/raw/sasatweets${i}.txt
	bash runAutoPhrase.sh data/raw/sasatweets${i}.txt ${MIN_SUPPORT}
	cp results/input_forTopicModel.txt sasatweets_forTopicModel.txt.${i}
	cp results/filtered_phrases.txt sasatweets_filtered_phrases.txt.${i}
done
cat sasatweets_forTopicModel.txt.* > sasatweets_forTopicModel.txt
cat sasatweets_filtered_phrases.txt.* > sasatweets_filtered_phrases.txt


