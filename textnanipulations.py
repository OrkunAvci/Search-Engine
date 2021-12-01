import string

def frequency_table(raw_text: str) -> dict:
	clean_text = raw_text.strip().strip(string.punctuation).strip(string.digits)
	words = clean_text.split(" ")

	dic = {}
	for key in words:
		if key not in dic.keys() :
			dic[key] = 0
		dic[key] = dic[key] + 1

	dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse = True)}
	return dic

def encapsulate(original: dict) -> dict:
	meta = {
		"total_word_count"  : sum([v for k, v in original.items()]),
		"unique_word_count" : len([v for k, v in original.items()]),
		"most_frequent"     : next(iter((original.items()))),
		"expectation"       : 0,
		"altered_data"      : {},
		"data"              : original
	}

	meta["expectation"] = meta["total_word_count"] / meta["unique_word_count"]
	meta["altered_data"] = {k:v for k,v in original.items() if v > meta["expectation"]}

	return meta
