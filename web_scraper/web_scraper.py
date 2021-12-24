import requests
from bs4 import BeautifulSoup

def get_article(url):
    page = requests.get(url)
    matches = BeautifulSoup(page.content, "html.parser").find_all(title="Wikipedia:Citation needed")
    return [match.find_parent('p').text for match in matches]

def get_citations_needed_count(url):
    paragraph = get_article(url)
    return len(paragraph)
    
def get_citations_needed_report(url):
    paragraph = get_article(url)
    return '\n'.join([sentence.strip() for sentence in paragraph])

url = "https://en.wikipedia.org/wiki/George_Sanders"
count = get_citations_needed_count(url)
report = get_citations_needed_report(url)
print(count, report)