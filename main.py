from bs4 import BeautifulSoup
import requests
import csv
import filecmp
import os
os.environ.setdefault('XAUTHORITY', '/home/user/.Xauthority')
os.environ.setdefault('DISPLAY', ':1')

url = "https://gopher.floodgap.com/gopher/gw?=gopher.club+70+312f70686c6f67732f"

response = requests.get(url)

phlogs = response.text

soup = BeautifulSoup(phlogs, "html.parser")

links = soup.find_all("a")

link_list = []
for link in links:
    link_list.append(link)

new_list = link_list[7:18]

small_list = []
for i, link in enumerate(new_list):
    if i % 2 == 0:
        small_list.append(link)
# html body table tbody tr td tt a

for link in small_list:
    link = str(link)
    print('\n')
    link = link.replace('<a href="', '')
    link = link.replace('">', ', ')
    link = link.replace('</a>', '')
    link = link.replace('2]', '2],')
    print(link)


with open('/home/steve/Python/gopherscraper/phlogs.csv', 'w') as f:

    for link in small_list:
        link = str(link)
        link = link.replace('<a href="', '')
        link = link.replace('">', ', ')
        link = link.replace('</a>', '')
        link = link.replace('2]', '2],')

        f.write(f"{link}\n")

if filecmp.cmp('/home/steve/Python/gopherscraper/phlogs.csv', '/home/steve/Python/gopherscraper/phlogs1.csv'):
    print("HI")
else:
    print("BYE")
    os.system('sh /home/steve/scripts/not.sh')
