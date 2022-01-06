import requests
from bs4 import BeautifulSoup

#1
# URL = 'https://www.vit.ac.in'
# response = requests.get(URL,verify=False)
# soup = BeautifulSoup(response.text, 'lxml') 

# print("Titles:\n")
# title = soup.findAll('title')
# print(title[0].text)


#2A
# print("\n\nA tags with class nav-link\n")
# for link in soup.find_all('a',class_='nav-link'):
#     print(link.text)



# print("\n\nFaculties with class title2 with research work: \n")
# for link in soup.findAll('div',class_='lightbox_course fancybox-content'):
#     print(link.text.strip())
#     print("\n")


# URL = 'https://vit.ac.in/school/allfaculty/site/computer-applications'
# response = requests.get(URL,verify=False)
# soup = BeautifulSoup(response.text, 'html.parser').find('span',class_='soclia_links')

# 2B
# print("\nSocial links: ")

# for link in soup.children:
#     print("Link: " + link['href'])
#     print("Class: " + str(link['class'])+"\n")


import requests
from bs4 import BeautifulSoup

# URL = "https://www.batimes.com.ar"
# response = requests.get(URL,verify=False)
# soup = BeautifulSoup(response.text, 'html.parser')


# print("All the image sources:\n")
# for ele in soup.findAll('img'):
#     if(ele['src']):
#         print("Image Src: " + str(ele['src']))
#         print("\n")
    

# print("\nItems with given class:")
# for item in soup.findAll(class_='nav-item text-uppercase px-0'):
#     print(item.text.strip())

# import termtables as tt

# import requests
# from bs4 import BeautifulSoup

# URL = "https://vit.ac.in/school/allfaculty/site/computer-applications"
# response = requests.get(URL,headers={'User-Agent':"Mozilla/5.0"}).text
# soup = BeautifulSoup(response,'lxml')

# finalList=[]
# print("\n\nFaculties with class title2 with research work: \n")
# for link in soup.findAll('div',class_='lightbox_course fancybox-content'):
#     facList = link.text.strip().split("\n")
#     if(facList[0]!=facList[-1]):
#         finalList.append(["\033[91m"+facList[0],"\033[96m"+facList[-1]])
#     print("\n")

# string = tt.to_string(
#     finalList,
#     header=["\033[92m Fac Name", "\033[92m Research Area "],
#     style=tt.styles.ascii_thin_double,
#     # alignment="ll",
#     # padding=(0, 1),
# )
# print(string)

# for link in soup.findAll('div'):
#     print(link['class'])
#     if(link['class']):
#         print(link['class'])
#     if(link.children):
#         for sub in  link.children:
#             if(str(sub.name)!='None'):
#                 print("     -"+str(sub.name))

import requests
from bs4 import BeautifulSoup

URL = "https://sermitsiaq.ag/english"
response = requests.get(URL,headers={'User-Agent':"Mozilla/5.0"}).text
soup = BeautifulSoup(response,'lxml')

print("Ele with article tags")
for article in soup.findAll('article'):
    print(article.text.strip().replace(' ', '')+"\n")


# import requests
# from bs4 import BeautifulSoup as bs

# url='https://www.batimes.com.ar/'
# html_text=requests.get(url,headers={'User-Agent':'Mozilla/5.0'}).text
# soup=bs(html_text,'html.parser')
# def WordFind(element):
#     string=str(element.find(text=True,recursive=False))
#     if "Matías Lammens" in string:
#         return True
#     return False
# for list1 in soup.find_all(WordFind):
#     print(list1)

def printDom(element,maxDepth,space=0):
    if maxDepth>0:
        if space==0:
            print("┌>",element.name)
        else:
            print("| "*space+"├>",element.name)
    for i in element.findChildren(recursive=False):
        printDom(i,maxDepth-1,space+1)
    return
printDom(soup.html,7)
