import process_pages as pp
import pprint

data = pp.get_text_from_url("https://orkunavci.hashnode.dev/master-google-in-3-minutes")

pprint.pprint(data)
