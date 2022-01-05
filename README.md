# Search Engine

This project has intended to implement TF-IDF based reverse index keyword to document hash table for a search engine. But in its aim to be self-sufficient it has also includes a web crawler and a local resource manager. It can further be developed by implementing Ranking algorithms.

## Libraries

- nltk
- re
- beautifulsoup4
- selenium
- requests
- PyQt5
- pyqt5-tools

## Quick Start

First install the libraries with `pip`.

````bash
pip install -r requirements.txt
````

Then run the `full_pipeline.py`.

```bash
cd ../Web-Crawler
python full_pipeline.py
```

If `python` doesn’t work try running with `python3` or `py`.

`full_pipeline.py` usually takes some time complete so you can leave it running in the background. You only need to run it ONCE.

When it finishes you will have local resources stored in `./data` folder inside the project folder.

Then you can safely run `main.py` and enjoy browsing the documents.

```bash
python main.py
```



