from web_scraper import __version__
from web_scraper.web_scraper import get_citations_needed_count, get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'


def test_scraper_passages_george_sanders():
    url = "https://en.wikipedia.org/wiki/George_Sanders"
    
    assert get_citations_needed_report(url).split('\n')[0] == 'Sanders was born on 3 July 1906 in Saint Petersburg, Russian Empire, at number 6 Petrovski Ostrov. His parents were Henry Peter Ernest Sanders[citation needed] (1868–1960),[2] and Margarethe Jenny Bertha Sanders (née Kolbe; 1883–1967), who was born in Saint Petersburg, of mostly German, but also Estonian and Scottish, ancestry.[3] A biography published in 1990 claimed that Sanders\' father was the illegitimate son of a prince of the House of Oldenburg and a Russian noblewoman of the Tsar’s court, married to a sister of the Tsar.[4][a] Actor Tom Conway (1904–1967) was George Sanders\' elder brother. Their younger sister, Margaret Sanders, was born in 1912.'

    assert get_citations_needed_report(url).split('\n')[1] == 'RKO had been in dispute with Leslie Charteris, creator of The Saint, so they stopped the series[citation needed] and put Sanders in a new B picture series about a suave crimefighter, The Falcon. The first entry was The Gay Falcon (1941). It was popular and quickly followed by A Date with the Falcon (1942).'

def test_scraper_count_george_sanders():
    url = "https://en.wikipedia.org/wiki/George_Sanders"
    assert get_citations_needed_count(url) == 3