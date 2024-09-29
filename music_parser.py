import requests
import wget
from bs4 import BeautifulSoup as bs


#1 поколение парсера


#def get_music(query):
#   query = " ".join(query.split()).strip().replace(" ", "+")      
#   url = f"https://rmf.muzmo.cc/search?q={query}"
#   r = requests.get(url)
#   try:
#      data = bs(r.text, "html.parser")
#      name = data.findAll('a', class_="block")   
#      global titles
#      global links
#      titles=[]
#      links=[]       
#      href=[i['href']  for i in name if i['href'].startswith('/get_new?')]  
#      for item in name:       
#      	filter= ("".join(" ".join(item.text.split()).split(", 320Kb/s")))
#      	if filter.endswith(')'):
#      	   titles.append((filter))      
#      for i in href:
#      	links.append((f"https://rmf.muzmo.cc{i}"))
#           
#   except Exception as ex:
#    print(f"[!]Error: {ex}")
 
 
 #2 поколение парсера
 
#def get_music(query):   
#   query = " ".join(query.split()).strip().replace(" ", "+")     
#   url = f"https://rmf.muzmo.cc/search?q={query}"   
#   r = requests.get(url)
#   try:
#      data = bs(r.text, "html.parser")
#      name = data.findAll('a', class_="block")       
#      global songs
#      global links      
#      songs=[]
#      links=[]       
#      href=[i['href']  for i in name if i['href'].startswith('/get_new?')]  
#      for item in name:       
#      	filter= ("".join(" ".join(item.text.split()).split(", 320Kb/s")))
#      	if filter.endswith(')'):      	   
#      	   songs.append((filter))      
#      for i in href:
#      	links.append((f"https://rmf.muzmo.cc{i}"))
#   except Exception as ex:
#    print(f"[!]Error: {ex}")      
#   if songs and links:
#            return songs, links          
#   else:       
#          new_link = href=[i['href']  for i in name if i['href'].startswith('/search')][0]          
#          link=f"https://rmf.muzmo.cc{new_link}"          
#          r = requests.get(link)
#          try:
#            data = bs(r.text, "html.parser")
#            name = data.findAll('a', class_="block")                     
#            href=[i['href']  for i in name if i['href'].startswith('/get_new?')]  
#            for item in name:
#            	filter= ("".join(" ".join(item.text.split()).split(", 320Kb/s")))
#            	if filter.endswith(')'):
#            		songs.append((filter))      
#            for i in href:
#            	links.append((f"https://rmf.muzmo.cc{i}"))
#          except Exception as ex:
#              print(f"[!]Error: {ex}") 
#          if songs and links:
#            return songs, links         
#          else:                  
#             print("К сожалению, ничего не найдено.")
 
             
# 3  поколение парсера 
max_search_circles=50                     
                                                 
def get_music(query):  
 global songs
 global links     
 songs=[]
 links=[]   
 a=0 
 while True:
   if a == max_search_circles:
   	print("К сожалению, ничего не найдено.")   	
   	break
   a+=1  
   print(a)
   query = " ".join(query.split()).strip().replace(" ", "+")     
   url = f"https://rmf.muzmo.cc/search?q={query}"   
   r = requests.get(url)
   try:
      data = bs(r.text, "html.parser")
      name = data.findAll('a', class_="block")            
      href=[i['href']  for i in name if i['href'].startswith('/get_new?')]  
      for item in name:       
      	filter= ("".join(" ".join(item.text.split()).split(", 320Kb/s")))
      	if filter.endswith(')'):      	   
      	   songs.append((filter))      
      for i in href:
      	links.append((f"https://rmf.muzmo.cc{i}"))
   except Exception as ex:
    print(f"[!]Error: {ex}")      
   if songs and links:
            return songs, links
            break
   else:
          try:       
            new_link = href=[i['href']  for i in name if i['href'].startswith('/search')][0]          
            link=f"https://rmf.muzmo.cc{new_link}"          
            r = requests.get(link)          
            data = bs(r.text, "html.parser")
            name = data.findAll('a', class_="block")                     
            href=[i['href']  for i in name if i['href'].startswith('/get_new?')]  
            for item in name:
            	filter= ("".join(" ".join(item.text.split()).split(", 320Kb/s")))
            	if filter.endswith(')'):
            		songs.append((filter))      
            for i in href:
            	links.append((f"https://rmf.muzmo.cc{i}"))
          except Exception as ex:
              print(f"[!]Error: {ex}") 
          if songs and links:
            return songs, links
            break
                
                               
def get_downloadlink(link):      
   data = bs(requests.get(link).text,'html.parser')
   name = data.findAll('a', class_='block')
   href=[i['href']  for i in name if i['href'].startswith('/get/music')][0]
   link=f"https://rmf.muzmo.cc{href}"  
   return link
    
get_music("Ваш запрос") 

#используется для скачивания песни с помощью  wget

"""link = links[0]
print(get_downloadlink(link))
wget.download(get_downloadlink(link))"""


#используется для вывода результатов поика

num = 0   
for i in songs:  
  print(f"Название:{i}\nСсылка:{links[num]}")
  num+=1
  
