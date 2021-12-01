import textnanipulations as tm

raw_text = """..."""
first = tm.frequency_table(raw_text)

raw_text_2 = """..."""
second = tm.frequency_table(raw_text_2)

print(first)
print(second)
print(tm.encapsulate(first))
print(tm.encapsulate(second))
