import csv # これは先頭に記述してください
import re
import requests
from bs4 import BeautifulSoup

r = requests.get('https://jvca.jp/members/vc-members')
html = r.content
soup = BeautifulSoup(html, 'html.parser')
#VC_list = soup.find_all('ul', class_='members-list')
#print(members_list)
VC_list = soup.find_all('li', class_=re.compile('item'))

output_list = []
output_list.append(['会社名', 'リンク'])  # ヘッダ

#VCごとに処理
for vc in VC_list:
    name = vc.select('h3')
    #print(len(name))
    if len(name) <= 0:
         continue
    else:
        name = name[0].text.strip()

    link = ''
    if vc.find('a') is not None:  # a タグがない場合の対策
        link = vc.find('a').get('href')
    output_list.append([name, link])

with open('vc_list.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(output_list) 