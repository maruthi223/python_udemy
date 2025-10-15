import requests
from bs4 import BeautifulSoup

res = requests.get(url='https://www.cbit.ac.in/')
soup = BeautifulSoup(res.content,'html.parser')
link = soup.find_all("div",class_ = "counter-col")[2]
pack = link.find('span' , class_ = 'counter-value')
s=pack['data-count']
print(s)