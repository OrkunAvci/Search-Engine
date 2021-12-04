import textnanipulations as tm
import json

raw_text = """..."""
first = tm.frequency_table(raw_text)

with open("random.txt", "w") as write:
	print(json.dumps(first))
	write.write(json.dumps(first))

with open("random.txt", "r") as read:
	back = json.loads(read.read())
	print(back)
