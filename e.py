# -*- coding: utf-8 -*-
import bs4

def read_value(a):
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



def read_e(file):

  #bs4で定義された関数を使ってsample.htmlを読み取る
  soup = bs4.BeautifulSoup(
      open(file, encoding = 'shift-jis'),
      'html.parser')

  #sample.htmlをコンソールに出力
  #print(soup)

  table = soup.find_all('table')

  Stress = table[0] 
  Tensile1 = table[1] 
  Tensile2 = table[2] 
  Abdominal1 = table[3] 
  Abdominal2 = table[4] 

  #print(Stress)

  """## ■壁体応力度"""

  td = Stress.find_all('td')

  # 常時 曲げ応力度
  a = td[0].contents
  c = read_value(a)
  
  re1_0 = c[0] 
  re1_1 = c[1] 

  # 常時 せん断応力度
  a = td[1].contents
  c = read_value(a)

  re2_0 = c[0]
  re2_1 = c[1]


  # 地震時 曲げ応力度
  a = td[2].contents
  c = read_value(a)

  re3_0 = c[0]
  re3_1 = c[1]


  # 地震時 せん断応力度
  a = td[3].contents
  c = read_value(a)

  re4_0 = c[0]
  re4_1 = c[1]


  """## 引張応力度 1段目"""
  td = Tensile1.find_all('td')

  # 常時 堤内側
  a = td[0].contents
  c = read_value(a)

  re5_0 = c[0]
  re5_1 = c[1]


  # 地震時 堤内側
  a = td[1].contents
  c = read_value(a)

  re6_0 = c[0]
  re6_1 = c[1]


  """## 引張応力度 2段目"""

  td = Tensile2.find_all('td')

  # 常時 堤内側
  a = td[0].contents
  c = read_value(a)

  re7_0 = c[0]  
  re7_1 = c[1]  


  # 地震時 堤内側
  a = td[1].contents
  c = read_value(a)

  re8_0 = c[0]  
  re8_1 = c[1]  


  """## ■腹起し材応力度 1段目"""

  td = Abdominal1.find_all('td')

  # 常時 堤内側
  a = td[0].contents
  c = read_value(a)

  re9_0 = c[0]  
  re9_1 = c[1]  


  # 地震時 堤内側
  a = td[1].contents
  c = read_value(a)

  re10_0 = c[0]  
  re10_1 = c[1]  


  """## ■腹起し材応力度 2段目"""

  td = Abdominal2.find_all('td')
  #print(Abdominal2)

  # 常時 堤内側
  a = td[0].contents
  c = read_value(a)

  re11_0 = c[0]  
  re11_1 = c[1]  


  # 地震時 堤内側
  a = td[1].contents
  c = read_value(a)

  re12_0 = c[0]  
  re12_1 = c[1]  

  return re1_0, re1_1, re2_0, re2_1, re3_0, re3_1, re4_0, re4_1, re5_0, re5_1, \
          re6_0, re6_1, re7_0, re7_1, re8_0, re8_1, re9_0, re9_1, re10_0, re10_1, \
          re11_0, re11_1, re12_0, re12_1