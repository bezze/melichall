import bs4
import requests
import json

url = 'https://www.fravega.com/p/smart-tv-50-4k-ultra-hd-tcl-l50p65-501908'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"

# html_file = 'smart-tv-philips-43-full-hd-43pfg581377.html'
# with open(html_file, 'r') as html:
#     html_doc = html.read()


def get_item_page(url):
    """docstring for get_catalogue_page"""
    headers = {
        'User-Agent': USER_AGENT
    }
    response = requests.request('GET', url, headers=headers)
    return response


def get_specs_box(box):
    specs = {}
    for content in box.find_all('li'):
        content_name = content.h1.text.strip()
        specs[content_name] = {}
        for spec in content.find_all('div', class_="Specifications__ContentDetails-i57k8a-4"):
            spec_name = spec.find('div', class_='specName').text.strip()
            spec_value = spec.find('div', class_='specValue').text.strip()
            specs[content_name][spec_name] = spec_value
    return specs


def process(url):

    html_response = get_item_page(url)
    html_text = html_response.text

    soup = bs4.BeautifulSoup(html_text, 'html.parser')

    name = soup.find('h1', class_='product-title').text.strip()

    previous_price = soup.find('span', class_='previous-price Price__PreviousPrice-sc-1a3e119-1 bcfAaX').text.strip()
    current_price = soup.find('p', class_='current-price').text.strip()

    box = soup.find('div', class_="Specifications__StyledSpecifications-i57k8a-0 bVxZEy")
    specs = get_specs_box(box)

    specs = {
        "name": name,
        "current_price": current_price,
        "previous_price": previous_price,
        **specs
    }

    return specs


def main():
    """docstring for main"""

    all_dic = {}
    failed = []
    with open('./product_urls_frave') as f:
        for url in f.readlines():
            try:
                item = process(url.strip())
                all_dic[item['name']] = item
            except Exception as e:
                failed.append(url)

    with open('processed_products_frave.json', 'w', encoding='utf8') as g:
        json.dump(all_dic, g, ensure_ascii=False)

    with open('failed_urls_frave', 'w') as h:
        for failure in failed:
            h.write(failure+'\n')



if __name__ == '__main__':
    main()

