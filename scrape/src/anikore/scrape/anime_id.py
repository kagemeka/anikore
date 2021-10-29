import typing
import bs4
import requests
import tqdm
import logging


def scrape_anime_ids() -> typing.List[int]:
    base_url = 'https://www.anikore.jp/50on'
    tails = (f'-{i + 1}-{j + 1}/' for i in range(3) for j in range(46))
    urls = [f'{base_url}{tail}' for tail in tails]
    anime_ids = []

    def scrape_per_page(url: str) -> typing.NoReturn:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        ls = soup.find_all(class_='rlta_ttl')
        for elm in ls:
            id_ = elm.find('a').get('href').split('/')[-2]
            anime_ids.append(int(id_))

    logging.info('start getting anime IDs on Anikore')
    for url in tqdm.tqdm(urls):
        scrape_per_page(url)
    return anime_ids


def search_max_anime_id() -> int:
    site_url = 'https://www.anikore.jp/'
    base_url = f'{site_url}anime/'

    def page_exist(anime_id: int) -> bool:
        response = requests.get(f'{base_url}{anime_id}/')
        return response.url != site_url

    def binary_search() -> int:
        lo, hi = 1, 1 << 16
        while hi - lo > 1:
            anime_id = (lo + hi) >> 1
            if page_exist(anime_id):
                lo = anime_id
            else:
                hi = anime_id
        return lo

    return binary_search()
