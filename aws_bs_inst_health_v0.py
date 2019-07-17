# ----------------------------------------------------------------------------------------------------------------------------  #
# aws_bs_inst_health_v0.py : AWS Beanstalk Health Status, An xample for the implemenantion of python's boto3 library with
# other python packages. 
# Script will show the overall health of beanstalk application with it's respective instances health too.
# 
# So what's new ? : The look and feel of all the details in a tabular format. 
# 
# As comapred to the same first script, no assumption is required over here for max-min instances, it will poppulate by it's own
# 
# Author : Jackuna
# ----------------------------------------------------------------------------------------------------------------------------  #

import boto3
import json
from prettytable import PrettyTable


#Color
R = "\033[0;31;40m" # RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m"       # Reset
CYAN = "\033[1;36m" # CYAN

# Global Varibales
instance_len_list = []
max_instance_len = ""
tabular_fields = ["Application Name","Health","Status"]

def ebs_app_status():


    def grab_instance_length():

        global instance_len_list
        global max_instance_len

        beanstalk = boto3.client('elasticbeanstalk')
        response = beanstalk.describe_environments()
        for val in response['Environments']:

            newval = val["EnvironmentName"]
            new_response = beanstalk.describe_instances_health(EnvironmentName=newval, AttributeNames=['HealthStatus','Color'])
            instance_len_list.append((len(new_response['InstanceHealthList'])))

        return max(instance_len_list)


    def create_preetyTable_feilds():

        global tabular_fields
        global max_instance_len

        max_instance_len = grab_instance_length()

        for new_range in range(0, max_instance_len):
            tabular_fields.append("Inst"+str(new_range))
        #print(tabular_fields)


    def create_preetyTable():

        global tabular_fields
        global max_instance_lencreate_preetyTable_feilds()

        beanstalk = boto3.client('elasticbeanstalk')
        response = beanstalk.describe_environments()
        tabular_table = PrettyTable()
        tabular_table.field_names = tabular_fields
        tabular_table.align["Application Name"] = "l"


        for val in response['Environments']:
            rows = []
            rows.append(str(CYAN+val['ApplicationName']+N))
            newval = val["EnvironmentName"]
            new_response = beanstalk.describe_instances_health(EnvironmentName=newval, AttributeNames=['HealthStatus','Color'])
            new_range = len(new_response['InstanceHealthList'])

            if val['HealthStatus'] == "Info":
                HealthStatus = Y+'Info'+N

            elif val['HealthStatus'] == "Ok":
                HealthStatus = G+'Ok'+N

            if val['Health'] == "Green":
                 Health = G+'Green'+N

            elif val['Health'] == "Info":
                 Health = Y+'Info'+N

            else:
                Health = R+'Red'+N

            rows.append(HealthStatus)
            rows.append(Health)

            for ll in range(0, new_range):

                Inst = list(new_response['InstanceHealthList'][ll].values())
                rows.append(str(Inst))
            length_rows = max_instance_len

            if length_rows > new_range:
                rng = length_rows - new_range
                for x_val in range(0, rng):
                    rows.append("NA")

            tabular_table.add_row(rows)

        print(tabular_table)

    create_preetyTable()
        
        
