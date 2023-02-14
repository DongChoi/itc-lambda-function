from flask import Flask
import os
# from models import Capsule, Image, connect_db
import yagmail
import datetime
from flask_cors import CORS
import boto3
import requests
from dataclasses import dataclass
import psycopg2
from psycopg2.extras import RealDictCursor
import json

# app = Flask(__name__)
x = requests.post("http://127.0.0.1:5001/aws_lambda", json={"password":"aoiDJncKesoij342"})
print(x)
# CORS(app)

### S3 Keys
# app.config['ACCESS_KEY_ID'] = os.environ.get('ACCESS_KEY_ID')
# app.config['SECRET_ACCESS_KEY'] = os.environ.get('SECRET_ACCESS_KEY')
# app.config['AWS_BUCKET_NAME'] = os.environ.get('AWS_BUCKET_NAME')


# ### SQLA Configs
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = False
# if os.environ.get('RDS_HOSTNAME') is not None:
#     driver = 'postgresql+psycopg2://'
#     app.config['SQLALCHEMY_DATABASE_URI'] = driver \
#                                             + os.environ.get('RDS_USERNAME') + ':' + os.environ.get('RDS_PASSWORD') \
#                                             +'@' + os.environ.get('RDS_HOSTNAME')  +  ':' + os.environ.get('RDS_PORT') \
#                                             + '/' + os.environ.get('RDS_DB_NAME')
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = (
#         os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://"))

# connect_db(app)




# host = "image-time-capsule.cey3nevdhhzm.us-west-1.rds.amazonaws.com"
# username ="itc_admin"
# password = "FosjHenGwn2017"
# database ="itc_first"
# print("lets go")
# conn = psycopg2.connect(
#     user = username,
#     password = password,
#     host = host,
#     database = database,
#     port="5432"
# )


# print("got past the connection")
# def lambda_handler():
#     print("runnning lambda hyandler")
#     cur = conn.cursor(cursor_factory = RealDictCursor)
#     print("is this connecting")
#     cur.execute("select * from users")
#     results = cur.fetchall()
#     json_result = json.dumps(results)
#     print(json_result)
#     return json_result
    


### ID and Keys for Yagmail
# app.config['PROGRAM_EMAIL'] = os.environ.get('PROGRAM_EMAIL')
# app.config['PROGRAM_EMAIL_PASSWORD'] = os.environ.get('PROGRAM_EMAIL_PASSWORD')





# ### Connect to AWS S3 client
# client_s3 = boto3.client(
#     's3',
#     'us-west-1',
#     aws_access_key_id=app.config['ACCESS_KEY_ID'],
#     aws_secret_access_key=app.config['SECRET_ACCESS_KEY']
# )

# @app.route("/", methods=["GET"])
# def lambda_handle(event=None, context=None):
#     print("*********************heres the SQLALCHEMY",app.config['SQLALCHEMY_DATABASE_URI'])
#     # return_capsules()
#     lambda_handler()
#     print("ran return capsules")
#     return "lambda_handler Ran!"


# """check daily for capsule dates that match today's date"""
# def return_capsules():
#     print("*******************Running return capsules********************")
#     # Create a date with time instance
#     datetimeInstance = datetime.datetime.today()
#     # Extract the date only from date time instance
#     dateInstance = datetimeInstance.date()
#     print("******************got past datetime instance*********************")
#     capsules = Capsule.get_capsules_due_today(dateInstance)
#     print("******************got capsules due today*********************")
#     for capsule in capsules:
#         file_names_for_this_capsule = Image.get_file_names_from_capsule_id(capsule.id)
#         user_email = capsule.user.email
#         capsule_name = capsule.name
#         capsule_message = capsule.message
#         urls = [capsule_message]
#         for file_name in file_names_for_this_capsule:
#             urls.append(get_files_from_aws(file_name))
#         send_emails(capsule_name,urls, user_email)
#         print(f"capsule no.{capsule.id} belonging to {capsule.user_id} has been sent to user")


# def get_files_from_aws(file_name):
#     " Requests presigned url using key stored in PostgreSQL"
#     try:
#         url = client_s3.generate_presigned_url('get_object',
#                                 Params={
#                                     'Bucket': app.config['AWS_BUCKET_NAME'],
#                                     'Key': file_name,
#                                 },                                  
#                                 ExpiresIn=86400)
#     except Exception as e:
#         print(e)
#     return url



# def send_emails(capsule_name, urls_and_message, user_email="dongandrewchoi@gmail.com"): 
#     """ Sends urls via email to users"""
#     user = app.config['PROGRAM_EMAIL']
#     app_password = app.config['PROGRAM_EMAIL_PASSWORD'] # a token for gmail
#     to = user_email

#     subject = capsule_name
#     #content = [body text, attachments, attachments] with each item, there will be a line break
#     content = urls_and_message


#     with yagmail.SMTP(user, app_password) as yag:
#         yag.send(to, subject, content)
#     print("sent emails")