import requests
from bs4 import BeautifulSoup
import re


def search_and_parse(query, city):
    try:
        url = f'https://tabletka.by/search?request={query}'
        response = requests.get(url)

        if response.status_code == 200:
            search_soup = BeautifulSoup(response.text, 'html.parser')
            first_result_link = search_soup.find(href=lambda href: href and href.startswith('/result?ls'))
            new_url = 'https://tabletka.by' + first_result_link['href'] + f'&region={city}'
            new_response = requests.get(new_url)

            if new_response.status_code == 200:
                with open('result.txt', 'w', encoding='utf-8') as file:
                    result_soup = BeautifulSoup(new_response.text, 'html.parser')
                    list_tags = result_soup.find_all('td', class_='address tooltip-info')
                    for tags in list_tags:
                        tag = tags.find('div', class_='tooltip-info-header')
                        text = tags.span.get_text()
                        text = text.strip()
                        index_comma = text.find(',')
                        if index_comma != -1:
                            file.write('\n' + text[index_comma + 2:] + '\n')

            with open('result.txt', 'r', encoding='utf-8') as file:
                result = file.read()
                return result
    finally:
        with open('result.txt', 'w', encoding='utf-8') as file:
            file.write('')


def parse_pills(query):
    try:
        url = f'https://bymed.top/drugs?q={query}'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                if query.lower() in link.text.lower():
                    full_url = 'https://bymed.top/' + link['href']
                    response = requests.get(full_url)
                    if response.status_code == 200:
                        with open('result.txt', 'w', encoding='utf-8') as file:
                            result_soup = BeautifulSoup(response.text, 'html.parser')
                            divs = result_soup.find_all('div', {'class': 'instruction instruction-ind instruction-block'})
                            for div in divs:
                                file.write(div.text)
            with open('result.txt', 'r', encoding='utf-8') as file:
                result = file.read()
                return result
    finally:
        with open('result.txt', 'w', encoding='utf-8') as file:
            file.write('')
