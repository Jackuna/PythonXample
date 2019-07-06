#!/usr/bin/python3

# grab_appd_agent_ver.py : Py Script meant to extract appdynamics
#                          agents version with node & tier name.
#                          Script creates CSV & XLSX file too
#                          Script shows tabular o/p & saves data. 
# Usage 
#
# ./grab_appd_agent_ver.py < appd_application_name >  < prd/nprd >
#
# python3 grab_appd_agent_ver.py < appd_application_name >< prd/nprd >
# python3 grab_appd_agent_ver.py < appd_application_name >  prd
# python3 grab_appd_agent_ver.py < appd_application_name >  nprd 
#
# Disable [comment] function create_xls() to stop creating additional xlsx 
#
# Dependencies ( Python3 with below additional liabraries) :
#
# prettytable ==> "pip install prettytable"
# pandas      ==> "pip install pandas"
#
# Author : jackuna [ https://github.com/Jackuna/ ]


import requests
import sys
import csv
from prettytable import PrettyTable
import pandas as pd


# Change Controller URL and Appd Application Name as per requirement
#
# PRD    ==> controller_url = "https://yourorganizationNPRD.saas.appdynamics.com/controller/"
# NONPRD ==> controller_url = "https://yourorganizationPRD.saas.appdynamics.com/controller/"
# 
# app_name = AppDynamics Application name.
# ENV = PRD or NPRD 
# tier_list = Tiers within Application.
# host_list = Nodes within application.
# controller_url = URL for your AppDynamics controller.
# user_and_account = username and appDaccount [ ex : jackuna@cyberkeedaprod ]
# cred = Password



# Global Varibales

app_name = ""
ENV = ""
tier_list = []
host_list = []
csv_data = []
controller_url = ""
user_and_account = ""
cred = ""


def check_argument():
    
    global app_name
    global ENV

    if (len(sys.argv)) > 2:

        app_name = str(sys.argv[1])
        ENV = str(sys.argv[2])
        
    else:
        
        print()
        print ('-----------------------------------------------------------------------------')
        print ('#                                                                           #')
        print ("#                  You must set argument !!!                                #")
        print ("# Usage:                                                                    #")
        print ('#                                                                           #')
        print ("# python3 grab_appd_agent_ver.py < appd_application_name > < prd/nprd >     #")
        print ('#                                                                           #')
        print ("-----------------------------------------------------------------------------")
        sys.exit()



def check_env():

    global controller_url
    global user_and_account
    global cred
    
    if ENV == "nprd":
        controller_url = "https://yourorganizationNPRD.saas.appdynamics.com/controller/"
        user_and_account = "jackuna@cyberkeedanprod"
        cred = "cyberkeedapassword"

    elif ENV == "prd":
        controller_url = "https://yourorganizationPRD.saas.appdynamics.com/controller/"
        user_and_account = "jackuna@cyberkeedaprod"
        cred = "keedapassword"
    
    else:
        print()
        print ('-----------------------------------------------------------------------------')
        print ('#                                                                           #')
        print ("#                  You must set 2nd argument ( prd or nprd )                #")
        print ("# Usage:                                                                    #")
        print ('#                                                                           #')
        print ("# python3 grab_appd_agent_ver.py < appd_application_name > < prd/nprd >     #")
        print ('#                                                                           #')
        print ("-----------------------------------------------------------------------------")
        sys.exit()


def grab_tiers():

    rest_endpoint = "rest/applications/"+app_name+"/tiers?output=JSON"

    GET_url = controller_url+rest_endpoint

    get_response = requests.get(GET_url, auth=(user_and_account, cred))

    newval = get_response.json()
    lens = len(newval)

    for val in range(0,lens):

        tier_list.append(newval[val]["name"])

    # Uncomment to enable debugging
    #print(tier_list)



def grab_nodes():
    
    tabular_table = PrettyTable()
    tabular_table.field_names = ["HostID","Tier Name","AppAgent","Machine Agent"]
    tabular_table.align["HostID"] = "l"
    #obj.writerow(("HostID","Tier Name","AppAgent","Machine Agent"))

    for list_val in tier_list:
        
        rest_endpoint = "rest/applications/"+app_name+"/tiers/"+list_val+"/nodes?output=JSON"
        some_url = controller_url+rest_endpoint

        response = requests.get(some_url, auth=(user_and_account, cred))
        val = response.json()
        lens = len(val)
        
        for newval in range(0,lens):
            HID = val[newval]["machineName"]
            host_list.append(HID)
            AID = " ".join(val[newval]['appAgentVersion'].split()[:3])
            MID = " ".join(val[newval]['machineAgentVersion'].split()[:3])
            
            #tabular_table.add_row([CYAN+HID+N, AID, MID])
            tabular_table.add_row([HID, list_val, AID, MID])
            csvfile = open(app_name+".csv",'w', newline='')
            obj=csv.writer(csvfile)
            obj.writerow(("HostID","Tier Name","AppAgent","Machine Agent"))
            csv_data.append((HID, list_val, AID, MID))
        

            obj.writerows(csv_data)
        
    print(tabular_table)
    csvfile.close()
    # Uncomment to enable debugging
    #print(host_list)


def create_xls():

    CS = pd.read_csv(app_name+".csv")
    feilds = CS.loc[:, ["HostID","Tier Name","AppAgent","Machine Agent"]]

    writer = pd.ExcelWriter(app_name+'.xlsx', engine='xlsxwriter')
    feilds.to_excel(writer, sheet_name=app_name, index=False)

    workbook  = writer.book

    worksheet = writer.sheets[app_name]
    worksheet.set_column(0, 5, 20)
    writer.save()


# Calling Functions

check_argument()
check_env()
grab_tiers()
grab_nodes()
create_xls()
