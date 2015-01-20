# CAZy data
from cazy_data import *

# BeautifulSoup
import bs4

# Functions to build URLs from names
def cazy_family_url(family):
    """ Returns CAZy family home page. Expects families in the form
        GH5, CE10, etc.
    """
    return CAZY_HOME + family.upper() + '.html'

