#!/usr/bin/env python
import re

def extracPhrase(content):
    phrase_pattern_express='<phrase>([\w\s]*)<\/phrase>'
    pattern = re.compile(phrase_pattern_express)
    matchedPhrases=re.findall(pattern,content)
    words_content=re.sub(phrase_pattern_express," ",content)
    words_content=re.sub("\s+"," ",words_content)
    return matchedPhrases,words_content


def _get_stopwords():
    """
    Returns a list of stopwords.
    """
    f = open("data/stopwords.txt")
    stopwords = set()
    for line in f:
        stopwords.add(line.rstrip())
    return stopwords


def word_count(documents):
    word_freq = dict()
    phrase_freq=dict()
    for document in documents:
        if(len(document)>0):
            words_or_phrases=document.split(",")
            set_of_terms=set(words_or_phrases)
            for term in set_of_terms:
                if(" " in term):
                    if(term not in phrase_freq):
                        phrase_freq[term]=1
                    else:
                        phrase_freq[term]=phrase_freq[term]+1
                else:
                    if(term not in word_freq):
                        word_freq[term]=1
                    else:
                        word_freq[term]=word_freq[term]+1
    return word_freq,phrase_freq


if __name__=="__main__":
    stopwords=_get_stopwords()
    documents=[]
    i=0
    with open("results/segmentation.txt","r") as f:
        for line in f:
            line_lowercase = line.lower()
            line_lowercase=re.sub("\t"," ",line_lowercase)
            line_lowercase=re.sub("\s+"," ",line_lowercase)
            matchedPhrases,words_content=extracPhrase(line_lowercase)

            #remove punctations
            sentences_no_punc = re.split(r"<\/phrase>|<phrase>|[\.,:;\!\?\(\)\[\]<>]",words_content)
            stripped_sentences = []
            for sentence in sentences_no_punc:
                if(len(sentence)>0 and sentence!=""):
                    #remove all words that contain any ^A-Za-z
                    stripped_sentences.append(re.sub('\w*[^A-Za-z ]\w*', ' ', sentence))
            sentences_no_punc = " ".join(stripped_sentences)
            #remove extra spaces
            sentences_no_punc=re.sub("\s+"," ",sentences_no_punc)
            #remove stopwords and short words whose length is <=2.
            document_without_stopwords=",".join([word for word in sentences_no_punc.split() if (word not in stopwords and len(word)>2)])
            if(len(matchedPhrases)>=1):
                phrases=",".join(matchedPhrases)
                #add extracted phrases
                document_without_stopwords=document_without_stopwords+","+phrases
            documents.append(document_without_stopwords)


    #do the wordcount
    word_freq,phrase_freq=word_count(documents)

    #output the final result
    fWriter=open("results/input_forTopicModel.txt","w")
    filtered_documents=[]
    for document in documents:
        if(len(document)>0):
            words_or_phrases=document.split(",")
            filtered_document=[]
            for term in words_or_phrases:
                if(" " not in term):
                    if(word_freq[term]>3):
                        filtered_document.append(term)
                else:
                    filtered_document.append(term)
            filtered_documents.append(",".join(filtered_document))
        else:
            filtered_documents.append(document)
    for filtered_document in filtered_documents:
        fWriter.write("%s\n" % filtered_document)
    fWriter.close()
