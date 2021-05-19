from bs4 import BeautifulSoup
import requests

class CoronaParser:
    def __init__(self, URL, HEADERS):
        self.URL = URL
        self.HEADERS = HEADERS
        
    def parse(self):
        response = requests.get(self.URL, headers = self.HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_ = 'col-12 col-sm-12 statistic-col mt-10') 
        comps = [] 


        for i in items:
            comps.append({
                'cases': i.find('li', class_ = 'statistic-square').get_text(strip = True),
                'recovered': i.find('li', class_ = 'statistic-circleGreen').get_text(strip = True),
                'fatal': i.find('li', class_ = 'statistic-circleRed').get_text(strip = True),
            })  

        for j in comps:
            print(j['cases'], j['recovered'],  j['fatal'], sep='\n')
                
