import bs4
import requests

url = 'https://www.garbarino.com'
category = f'{url}/productos/televisores-y-video/4340'


class EndOfCatalogue(Exception):
    pass


def get_catalogue_page(url, page=1):
    """docstring for get_catalogue_page"""
    page_url = f'{url}?page={page}'
    response = requests.request('GET', page_url)
    if response.url == page_url:
        return response
    else:
        raise EndOfCatalogue("Redirection. Possibly page doesnt exist")


def save_urls(result_urls):
    with open('product_urls_garba', 'w') as products:
        for uri in result_urls:
            products.write(f'{url}{uri}\n')


def get_urls():
    page = 0
    results = []
    while True:
        page += 1
        try:
            print(page)
            html_doc = get_catalogue_page(category, page=page)
            soup = bs4.BeautifulSoup(html_doc.text, 'html.parser')
            result_uris = [i['content'] for i in soup.find_all('meta', itemprop='url')]
            results += result_uris
        except EndOfCatalogue:
            break

    save_urls(results)


def main():
    get_urls()


if __name__ == '__main__':
    main()
