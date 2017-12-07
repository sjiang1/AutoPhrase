if [ ! -e data/raw/mathematics.txt ]; then
    if [ ! -e data/raw/mathematics.json ]; then
        wget -c https://www.dropbox.com/s/816k7dkkub6kd0f/mathematics.json.gz?dl=0 -O data/raw/mathematics.json.gz
        gzip -d data/raw/mathematics.json.gz
    fi
    python data/extract_contents_from_json.py data/raw/mathematics.json data/raw/mathematics.txt
    echo "the input file data/raw/mathematics.txt is prepared"
fi

bash runAutoPhrase.sh data/raw/mathematics.txt
