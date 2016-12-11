from pymediawiki import WikiPage
from pprint import pprint
import sys

titles = ['pantera', 'opeth']

try:
    wk = WikiPage(titles=titles)
except ValueError as error:
    print(error.args)
    sys.exit("Exited!")

pprint(wk.get_categories())
pprint(wk.get_images())
pprint(wk.get_linkshere())
