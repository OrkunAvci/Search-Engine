import process_pages as pp
import process_text as pt
import file_manager as fm
import process_reverse_index as pri

tags = [
	# Commented out for safety and sanity.
	# "https://hashnode.com/n/javascript",
	# "https://hashnode.com/n/web-development",
	# "https://hashnode.com/n/reactjs",
	# "https://hashnode.com/n/python",
	# "https://hashnode.com/n/nodejs",
	# "https://hashnode.com/n/github",
	# "https://hashnode.com/n/java",
	# "https://hashnode.com/n/programming",
	# "https://hashnode.com/n/javascript/recent",
	# "https://hashnode.com/n/web-development/recent",
	# "https://hashnode.com/n/reactjs/recent",
	# "https://hashnode.com/n/python/recent",
	# "https://hashnode.com/n/nodejs/recent",
	# "https://hashnode.com/n/github/recent",
	# "https://hashnode.com/n/java/recent",
	# "https://hashnode.com/n/programming/recent"
]

#   Links to blog posts (also used in file naming)
all_links = []
for tag in tags:
	urls = pp.get_url_list(tag)
	fm.save("tag_" + tag, urls)
	all_links = all_links + urls

#   Remove duplicates
all_links = list(set(all_links))

#   Get raw text and frequency table of each document
#   Collect all unique words across all documents in {guide}
#   Guide also defines the final vector space
guide = {}
for link in all_links:
	raw = pp.get_text_from_url(link)
	#   fm.save("raw_" + link, raw)     #   Optional.
	tokens = pt.tokenize(raw)
	table = pt.frequency_table(tokens)
	if len(table) > 5:
		fm.save("ft_" + link, table)
		for key in table.keys():
			guide[key] = {}

#   Sort guide
guide = dict(sorted(guide.items()))

#   Save the list of links and guide
if len(all_links) > 0 and len(guide) > 0:
	fm.save("_all_links", all_links)
	fm.save("_guide", guide)

reverse_index = guide
for key in reverse_index.keys():
	reverse_index[key] = []

#   Represent each document in {guide} vector space
for link in all_links:
	ft = fm.get("ft_" + link)
	fm.save("ft_" + link, ft)
	for keyword,count in ft.items():
		reverse_index[keyword].append({
			"link": link,
			"count": count,
			"TF-IDF": 0
		})

fm.save("_reverse_index", reverse_index)

reverseIndex = fm.get('_reverse_index')
wordCounts = pri.getLinkWordCounts(all_links)
fm.save('linksWordCounts', wordCounts)

fixedReverseIndex = pri.fixReverseIndex(reverseIndex, wordCounts)
fm.save('_reverse_index_final', fixedReverseIndex)