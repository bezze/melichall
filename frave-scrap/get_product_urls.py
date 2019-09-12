import bs4
import requests

url = 'https://www.fravega.com'

category = f'{url}/l/?categories=tv-y-video%2Ftv'

html_file = 'example.html'

# with open(html_file, 'r') as html_doc:
#     soup = bs4.BeautifulSoup(html_doc.read(), 'html.parser')

class EndOfCatalogue(Exception):
    pass


def get_catalogue_page(url, page=1):
    """docstring for get_catalogue_page"""
    page_url = f'{url}&page={page}'
    response = requests.request('GET', page_url)
    if "No se han encontrado resultados" not in response.text:
        return response
    else:
        raise EndOfCatalogue("Possibly page doesnt exist")


def save_urls(result_urls):
    with open('product_urls', 'w') as products:
        for uri in result_urls:
            products.write(f'{url}{uri}\n')


page = 0
results = []
while True:
    page += 1
    try:
        print(page)
        html_doc = get_catalogue_page(category, page=page)
        soup = bs4.BeautifulSoup(html_doc.text, 'html.parser')
        item_class = 'styled__CallToAction-sc-3dysb6-2 kAByqR'
        result_uris = [i['href'] for i in soup.find_all('a', class_=item_class)]
        results += result_uris
    except EndOfCatalogue:
        break
save_urls(results)
