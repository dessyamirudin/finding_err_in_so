import sys
import webbrowser
import urllib.parse

def search_last_err_on_so():
	last_err = sys.last_value
	url = "https://stackoverflow.com/search?q=" + str(last_err)
	webbrowser.open_new_tab(urllib.parse.quote(url))

#credit to https://www.linkedin.com/in/thomasneitmann/