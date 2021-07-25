from urllib.request import urlopen as uReq
#    package.module import function
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"

# Opens a connection, grabs webpage
uClient = uReq(my_url)

# reads webpage and puts in variable
page_html = uClient.read()

# html parsing
page_soup = soup(page_html, "html.parser")

page_soup.h1

# closes client
uClient.close()
