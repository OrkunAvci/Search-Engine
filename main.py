import process_pages as pp
import file_manager as fm
import pprint

all_links = fm.get("_all_links")
guide = fm.get("_guide")

reverse_index = guide
for key in reverse_index.keys():
	reverse_index[key] = []

for link in all_links:
	ft = fm.get("ft_" + link)
	for keyword,count in ft.items():
		reverse_index[keyword].append({
			"link": link,
			"count": count,
			"TF-IDF": 0
		})

pprint.pprint(reverse_index)    # BIG text, use with a terminal that can handle it

fm.save("_reverse_index", reverse_index)
