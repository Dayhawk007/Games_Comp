import requests
from bs4 import BeautifulSoup
import pandas as pd
search_query=input("Enter the name of the game\n")
details=open("Details.csv","w")
details.write('Store,Name,Price\n')
details.flush()
s_l=search_query.split()
s="+".join(s_l)
res=requests.get("https://gocdkeys.com/en/search?product="+str(s))
soup=BeautifulSoup(res.content,features='html.parser')
for a in soup.find_all('a'):
    if search_query in a.text:
        link=a.get('href')
        kek=requests.get("https://gocdkeys.com"+str(link))
        keksoup=BeautifulSoup(kek.content,features='html.parser')
        #print(kek.text)
        for nam,pric in zip(keksoup.find_all('meta',{'itemprop':'name'}),keksoup.find_all('b',{'itemprop':'price'})):
            details.write(f"{str(nam.get('content'))} ,{search_query} ,{pric.text} \n")
        break
details.flush()
game_file=pd.read_csv("Details.csv")
print(game_file)









