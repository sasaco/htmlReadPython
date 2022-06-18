# -*- coding: utf-8 -*-
import bs4

def read_value(a):

  if '******' in a[0]:
    return ['999.99']

  b = a[0].contents[0]
  if '≧' in b:
    c = b.split('≧')
  elif '＜' in b:
    c = b.split('＜')

  # 先・末尾の空白を削除
  d = list(map(str.strip, c))

  return d

def read_c(file):
#bs4で定義された関数を使ってsample.htmlを読み取る
  soup = bs4.BeautifulSoup(
      open(file, encoding = 'shift-jis'),
      'html.parser')

  table = soup.find_all('table')
  SheetPile = table[0]  

  td = SheetPile.find_all('td')

  # 常時 必要長
  a = td[0].contents

  # 常時 地盤支持力
  c = read_value(td[1].contents)
  re1 = c[0]

  # 地震時 必要長
  a = td[3].contents

  # 地震時 地盤支持力
  c = read_value(td[4].contents)
  re2 = c[0]
  
  return re1, re2