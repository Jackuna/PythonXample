import requests
import json
import base64
from requests.auth import HTTPBasicAuth

# Inorder to encrypt/decrypt your credentials using base64 module as below.
# To encode --> base64.b64encode(bytes("random", "utf-8"))
# To decode --> base64.b64decode("cmFuZG9t").decode("utf-8")

class JiraHandler:
      
    def __init__(self, username):
        print('Loading Instnace variables...')
        self.username = username
        self.securestring = base64.b64decode("replaceItwithYourCredential").decode("utf-8")
        self.url = "https://jira.yourownjiradomain.com/rest/api/2/issue/"

    def get_jira_details(self,jira_ticket):

        try :
            
            auth = HTTPBasicAuth(self.username, self.securestring)
            get_details_url = self.url + jira_ticket

            headers = {
               "Accept": "application/json"
            }
            
            print("retrieveing", jira_ticket, "details...")
            response = requests.request(
               "GET",
               get_details_url,
               headers=headers,
               auth=auth
            )
            print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
            
        except Exception as e:
            return e



    def create_jira_cr_ticket(self, filename):
        get_details_url = self.url

        auth = HTTPBasicAuth(self.username, self.securestring)

        headers = {
           "Accept": "application/json",
           "Content-Type": "application/json"
        }
        try:
            with open(filename, "r") as re_read_file:
                payload = re_read_file.read()
                print("Creating new JIRA...")
                response = requests.request(
                   "POST",
                   get_details_url,
                   data=payload,
                   headers=headers,
                   auth=auth
                )
                print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        except Exception as filenotfound:
            print("Can't load file..", filenotfound)
