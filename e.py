# -*- coding: utf-8 -*-
import bs4

#bs4で定義された関数を使ってsample.htmlを読み取る
soup = bs4.BeautifulSoup(
    open('/content/drive/MyDrive/二重矢板/0e.html', encoding = 'shift-jis'),
    'html.parser')

#sample.htmlをコンソールに出力
print(soup)

table = soup.find_all('table')

Stress = table[0] 
Tensile1 = table[1] 
Tensile2 = table[2] 
Abdominal1 = table[3] 
Abdominal2 = table[4] 

print(Stress)

"""## ■壁体応力度"""

td = Stress.find_all('td')

# 常時 曲げ応力度
a = td[0].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 常時 せん断応力度
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 地震時 曲げ応力度
a = td[2].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 地震時 せん断応力度
a = td[3].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

"""## 引張応力度 1段目"""

td = Tensile1.find_all('td')
print(Tensile1)

# 常時 堤内側
a = td[0].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 地震時 堤内側
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

"""## 引張応力度 2段目"""

td = Tensile2.find_all('td')
print(Tensile2)

# 常時 堤内側
a = td[0].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 地震時 堤内側
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

"""## ■腹起し材応力度 1段目"""

td = Abdominal1.find_all('td')
print(Abdominal1)

# 常時 堤内側
a = td[0].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 地震時 堤内側
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

"""## ■腹起し材応力度 2段目"""

td = Abdominal2.find_all('td')
print(Abdominal2)

# 常時 堤内側
a = td[0].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])

# 地震時 堤内側
a = td[1].contents
b = a[0].contents[0]

if '≧' in b:
  c = b.split('≧')
elif '≦' in b:
  c = b.split('≦')
elif '＜' in b:
  c = b.split('＜')
  
print(c[0])