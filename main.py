import scrapy
import string

raw_text = """..."""

clean_text = raw_text.strip(string.punctuation)
words = clean_text.split(" ")

dic = {}
for key in words:
	if key not in dic.keys() :
		dic[key] = 0
	dic[key] = dic[key] + 1

print(dic)
