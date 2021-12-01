import textnanipulations as tm

def jaccard(base: dict, added: dict):
	merged = base
	intersected = {}
	for word in added:
		if word in base.keys():
			merged[word] = base[word] + added[word]
			intersected[word] = base[word] + added[word]
		else:
			merged[word] = added[word]

	tm.encapsulate(merged)
	tm.encapsulate(intersected)

	# ... Compare

	pass
