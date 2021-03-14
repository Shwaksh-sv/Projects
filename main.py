import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.brownells.com/"
r = requests.get(url)
htmlContent = r.content
pah = [["Product Title", "Hyperlink"]]
schm = [["Schematics"]]
supp = [["Suppliers arranged alphabetically"]]
stocks = [["Products and their Stocks"], [" "]]
soup = BeautifulSoup(htmlContent, 'lxml')

productAndHyperlink = soup.find('nav', {'class': 'dbl desktop'})
k = productAndHyperlink.find_all('a')
for i in k:
    pah.append([i['title'], i['href']])

with open('BrownellsScraping', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(pah)
    file.close()

with open('BrownellsScraping', 'r') as file:
    data = csv.reader(file)
    for row in data:
        print(row[0] + "\t" + row[1])
schematics = soup.find('ul', {'class': 'mfrList'})
l = schematics.find_all('a')
print()
print()
# print("schematics\n")
for i in l:
    if ".htm" not in i['href']:
        schm.append(['https://www.brownells.com' + i['href']])
    else:
        schm.append([i['href']])
with open('BrownellsScrapingSchematics', 'w', newline='') as file1:
    writer = csv.writer(file1)
    writer.writerows(schm)
    file.close()

with open('BrownellsScrapingSchematics', 'r') as file1:
    data1 = csv.reader(file1)
    for row in data1:
        print(row[0])
suppliers = soup.find('ul', {'class': 'alphaList'})
m = suppliers.find_all('a')
print()
print()
for i in m:
    supp.append([i['href']])

with open('BrownellsScrapingSuppliers', 'w', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerows(supp)
    file.close()

with open('BrownellsScrapingSuppliers', 'r') as file2:
    data2 = csv.reader(file2)
    for row in data2:
        print(row[0])
print()

urlpsf = ["https://www.brownells.com/firearms/index.htm?f_a=1", "https://www.brownells.com/firearms/index.htm?f_a=13",
          "https://www.brownells.com/firearms/index.htm?f_a=25", "https://www.brownells.com/firearms/index.htm?f_a=37",
          "https://www.brownells.com/firearms/index.htm?f_a=49"]
stocks.append(["FireArms and their status"])
stocks.append([" "])
for z in urlpsf:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])

urlpsrp = ["https://www.brownells.com/rifle-parts/index.htm", "https://www.brownells.com/rifle-parts/index.htm?f_a=13",
           "https://www.brownells.com/rifle-parts/index.htm?f_a=25",
           "https://www.brownells.com/rifle-parts/index.htm?f_a=37",
           "https://www.brownells.com/rifle-parts/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Rifle Parts and their status"])
stocks.append([" "])
for z in urlpsrp:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpshp = ["https://www.brownells.com/handgun-parts/index.htm",
           "https://www.brownells.com/handgun-parts/index.htm?f_a=13",
           "https://www.brownells.com/handgun-parts/index.htm?f_a=25",
           "https://www.brownells.com/handgun-parts/index.htm?f_a=37",
           "https://www.brownells.com/handgun-parts/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Handgun Parts and their status"])
stocks.append([" "])
for z in urlpshp:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpssp = ["https://www.brownells.com/shotgun-parts/index.htm",
           "https://www.brownells.com/shotgun-parts/index.htm?f_a=13",
           "https://www.brownells.com/shotgun-parts/index.htm?f_a=25",
           "https://www.brownells.com/shotgun-parts/index.htm?f_a=37",
           "https://www.brownells.com/shotgun-parts/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Shotgun Parts and their status"])
stocks.append([" "])
for z in urlpssp:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsm = ["https://www.brownells.com/magazines/index.htm",
          "https://www.brownells.com/magazines/index.htm?f_a=13",
          "https://www.brownells.com/magazines/index.htm?f_a=25",
          "https://www.brownells.com/magazines/index.htm?f_a=37",
          "https://www.brownells.com/magazines/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Magazines and their status"])
