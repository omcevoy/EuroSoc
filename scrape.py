import requests
from bs4 import BeautifulSoup
import unicodecsv as csv
urlBeg = "https://www.spotrac.com/epl/"
urlEnd = ["afc-bournemouth/payroll/", "arsenal-f.c/payroll/", "aston-villa-f.c/payroll/", "brighton-hove-albion/payroll", "burnley-f.c/payroll/", "chelsea-f.c/payroll/", "crystal-palace/payroll/", "everton-f.c/payroll/", "leicester-city/payroll/", "liverpool-f.c/payroll/", "manchester-city-f.c/payroll/", "manchester-united-f.c/payroll/", "newcastle-united-f.c/payroll/", "norwich-city-f.c/payroll/", "sheffield-united-f.c/payroll/", "southampton-f.c/payroll/", "tottenham-hotspur-f.c/payroll/", "watford/payroll/", "west-ham-united-f.c/payroll/", "wolverhampton-wanderers-f.c/payroll/"]

clubName = ["AFC Bournermouth", "Arsenal FC", "Aston Villa FC", "Brighton & Hove Albion FC", "Burnley FC", "Chelsea FC", "Crystal Palace FC", "Everton FC", "Leicester City FC", "Liverpool FC", "Manchester City FC", "Manchester United FC", "Newcastle United FC", "Norwich City FC", "Sheffield United FC", "Southampton FC", "Tottenham Hotspur FC", "Watford FC", "West Ham United FC", "Wolverhampton Wanderers FC"] 


data = []
for i in range(20):
    url = urlBeg + urlEnd[i]
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')

    rows = soup.find_all('tr')

    for tr in soup.find_all('tr'): #goes through tr elements
        rowData = []
        tdC = 0 #this will get rid of name duplicate
        for td in tr.find_all('td'):
            col = td.text.strip()
            if (tdC == 0):
                newCol = col.split('\n')
                try:
                    if len(newCol[1]) > 0:
                        rowData.append(newCol[1])
                except:
                    continue
            else:
                col.strip('"'); #takes quotes off wages
                if tdC < 3:
                    rowData.append(col) #ignoring 3rd column since it's vacant
                if tdC > 3:
                    col = col[1:].replace(",", "") #removes commas from wages
                    try:
                        col = int(col)
                        rowData.append(int(col))
                    except:
                        continue
            tdC +=1
        if len(rowData) > 0: #only append if there's actual data
            if type(rowData[-1]) is int: #only accepting data with player wages
                rowData.append(clubName[i]) 
                data.append(rowData)

with open("playerData.csv", 'a') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(data)


