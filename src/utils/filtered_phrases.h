//
// Created by Huang Waleking on 11/1/17.
// input：results/filtered_phrases.txt, tmp/token_mapping.txt
// output: set<vector<int>> phrasesById
//

#ifndef AUTOPHRASE_FILTERED_PHRASES_H
#define AUTOPHRASE_FILTERED_PHRASES_H
#include "../utils/utils.h"
#include "../frequent_pattern_mining/frequent_pattern_mining.h"
namespace FilteredPhrases {
    //construct new_patterns by filtedred phrases
    vector<FrequentPatternMining::Pattern> filter_patterns(set<vector<TOKEN_ID_TYPE>> phrasesById){
        vector<FrequentPatternMining::Pattern> new_patterns;
        for(vector<TOKEN_ID_TYPE> phraseById: phrasesById){
            int pattern_id=FrequentPatternMining::whichPattern(phraseById);
            if(pattern_id>0){
                new_patterns.push_back(FrequentPatternMining::patterns[pattern_id]);
            }
        }
        return new_patterns;
    }

    vector<vector<string>> readFilteredPhrases() {
        vector<vector<string>> phrases;
        FILE *in = tryOpen("results/filtered_phrases.txt", "r");
        while (getLine(in)) {
            vector<string> phrase;
            stringstream sin(line);
            for (string temp; sin >> temp;) {
                phrase.push_back(temp);
                //            cout<< temp<< " ";
            }
            phrases.push_back(phrase);
            //        cout<<endl;
        }
        return phrases;
    }


    map<string, TOKEN_ID_TYPE> readTokenMapping() {
        map<string, TOKEN_ID_TYPE> tokenMapStr2Id;
        FILE *in = tryOpen("tmp/token_mapping.txt", "r");
        while (getLine(in)) {
            stringstream sin(line);
            string temp;
            sin >> temp;
            int token_id = stoi(temp);//TODO, change int to TOKEN_ID_TYPE or something
            sin >> temp;
            string phrase = temp;
            tokenMapStr2Id[phrase] = token_id;
        }
        return tokenMapStr2Id;
    }


    set<vector<TOKEN_ID_TYPE>> getFilteredPhrasesById(vector<vector<string>> phrases, map<string, TOKEN_ID_TYPE> tokenMapStr2Id) {
        set<vector<TOKEN_ID_TYPE>> phrasesById;
        for (int i = 0; i < phrases.size(); i++) {
            vector<TOKEN_ID_TYPE> phraseById;

            vector<string> phrase = phrases[i];
            for (int j = 0; j < phrase.size(); j++) {
                string token = phrase[j];
                phraseById.push_back(tokenMapStr2Id[token]);
            }
            phrasesById.insert(phraseById);
        }
        return phrasesById;
    }

    //portal of filtered_phrases.h
    set<vector<TOKEN_ID_TYPE>> loadPhrasesById(){
        vector<vector<string>> phrases=readFilteredPhrases();
        map<string,TOKEN_ID_TYPE> tokenMapStr2Id=readTokenMapping();
        set<vector<TOKEN_ID_TYPE>> phrasesById=getFilteredPhrasesById(phrases,tokenMapStr2Id);
        return phrasesById;
    }
}

#endif //AUTOPHRASE_FILTERED_PHRASES_H



