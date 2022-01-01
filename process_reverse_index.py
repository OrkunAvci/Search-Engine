import os
import math
import process_text as pt
import file_manager as fm


#returns list of dictionaries contains links/total word counts. assume raw_data contains all raw text files obtained by crawling
def getLinkWordCounts(allLinks)->list:
    linksAndCounts = []
    for link in allLinks:
        sub = link.partition("https://")[2].replace("-","_").replace("/","_").replace(".","_")
        for filename in os.listdir(r'./data/raw_data'):
            if filename.partition("raw_")[2] == sub:
                linkCount = {"link":None, "total_word_count":0}
                text_file = open(filename)  
                textt = text_file.read()
                total_word_cnt = len(pt.tokenize(textt))
                linkCount["link"] = link
                linkCount["total_word_count"] = total_word_cnt
                text_file.close()
                linksAndCounts.append(linkCount)
    return linksAndCounts


#returns total word count of a given link/file
def getWordCountOfLink(link, wordCounts)->int:
    for linkCountTuple in wordCounts:
        if linkCountTuple["link"] == link:
            return linkCountTuple["total_word_count"]
    return None

#method to fix '_reverse_index'
def fixReverseIndex(reverseIndexDict, wordCounts)->dict:
    copyToReturn = reverseIndexDict.copy()
    for word in copyToReturn.keys():                         #iterate through all words in main dictionary
        for wordDataDict in copyToReturn.get(word):          #iterate through dictionaries in list of dicts
            termFreq = wordDataDict["count"]/getWordCountOfLink(wordDataDict["link"], wordCounts)
            documentFreq = len(copyToReturn.get(word))
            inverseDocFreq = math.log(len(wordCounts)/(documentFreq+1))
            tf_idf = termFreq*inverseDocFreq
            wordDataDict["TF-IDF"] = tf_idf
    return copyToReturn


#returns links, counts and tf-idf values of word/file pairs sorted on tf-idf value; only if word is in our word list
def getTfIdfsOfWord(word, fixedReverseIndex)->list:
    if not word in fixedReverseIndex:
        print("Couldnt find the word in list")
        return None
    else:
        listOfDicts = fixedReverseIndex.get(word)
        sortedList = sorted(listOfDicts, key=lambda d: d['TF-IDF'], reverse=True) 
        return sortedList

