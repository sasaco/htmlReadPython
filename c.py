# -*- coding: utf-8 -*-
import bs4

#bs4で定義された関数を使ってsample.htmlを読み取る
soup = bs4.BeautifulSoup(
    open('/content/drive/MyDrive/二重矢板/0c.html', encoding = 'shift-jis'),
    'html.parser')

#sample.htmlをコンソールに出力
print(soup)

table = soup.find_all('table')
SheetPile = table[0]  
print(SheetPile)

td = SheetPile.find_all('td')

# 常時 必要長
a = td[0].contents
print(a[0])

# 常時 地盤支持力
a = td[1].contents

if not '******' in a[0]:

  b = a[0].contents[0]

  if '≧' in b:
    c = b.split('≧')
  elif '＜' in b:
    c = b.split('＜')
  else:
    c = [0]
    
  print(c[0])

# 地震時 必要長
a = td[3].contents
print(a[0])

# 地震時 地盤支持力
a = td[4].contents

if not '******' in a[0]:

  b = a[0].contents[0]

  if '≧' in b:
    c = b.split('≧')
  elif '＜' in b:
    c = b.split('＜')
  else:
    c = [0]
    
  print(c[0])