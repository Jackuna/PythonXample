from bs4 import BeautifulSoup
import requests
import re
import sys


CarrierList=[]
CarrierStatus=[]
ApiDict={}


def parse_webpage():
    
    global table_class
    global all_tableRow
    global all_href

    try:
        page_url = "https://www.shippingapimonitor.com/index.html"
        page_request = requests.get(page_url)
        soup = BeautifulSoup(page_request.text, 'html.parser')
        
    except:
        print("Either your Internet is not working or URL is wrong/down ")
        sys.exit()
        

    table_class = soup.find(class_='clear')
    all_tableRow = table_class.find_all('tr')
    all_href = table_class.find_all('a')



def carrier_options():
    
    global select
    select_list =['usps','ups','candapost','fedex']
    select = input ("Choose from USPS | UPS | CanadaPost | Fedex : Provide your carrier in lower case : ")

    if select in select_list:
        pass
    else:
        select = input ("We mean to say choose from these options: [ usps,ups,candapost,fedex ] ")
        if select in select_list:
            pass
        else:
            sys.exit()
        

        
def parse_api_status():
    for atags in all_href:
        tags = atags.contents[0]
        titles=re.findall("title=.*/>",str(tags),re.IGNORECASE)
        carrier=re.findall('".*"',str(titles))[0].replace('"','')
        CarrierList.append(carrier.lower().replace(' ',''))
        
    for btags in all_tableRow:
        all_tds = btags.find_all('td')
        rows = [i.text for i in all_tds ]
        if len(rows) == 0:
            pass
        else:
            rows.pop(0)
            CarrierStatus.append(rows)

        for key, value in zip(CarrierList,CarrierStatus):
            ApiDict.update({key:value})

    print(ApiDict)

    try:
        if len(select)==0:
            pass

        else:

            print(select.upper(), "Live API Status : ", ApiDict[select][0])
        
    except: 
        sys.exit()
        


run = parse_webpage()
#carrier_options()
parse_api_status()
    




