#!/usr/bin/python3
# --------------------------------------------------------------------------------------------------------------------------------  #
# aws_dynamic_host_inventory.py : A python script meant to list and search instances based on AWS regions.
#                                 Script can be made universal by adding respective credentails,regions and environment name
#
#
#
# Dependencies ( One time Installation )
# --------------------------------------
# 1. Python 3.6+
# 2. Additional python libraries.
#   Install additional mandatory python packages using command.
#   --> "pip3 install  boto3 "
#   --> "pip3 install prettytable"
#
# How to
# --------
# 1. Specify your aws_access_key_id and aws_secret_access_key for every profile
#    Example : cat .aws/credentials
#
#     [prod]
#     aws_access_key_id = ANYPASSWORDOFMINE
#     aws_secret_access_key = KUCHBHISECRETKEYOFMINE
#
#     [non_prod]
#     aws_access_key_id = ANOTHERPA55WORD!23HKDKD
#     aws_secret_access_key = 7938303NDJDNDEJDNDJ9@@@0CNCKDDMD
#
# 2. Now edit one more line within a script  "user_env_input =  input('Your ENV (prod1/prod2/qa1/stage1) please :: ')"
#    Chnage it as per your need, like l"user_env_input =  input('Your ENV name (prod / non_prod please :: ')"
#
# 3. run the python script as "aws_dynamic_host_inventory.py".
#    script will prompt for environmnet name (type the one that you mentioned within the credentials file and search string.)
#
# 4. Argumnet mode is also supported as python3 aws_dynamic_host_inventory.py < non_prod >  < myhostname >
#
# 5. To enlist all the host within the specific region's account
#    Run -->  python3 aws_dynamic_host_inventory.py
#             Provide your environment name and then leave blank when asked for search string
#
#
# DOC     : 23-Sep-2019
# Updates : XX-XXX-2019
#         : XX-XXX-2019
#
# Author : JacKuna
# --------------------------------------------------------------------------------------------------------------------------------- #

import boto3
from prettytable import PrettyTable
import sys


#Color
R = "\033[0;31;40m" # RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m"       # Reset
CYAN = "\033[1;36m" # CYAN

def check_argument():

    global user_env_input
    global search_string
    global user_input

    if (len(sys.argv)) > 2:

        user_env_input = str(sys.argv[1])
        user_input = str(sys.argv[2])
        search_string = ''

    else:

        print()
        user_env_input =  input('Your ENV (prod1/prod2/qa1/stage1) pleas :: ')
        user_input =  input('Your Search String please :: ')
        search_string = ''
        
def grab_bs_instnaces_info():

    global user_env_input
    global search_string
    global user_input

    session = boto3.session.Session(profile_name=user_env_input)

    ec2 = session.client('ec2')
    response = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['*'+ user_input + search_string + '*']}])

    tabular_table = PrettyTable()
    tabular_table.field_names = ["BeanStalk App Name","Instance","IP Address"]
    tabular_table.align["BeanStalk App Name"] = "l"
    tabular_table.align["IP Address"] = "l"

    for val in response['Reservations']:

        for newval in val['Instances']:
            for new_val in newval['Tags']:

                if new_val['Key'] == 'Name':
                    tabular_table.add_row([CYAN+new_val['Value']+N, newval['InstanceId'], Y+newval['PrivateIpAddress']+N])
                else:

                    pass
    print()
    print(tabular_table)

try:
    check_argument()
    grab_bs_instnaces_info()
except:
    print(" Entered Environment", R+user_env_input.upper()+N , "can't be located, check again ! " )


