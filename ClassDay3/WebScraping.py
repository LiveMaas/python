### Example Task 1 - Grabbing all elements of a class
# Let's try to grab all the section headings of the Wikipedia Article on Grace Hopper from this 
# URL: https://en.wikipedia.org/wiki/Grace_Hopper

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
# type(res.text)
soup = bs4.BeautifulSoup(res.text, "lxml")

# type(soup)
# mw-heading mw-heading2
for heading in soup.select(".mw-heading.mw-heading2"):
    print(heading.getText().replace('[edit]', ''))

### Example Task 3 - Getting an Image from a Website
# Let's attempt to grab the image of the Deep Blue Computer from this wikipedia article: 
# https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)

import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, "lxml")

image_url = "https:" + soup.select('.mw-file-element')[1]['src']

res_2 = requests.get(image_url)
with open('deep_blue.jpg', 'wb') as f:
    f.write(res_2.content)
    f.close()
# The image is saved in the current working directory as deep_blue.jpg