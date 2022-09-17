# -*- coding: utf-8 -*-
import bs4

def read_d(file):

  #bs4で定義された関数を使ってsample.htmlを読み取る
  soup = bs4.BeautifulSoup(
      open(file, encoding = 'shift-jis'),
      'html.parser')

  table = soup.find_all('table')
  if len(table) == 0:
    raise ValueError("error!")

  PenetrationPathLength = table[0]  

  td = PenetrationPathLength.find_all('td')

  # 常時 浸透路長 
  a = td[0].contents

  # 常時 安全率　
  a = td[1].contents

  b = a[0].contents[0]

  if '******' in b:
    return '999.99'

  if '≧' in b:
    c = b.split('≧')
  elif '＜' in b:
    c = b.split('＜')


  # 先・末尾の空白を削除
  re1 = str.strip(c[0])
  re2 = str.strip(c[1])

  return re1, re2