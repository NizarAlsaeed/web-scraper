import requests
from bs4 import BeautifulSoup
import re
url = 'https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url)->int:
    """return the number of citations needed."""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    a_citations = soup.findAll('a', attrs={'title':re.compile(r"Wikipedia:Citation needed")})
    return len(a_citations)

def get_citations_needed_report(url)->str:
    output = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    parag = soup.find_all('p')   
    for p in parag:
        children = p.findAll('a', attrs={'title':re.compile(r"Wikipedia:Citation needed")})
        if children:
            output = output + (p.text) +'\n'
    return output

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))