stocks.append([" "])
for z in urlpsm:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsa = ["https://www.brownells.com/ammunition/index.htm",
          "https://www.brownells.com/ammunition/index.htm?f_a=13",
          "https://www.brownells.com/ammunition/index.htm?f_a=25",
          "https://www.brownells.com/ammunition/index.htm?f_a=37",
          "https://www.brownells.com/ammunition/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Ammunitions and their status"])
stocks.append([" "])
for z in urlpsa:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsre = ["https://www.brownells.com/reloading/index.htm",
           "https://www.brownells.com/reloading/index.htm?f_a=13",
           "https://www.brownells.com/reloading/index.htm?f_a=25",
           "https://www.brownells.com/reloading/index.htm?f_a=37",
           "https://www.brownells.com/reloading/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Relodings and their status"])
stocks.append([" "])
for z in urlpsre:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpssa = ["https://www.brownells.com/shooting-accessories/index.htm",
           "https://www.brownells.com/shooting-accessories/index.htm?f_a=13",
           "https://www.brownells.com/shooting-accessories/index.htm?f_a=25",
           "https://www.brownells.com/shooting-accessories/index.htm?f_a=37",
           "https://www.brownells.com/shooting-accessories/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Shooting Accessories and their status"])
stocks.append([" "])
for z in urlpssa:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsgts = ["https://www.brownells.com/gunsmith-tools-supplies/index.htm",
            "https://www.brownells.com/gunsmith-tools-supplies/index.htm?f_a=13",
            "https://www.brownells.com/gunsmith-tools-supplies/index.htm?f_a=25",
            "https://www.brownells.com/gunsmith-tools-supplies/index.htm?f_a=37",
            "https://www.brownells.com/gunsmith-tools-supplies/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Gunsmith tools supplies and their status"])
stocks.append([" "])
for z in urlpsgts:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsop = ["https://www.brownells.com/optics-mounting/index.htm",
           "https://www.brownells.com/optics-mounting/index.htm?f_a=13",
           "https://www.brownells.com/optics-mounting/index.htm?f_a=25",
           "https://www.brownells.com/optics-mounting/index.htm?f_a=37",
           "https://www.brownells.com/optics-mounting/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Optics Mounting and their status"])
stocks.append([" "])
for z in urlpsop:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsgcc = ["https://www.brownells.com/gun-cleaning-chemicals/index.htm",
            "https://www.brownells.com/gun-cleaning-chemicals/index.htm?f_a=13",
            "https://www.brownells.com/gun-cleaning-chemicals/index.htm?f_a=25",
            "https://www.brownells.com/gun-cleaning-chemicals/index.htm?f_a=37",
            "https://www.brownells.com/gun-cleaning-chemicals/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Gun cleaning chemicals and their status"])
stocks.append([" "])
for z in urlpsgcc:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
urlpsesg = ["https://www.brownells.com/emergency-survival-gear/index.htm",
            "https://www.brownells.com/emergency-survival-gear/index.htm?f_a=13",
            "https://www.brownells.com/emergency-survival-gear/index.htm?f_a=25",
            "https://www.brownells.com/emergency-survival-gear/index.htm?f_a=37",
            "https://www.brownells.com/emergency-survival-gear/index.htm?f_a=49"]
stocks.append([" "])
stocks.append(["Emergency survival gear and their status"])
stocks.append([" "])
for z in urlpsesg:
    page = requests.get(z)
    soup1 = BeautifulSoup(page.content, 'lxml')
    name = soup1.find_all('span', itemprop='name')
    status = soup1.find_all('p', {'class': 'status'}, itemprop='availability')
    length = len(name)
    for i in range(length):
        stocks.append([name[i].text + ' - ' + status[i].text])
with open('BrownellsScrapingProductStatus', 'w', newline='') as file3:
    writer = csv.writer(file3)
    writer.writerows(stocks)
    file.close()

with open('BrownellsScrapingProductStatus', 'r') as file3:
    data3 = csv.reader(file3)
    for row in data3:
        print(row[0])