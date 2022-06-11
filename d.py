# -*- coding: utf-8 -*-
import bs4

#bs4で定義された関数を使ってsample.htmlを読み取る
soup = bs4.BeautifulSoup(
    open('/content/drive/MyDrive/二重矢板/0d.html', encoding = 'shift-jis'),
    'html.parser')

#sample.htmlをコンソールに出力
print(soup)

table = soup.find_all('table')
PenetrationPathLength = table[0]  
print(PenetrationPathLength)

td = PenetrationPathLength.find_all('td')

# 常時 浸透路長 
a = td[0].contents
print(a[0])

# 常時 安全率　
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