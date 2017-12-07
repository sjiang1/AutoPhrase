if [ ! -e data/raw/chemistry.txt ]; then
    if [ ! -e data/raw/chemistry.json ]; then
        wget -c https://www.dropbox.com/s/89f9gvrg2en0f8i/Chemistry.json.gz?dl=0 -O data/raw/chemistry.json.gz
        gzip -d data/raw/chemistry.json.gz
    fi
    python data/extract_contents_from_json.py data/raw/chemistry.json data/raw/chemistry.txt
    echo "the input file data/raw/chemistry.txt is prepared"
fi

bash runAutoPhrase.sh data/raw/chemistry.txt
