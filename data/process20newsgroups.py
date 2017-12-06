'''
input: /Users/huangwaleking/Downloads/20news-18828
output: raw20newsgroups.csv, 20newsgroups.csv
'''
import nltk
from nltk.tokenize import RegexpTokenizer
import re
from operator import itemgetter
from nltk.corpus import stopwords


def strip_newsgroup_header(text):
    """
    Given text in "news" format, strip the headers, by removing everything
    before the first blank line.
    """
    _before, _blankline, after = text.partition('\n\n')
    return after


def strip_newsgroup_footer(text):
    """
    Given text in "news" format, attempt to remove a signature block.

    As a rough heuristic, we assume that signatures are set apart by either
    a blank line or a line made of hyphens, and that it is the last such line
    in the file (disregarding blank lines at the end).
    """
    lines = text.strip().split('\n')
    for line_num in range(len(lines) - 1, -1, -1):
        line = lines[line_num]
        if line.strip().strip('-') == '':
            break

    if line_num > 0:
        return '\n'.join(lines[:line_num])
    else:
        return text


def removeHeder(text):
    return re.sub("From:.*@[\w.]*[>)]"," ",text)


def removeEmail(text):
    return re.sub("[\w+.]*@[\w+.]*"," ",text)

def removeDigits(text):
    return re.sub("\d+"," ",text)


def removeUrl(text):
    return re.sub("https?:\/\/([\w./])+", " ", text)


def getclass(fileid):
    """Get class name from fileid"""
    return fileid.split('/')[0]

def wordcount(d):
    dWord=dict()
    for id in d.keys():
        text=d[id][1]
        words=text.split(" ")
        for word in words:
            if(word in dWord):
                dWord[word]=dWord[word]+1
            else:
                dWord[word]=1
    fWordCount=open("wordcount.txt","w")
    soredWordcount=sorted(dWord.items(),key=itemgetter(1),reverse=True)
    for t in soredWordcount:
        fWordCount.write("%s\t%s\n" % (t[0],t[1]))
    fWordCount.close()
    return dWord


def filterLowfreq(dWord,d):
    fWriter = open("20newsgroups.csv", "w")
    for id in d.keys():
        text=d[id][1]
        classname=d[id][0]
        words=text.split(" ")
        tmp=[]
        for word in words:
            if(dWord[word]>3):
                tmp.append(word)
        fWriter.write("%s\t%s\t%s\n" %(classname,id," ".join(tmp)) )
    fWriter.close()

def preparedDataForToPMine():
    '''
    raw20newsgroups.txt
    '''
    fWriter=open("20newsgroups.txt", "w")
    newsgroups = \
        nltk.corpus.PlaintextCorpusReader('/Users/huangwaleking/Downloads/20news-18828', '.*/[0-9]+', encoding='latin1')
    ids = newsgroups.fileids()
    i = 0
    for id in ids:
        text = newsgroups.raw(fileids=id)
        text = strip_newsgroup_header(text)
        text = strip_newsgroup_footer(text)
        text = strip_newsgroup_quoting(text)
        s = removeHeder(text)
        s = removeEmail(s)
        s = re.sub("\\n"," ",s)#remove \n
        s = re.sub(r'[^\x00-\x7F]+', ' ', s) #remove non-ascii characters
        s = s.encode('utf-8').strip()

        fWriter.write("%s\n" % s)
        if (i % 100 == 0):
            print("processed %d files" % i)
        i = i + 1
    fWriter.close()




_QUOTE_RE = re.compile(r'(writes in|writes:|wrote:|says:|said:'
                       r'|^In article|^Quoted from|^\||^>)')


def strip_newsgroup_quoting(text):
    """
    Given text in "news" format, strip lines beginning with the quote
    characters > or |, plus lines that often introduce a quoted section
    (for example, because they contain the string 'writes:'.)
    """
    good_lines = [line for line in text.split('\n')
                  if not _QUOTE_RE.search(line)]
    return '\n'.join(good_lines)


if __name__=="__main__":
    print("read the raw dataset")
    preparedDataForToPMine()
