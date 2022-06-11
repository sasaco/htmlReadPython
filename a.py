# -*- coding: utf-8 -*-
import bs4

from google.colab import drive
drive.mount('/content/drive')

#bs4で定義された関数を使ってsample.htmlを読み取る
soup = bs4.BeautifulSoup(
    open('/content/drive/MyDrive/二重矢板/0a.html', encoding = 'shift-jis'),
    'html.parser')

#sample.htmlをコンソールに出力
print(soup)


table = soup.find_all('table')
Dead = table[0] 
Quake = table[1] 
print(Dead)

td = Quake.find_all('td')

# 根入れ先端 安全率
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])

# 最小安全率 安全率
a = td[3].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])

# 現地盤面 安全率
a = td[5].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])