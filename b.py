# -*- coding: utf-8 -*-
import bs4

#bs4で定義された関数を使ってsample.htmlを読み取る
soup = bs4.BeautifulSoup(
    open('/content/drive/MyDrive/二重矢板/0b.html', encoding = 'shift-jis'),
    'html.parser')

#sample.htmlをコンソールに出力
print(soup)

table = soup.find_all('table')
Support = table[0]  
print(Support)

td = Support.find_all('td')

# 常時 滑動
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])

# 常時 地盤支持力
a = td[2].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])

# 地震時 滑動
a = td[4].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])

# 地震時 地盤支持力
a = td[5].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '＜' in b:
  c = b.split('＜')

print(c[0])