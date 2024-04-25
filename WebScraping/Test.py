import requests
import subprocess
import validators
import datetime
import whois
from bs4 import BeautifulSoup

def getLinks(url):
    hrefsBase = []
    try:
        # Fetch the HTML content
        response = requests.get(url)
        html_content = response.content
        
        # Parse the HTML with Beautiful Soup
        soup = BeautifulSoup(html_content, "html.parser")
        
        links = soup.find_all('a')
        if len(links) == 0 or links[0] == None:
            return []
        hrefs = []
    
        hrefs = [link.get('href') for link in links if not link.get('href') == None and link.get('href').startswith('http')]
    
        for href in hrefs:
            if inBlackList(href):
                continue
            data = href.split("/")
            if data[2] not in hrefsBase:
                if "?" in data[2]:
                    data[2] = data[2].split("?")[0]
                if "#" in data[2]:
                    data[2] = data[2].split("#")[0]
                if validators.url(data[0] + "//" + data[2]):
                    hrefsBase.append(data[0] + "//" + data[2])
    except Exception as e:
        print("ERROR: ", e)
    return hrefsBase

def inBlackList(href):
    blackList = ["facebook", "google", "linkedin", "youtube", "twitter", "instagram"]
    if href in blackList:
        return True
    return False

def printTime():
    current_time = datetime.datetime.now()
    print("Current time:", current_time)

def whoisDomain(domain):
    try:
        whois.whois(domain)
    except:
        return True
    return False

def nslookup(i):
    command = "nslookup " + i
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result

printTime()
checkedList = ["https://www.xataka.com.mx", "https://www.diariodemorelos.com", "https://www.nytimes.com"]
notAvailableLinks = [] #456123: To find those are doesn't have any ip, I should use the windows command in shell: nslookup
listItems = getLinks(checkedList[0])
setItems = set(listItems)
while len(checkedList) < 500:#len(listItems) > 0:
    for li in listItems:
        if li not in checkedList:
            #"""
            command = "nslookup " + li
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                checkedList.append(li)
                listTemp = getLinks(li)
                if len(listTemp) == 0:
                    continue
                setItems.update(listTemp)
            else:
                notAvailableLinks.append(li)
            #"""
            """if whoisDomain(li):
                notAvailableLinks.append(li)
            else:
                checkedList.append(li)
                listTemp = getLinks(li)
                if len(listTemp) == 0:
                    continue
                setItems.update(listTemp)"""
    try:
        for ci in checkedList:
            setItems.remove(ci)
    except Exception as e:
        print("ERROR: ", e)
    listItems = list(setItems)

for li in checkedList:
    print(li)
print("notAvailableLinks: ")
for li in notAvailableLinks:
    print(li)
printTime()