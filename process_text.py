import nltk
import re

def tokenize(raw_text: str) -> list:
	no_space_text = " ".join(raw_text.split())  # Remove extra spaces
	no_punctuation_text = re.sub("[^0-9A-Za-z ]", "", no_space_text)  # Remove punctuation
	pure_text = "".join([i.lower() for i in no_punctuation_text])  #   To lower

	tokens = nltk.tokenize.word_tokenize(pure_text)
	stop_words = nltk.corpus.stopwords.words("english")
	tokens = [token for token in tokens if token not in stop_words]

	lemm = nltk.stem.WordNetLemmatizer()
	tokens = [lemm.lemmatize(token) for token in tokens]
	tokens.sort()
	return tokens

def frequency_table(tokens: list) -> dict:
	table = {}
	for token in tokens:
		if token not in table.keys():
			table[token] = 0
		table[token] = table[token] + 1

	return table

def encapsulate(original: dict) -> dict:
	meta = {
		"total_word_count"  : sum([v for k, v in original.items()]),
		"unique_word_count" : len([v for k, v in original.items()]),
		"TF-IDF"            : 0,
		"data"              : original
	}

	return meta
