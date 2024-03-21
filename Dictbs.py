from bs4 import BeautifulSoup as bs
import requests
print("Enter the word you want to find the meaning")
word=input()
url="https://www.dictionary.com/browse/"+word
try:
    page=requests.get(url)
    soup=bs(page.content,'lxml')
except:
    print("Check your internet connection")
    exit(-1)
try:
    pos=soup.findAll("span",{"class":"luna-pos"})[0].text
    meanings=list(soup.find("div",{"class":"default-content"}))

except:
    print("Please check the word you have entered")
    exit(-1)

print(word+":"+pos)
for i in range(0,len(meanings)):
    print(str(i+1)+" "+meanings[i].text)
