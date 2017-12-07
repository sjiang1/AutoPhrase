if [ ! -e data/raw/argentina.txt ]; then
    if [ ! -e data/raw/argentina.json ]; then
        wget -c https://www.dropbox.com/s/buo26zn074gnt5y/Argentina.json.gz?dl=0 -O data/raw/argentina.json.gz
        gzip -d data/raw/argentina.json.gz
    fi
    python data/extract_contents_from_json.py data/raw/argentina.json data/raw/argentina.txt
    echo "the input file data/raw/argentina.txt is prepared"
fi

bash runAutoPhrase.sh data/raw/argentina.txt
