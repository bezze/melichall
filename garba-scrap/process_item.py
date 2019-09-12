import bs4
import requests
import json

url = 'https://www.garbarino.com/producto/smart-tv-philips-43-full-hd-43pfg581377/9ef586dbf7'
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


def get_specs_box(gb_tech_spec):
    spec_box = gb_tech_spec.find('div', class_="gb-tech-spec-module-list gb-expandable-list gb--expanded")
    specs = {}
    for pair in spec_box.find_all('li'):
        key = pair.find('h3', class_='gb-tech-spec-module-list-title').contents[0].strip()
        value = pair.find('span', class_='gb-tech-spec-module-list-description').text.strip()
        specs[key] = value
    return specs


def process(url):

    html_response = get_item_page(url)
    html_text = html_response.text

    soup = bs4.BeautifulSoup(html_text, 'html.parser')

    name = soup.h1.text

    # print(name, url)

    gb_tech_spec_screen = soup.find('div', class_='gb-tech-spec', id='gb-tech-spec')
    screen = get_specs_box(gb_tech_spec_screen)

    gb_tech_spec_dim = soup.find('div', class_='gb-accordion-module gb-tech-spec-module gb-tech-spec-dimensions', id='gb-tech-spec-dimensiones')
    dim = get_specs_box(gb_tech_spec_dim)

    gb_tech_spec_conn = soup.find('div', class_='gb-accordion-module gb-tech-spec-module gb-tech-spec-conectivity', id='gb-tech-spec-conectividad')
    conn = get_specs_box(gb_tech_spec_conn)

    gb_tech_spec_extra = soup.find('div', class_='gb-accordion-module gb-tech-spec-module gb-tech-spec-functions', id='gb-tech-spec-funciones-especiales')
    extra = get_specs_box(gb_tech_spec_extra)

    structure = {
        "name": name,
        "screen": screen,
        "dimensions": dim,
        "connection": conn,
        "extra": extra
    }

    return structure


def main():
    """docstring for main"""

    all_dic = {}
    failed = []
    with open('./product_urls') as f:
        for url in f.readlines():
            try:
                item = process(url.strip())
                all_dic[item['name']] = item
            except Exception as e:
                failed.append(url)

    with open('processed_products.json', 'w') as g:
        g.write(json.dumps(all_dic))

    with open('failed_urls', 'w') as h:
        for failure in failed:
            h.write(failure+'\n')



if __name__ == '__main__':
    main()
