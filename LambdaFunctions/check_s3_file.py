
from boto3 import resource, client
import botocore
from datetime import datetime

SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:387634983977:mySNSTopic'

def lambda_handler(event, context):
    
    def trigger_email(email_subject, email_message):
        
        sns = client('sns')
        sns.publish(
        TopicArn = SNS_TOPIC_ARN,
        Subject = email_subject,
        Message = email_message
    )
        

    def initialize_objects_and_varibales():
        global SOURCE_BUCKET_NAME
        global FILE_NAME
        global FILE_NAME_WITH_DIRECTORY
        global dt
        
        dt = datetime.now()
        File_PREFIX_DATE = dt.strftime('%Y%m%d')
        FILE_PREFIX_DIRECTORY = event["bucket_sub_directory"]
        FILE_SUFFIX = event["file_suffix"]
        SOURCE_BUCKET_NAME = event["bucket_name"]
        FILE_TYPE = event['fileType']
        
        if event["bucket_sub_directory"] == 'NO':
            
            FILE_NAME_WITH_DIRECTORY = FILE_SUFFIX
        else:
            FILE_NAME_WITH_DIRECTORY = FILE_PREFIX_DIRECTORY+File_PREFIX_DATE+FILE_SUFFIX
            
        
        if FILE_TYPE == 'daily':
            FILE_NAME = File_PREFIX_DATE+FILE_SUFFIX
        else:
            FILE_NAME = FILE_SUFFIX
            

    def check_file_existance():
        
        s3 = resource('s3')
        try:
            print(FILE_NAME_WITH_DIRECTORY)
            s3.Object(SOURCE_BUCKET_NAME, FILE_NAME_WITH_DIRECTORY).load()
            print("[SUCCESS]", dt, "File Exists with name as",FILE_NAME)
            email_subject = "[INFO] Daily Report File found in report Folder"
            email_message = "Today's file name : {} \n Bucket Name : {} \n Lambda Function Name : {}".format(FILE_NAME, SOURCE_BUCKET_NAME,context.function_name )
            #trigger_email(email_subject,email_message)

        except botocore.exceptions.ClientError as errorStdOut:
            
            if errorStdOut.response['Error']['Code'] >= "401":
                print("[ERROR]", dt, "File does not exist. :", FILE_NAME)
                email_subject = "[ERROR]  Daily Report File not found in report Folder"
                email_message = "Expected file name : {} \n Bucket Name : {} \n Lambda Function Name : {}".format(FILE_NAME, SOURCE_BUCKET_NAME,context.function_name)
                #trigger_email(email_subject,email_message)

            else:
                print("[ERROR]", dt, "Something went wrong")
                email_subject = "[ERROR] Lambda Error"
                email_message = "Something went wrong, please check lambda logs.\n Expected file name : {} \n Bucket Name : {}\n Lambda Function Name : {}".format(FILE_NAME,SOURCE_BUCKET_NAME,context.function_name )
                #trigger_email(email_subject,email_message)
    
    initialize_objects_and_varibales()
    check_file_existance()
