from bs4 import BeautifulSoup
import requests
import csv

from requests import NullHandler, models


file=open('arac.csv.csv','w')
writter=csv.writer(file)


sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]
   
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63"}
url=requests.get("https://www.arabam.com/ikinci-el?take=50",headers=header)
count=1
z=0
soup=BeautifulSoup(url.content,"html.parser",from_encoding='UTF-8')
i=soup.find("div",{"class":"listing-new-pagination cb tac mt16 pt16"}).span.text
cars=soup.find_all("tr",{"class":"listing-list-item pr should-hover bg-white"})
print(i)
for sehir in sehirler:
   for page in range(int(i)):
      url=requests.get(f"https://www.arabam.com/ikinci-el/otomobil-"+sehir.lower()+"?page="+str(10+page)+"&take=50",headers=header)
      soup=BeautifulSoup(url.content,"html.parser",from_encoding='UTF-8')
      cars=soup.find_all("tr",{"class":"listing-list-item pr should-hover bg-white"})
      for car in cars:
         carurl=car.find("td",attrs={"class":"listing-modelname pr"}).a.get("href")
         carvisiturl=requests.get("https://www.arabam.com/"+str(carurl)+"",headers=header,)
         carsoup=BeautifulSoup(carvisiturl.content,"html.parser",from_encoding='UTF-8')
         carprice=car.find("span",{"class":"db no-wrap"}).a.text
         
         carview=carsoup.find_all("span",{"bli-particle"})
         carinfo=[]
         carinfo.append(carprice)
         print(carview)
         if carsoup.find_all("span")[29].text == "Bu ilan yayında değildir.":
            continue
         else:
            for j in range(22):
               if j%2==1 and carview!=[]:   
                  carinfo.append(carview[j].text.strip())
                  print(carview[j].text)
         
         print("\n")
         print(count)
         writter.writerow([carinfo[0],carinfo[1],carinfo[2],carinfo[3],carinfo[4],carinfo[5],carinfo[6],carinfo[7],carinfo[8],carinfo[9],carinfo[10],carinfo[11]])
         count +=1
         if count==21:
            break   
         
      
   
file.close()

   

