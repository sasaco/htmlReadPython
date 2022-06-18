# -*- coding: utf-8 -*-
import bs4

def read_value(a):

  if '******' in a[0]:
    return ['999.99']

  b = a[0].contents[0]
  if '≧' in b:
    c = b.split('≧')
  elif '≦' in b:
    c = b.split('≦')
  elif '＜' in b:
    c = b.split('＜')
  elif '＞' in b:
    c = b.split('＞')

  # 先・末尾の空白を削除
  d = list(map(str.strip, c))

  return d


def read_table(Target):
  td = Target.find_all('td')

  #print(td)
  # 根入れ先端 安全率
  a = td[1].contents
  c = read_value(a)
  re1 = c[0] #値入れ先端　安全率の応答値

  # 最小安全率 安全率
  a = td[3].contents
  c = read_value(a)
  re2 = c[0]

  # 現地盤面 安全率
  a = td[5].contents
  c = read_value(a)
  re3 = c[0]

  return re1, re2, re3


def read_a(file):

  #bs4で定義された関数を使ってsample.htmlを読み取る
  soup = bs4.BeautifulSoup(
      open(file, encoding = 'shift-jis'),
      'html.parser')


  table = soup.find_all('table')
  Dead = table[0] 
  Quake = table[1] 
  
  a1, a2, a3 = read_table(Dead)
  a4, a5, a6 = read_table(Quake)

  return a1, a2, a3, a4, a5, a6

