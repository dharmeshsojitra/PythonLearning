import webbrowser
import requests, bs4

search_string = input('enter search term: ')

response = requests.get('https://pypi.org/search/?q=' + search_string)
try:
    response.raise_for_status()
except Exception as e:
    print(f'something went wrong:{e}')

soup = bs4.BeautifulSoup(response.text,'parser.html')

link_elem= soup.select('.package-snippet')
print(f'length of the search results: {len(link_elem)}')


num_open  = min(5, len(link_elem))


for i in range(num_open):
    url_to_open = 'https://pypi.org+'+link_elem[i].get('href')
    print(f'opening: {url_to_open}')
    webbrowser.open_new_tab(url_to_open)