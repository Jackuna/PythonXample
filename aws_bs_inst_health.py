# ----------------------------------------------------------------------------------------------------------------------------  #
# aws_bs_inst_health.py : AWS Beanstalk Health Status, An xample for the implemenantion of python's boto3 library with
# other python packages. 
# Script will show the overall health of beanstalk application with it's respective instances health too.
# 
# So what's new ? : The look and feel of all the details in a tabular format. 
# 
# Assumptions wthin the script:
# Total defined instnaces within Beanstalk : Min : 1, Mac : 4
# 
# Author : Jackuna
# ----------------------------------------------------------------------------------------------------------------------------  #

import boto3
from prettytable import PrettyTable


#Color
R = "\033[0;31;40m" # RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m"       # Reset
CYAN = "\033[1;36m" # CYAN

def ebs_app_status():

    beanstalk = boto3.client('elasticbeanstalk')
    response = beanstalk.describe_environments()
    tabular_table = PrettyTable()
    tabular_table.field_names = ["Application Name","Health", "Inst1","Inst2","Inst3","Inst4"]
    tabular_table.align["Application Name"] = "l"
    #tabular_table.align["Environment Name"] = "l"
    for val in response['Environments']:

        newval = val["EnvironmentName"]
        new_response = beanstalk.describe_instances_health(EnvironmentName=newval, AttributeNames=['HealthStatus','Color'])
        instance_len = (len(new_response['InstanceHealthList']))

        if instance_len == 1:
            Instnace_1 = list(new_response['InstanceHealthList'][0].values())
            Instnace_2 = "NA"
            Instnace_3 = "NA"
            Instnace_4 = "NA"

        elif instance_len == 2:
            Instnace_1 = list(new_response['InstanceHealthList'][0].values())
            Instnace_2 = list(new_response['InstanceHealthList'][1].values())
            Instnace_3 = "NA"
            Instnace_4 = "NA"

        elif instance_len == 3:
            Instnace_1 = list(new_response['InstanceHealthList'][0].values())
            Instnace_2 = list(new_response['InstanceHealthList'][1].values())
            Instnace_3 = list(new_response['InstanceHealthList'][2].values())
            Instnace_4 = "NA"

        elif instance_len == 4:
            Instnace_1 = list(new_response['InstanceHealthList'][0].values())
            Instnace_2 = list(new_response['InstanceHealthList'][1].values())
            Instnace_3 = list(new_response['InstanceHealthList'][2].values())
            Instnace_4 = list(new_response['InstanceHealthList'][3].values())
            
        if val['Health'] == "Green":
            Health = G+'Green'+N
        else:
            Health = R+'Red'+N

        #tabular_table.add_row([Y+val['ApplicationName']+N,Health, val['HealthStatus'], Instnace_1,Instnace_2, Instnace_3, Instnace_4])
        tabular_table.add_row([CYAN+val['ApplicationName']+N, Health, Instnace_1,Instnace_2, Instnace_3, Instnace_4])

    print(tabular_table)

ebs_app_status()
