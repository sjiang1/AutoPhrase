# AutoPhrase: Automated Phrase Mining from Massive Text Corpora

## Publications

Please cite the following two papers if you are using this tool. Thanks!

*   Jingbo Shang, Jialu Liu, Meng Jiang, Xiang Ren, Clare R Voss, Jiawei Han, "**Automated Phrase Mining from Massive Text Corpora**", submitted to SIGKDD 2017, under review. [arXiv:1702.04457](https://arxiv.org/abs/1702.04457) [cs.CL]

*   Jialu Liu\*, Jingbo Shang\*, Chi Wang, Xiang Ren and Jiawei Han, "**[Mining
    Quality Phrases from Massive Text
    Corpora](http://jialu.cs.illinois.edu/paper/sigmod2015-liu.pdf)**”, Proc. of
    2015 ACM SIGMOD Int. Conf. on Management of Data (SIGMOD'15), Melbourne,
    Australia, May 2015. (\* equally contributed,
    [slides](http://jialu.cs.illinois.edu/paper/sigmod2015-liu-slides.pdf))
    
## Modification made by waleking's fork.
The originial version is [shangjingbo1226/AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase/). 

This fork version is mainly desinged for [SparseTP](https://github.com/waleking/SparseTP), a topic modeling tool for phrases, which is going to be published in the 29th IEEE International Conference on Tools with Artifical Intelligence (ICTAI'17).  

*	**Efficient Topic Modeling on Phrases via Sparsity**, Weijing Huang, Wei Chen, Tengjiao Wang and Shibo Tao, Proceedings of the 29th IEEE International Conference on Tools with Artifical Intelligence (ICTAI'17), Boston, USA, Nov 2017. ([slides](https://github.com/waleking/SparseTP/blob/master/ICTAI_presentation.pdf))


The modification of this fork is mainly in three folds. 

1.	Provide an portal [runAutoPhrase.sh](https://github.com/waleking/AutoPhrase/blob/master/runAutoPhrase.sh) to process the raw input file to get the final result file `input_forTopicModel.txt`, which is used as the input of [SparseTP](https://github.com/waleking/SparseTP).

2. We add [filter.py](https://github.com/waleking/AutoPhrase/blob/master/filter.py) to remove the low quality phrases (e.g., score<0.5), and get high quality phrases file `results/filtered_phrases.txt`. And with the high quality phrases, we update [src/segment.cpp](https://github.com/waleking/AutoPhrase/blob/master/src/segment.cpp) to segment the raw input file. Finaly, we add [prepare_for_topicmodeling.py](https://github.com/waleking/AutoPhrase/blob/master/prepare_for_topicmodeling.py) to get the result file `input_forTopicModel.txt `, with the foramt `word_1,word_2,word_3,...,word_n,phrases_1,...,phrases_m\n` in each line representing a single document in a corpus.

3. We add several running examples to provide a **"one click" quick way** to know how to use this tool. The running example 1 is designed to process the dataset [20newsgroups](http://qwone.com/~jason/20Newsgroups/); The running example 2 is designed to process the Wikipedia articles under the [Mathematics category](https://en.wikipedia.org/wiki/Category:Mathematics) (the json data are available at [Dropbox](https://www.dropbox.com/s/816k7dkkub6kd0f/mathematics.json.gz)); The running example 3 and 4 are designed for [Chemistry](https://en.wikipedia.org/wiki/Category:Chemistry) ([availabe json data](https://www.dropbox.com/s/89f9gvrg2en0f8i/Chemistry.json.gz)) and [Argentina](https://en.wikipedia.org/wiki/Category:Argentina) ([available json data](https://www.dropbox.com/s/buo26zn074gnt5y/Argentina.json.gz)).

### Usage
bash runAutoPhrase.sh $input_file

`$input_file` is the path of the input file, which includes the whole corpus with each line representing a single file in a corpus.

The result file will be restored in `results/input_forTopicModel.txt`.

### Running Examples
1, `bash runningExample1.sh`

After running on the 20newsgroups dataset, the result file can be found as results/input_forTopicModel.txt. 

Or for a quick view without running, the result can be downloaded from [Dropbox](https://www.dropbox.com/s/2ifzu84j56knvsn/20newsgroups.txt.gz). 

Take one line in the result file as an example, it represents the document after extracting phrases: *alt,introduction,april,version,introduction,atheism,mathew,...,read,article,mathew,version,pgp signed message,frequently asked questions,faq files,strong atheism,weak atheism,strong atheism,god exists,point of view,weak atheism,...,god exists,peer pressure,pgp signature,pgp signature*


2, `bash runningExample2.sh`

After running on the Mathematics Wiki dataset, the result file can be found as results/input_forTopicModel.txt. 

Or for a quick view without running, the result can be downloaded from [Dropbox](https://www.dropbox.com/s/gbhhe0xogdmwo8x/mathematics.txt.gz).

Take one line in the result file as an example, it represents the document after extracting phrases: *kohli,scientist,lab,cambridge,majority,research,field,machine,learning,vision,contributions,game,theory,psychometrics,picture,josh,semantic,paint,kinect,fusion,voxel,crf,inference,microsoft research,discrete algorithms,programming language,higher order,graphical models*


3, `bash runningExample3.sh`

After running on the Chemistry Wiki dataset, the result file can be found as results/input_forTopicModel.txt. 

Or for a quick view without running, the result can be downloaded from [Dropbox](https://www.dropbox.com/s/kv4a0xutepdn8ws/chemistry.txt.gz).

4, `bash runningExample4.sh`

After running on the Argentina Wiki dataset, the result file can be found as results/input_forTopicModel.txt. 

Or for a quick view without running, the result can be downloaded from [Dropbox](https://www.dropbox.com/s/fdx2z99xc0aepce/argentina.txt.gz).

### Performance

We test runAutoPhrase.sh on a signle 4-Core 3.4GHz CPU, 24GB RAM machine. To see what will happen for processing a very big input file, we take [whole Wikipedia pages](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2) as an input. There are 5,738,260 articles, 2,036,099,636 tokens, 10.67GB. In order to fit it in our limit memory, we split this big file into 5 smaller ones, each one with about 2.1GB size. In this way, we run AutoPhrase sequencely on these 5 splitted files, in which each 2.1GB file costs 24GB memory. After 12.5 hours, we got the processed result for Wikipedia pages.

In short, we summarize the performance as the following table.

|setting       | input file size | memory cost | time cost|
|--------------|-----------------|-------------|----------|
|Directly              | 2.1GB           | 24 GB       | 2.5 hours|
|Running on 5 splited files sequencely| 10.67GB           | 24 GB       | 12.5 hours|




