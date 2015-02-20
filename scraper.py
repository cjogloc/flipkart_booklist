import scraperwiki

import lxml.html

html = scraperwiki.scrape("http://www.flipkart.com/books/list/2-0")
root = lxml.html.fromstring(html)

for e in root.cssselect(".booklist_items table")[0].cssselect("a"):
    print e.attrib['href']