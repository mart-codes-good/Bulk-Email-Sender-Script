# @author: Martin Tejada
# @version: 1.0
# @since: August 13, 2025

import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import csv

load_dotenv()

# Load protected information
my_email = os.getenv("My_Email")
password = os.getenv("App_Password")

# TODO add scanning from csv file

recepients = {}

with open("recipients.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        recepients[int(row["id"])] = { # wrap first coloumn for easy iteration
            "name": row["name"],
            "email": row["email"],
            "context": row["context"]
        }

print(recepients)

# Method to send emails
def send_emails(Subject, To, From, Body):
    # Creating EmailMessage object 
    mail = EmailMessage()
    mail['Subject'] = Subject
    mail['To'] = To
    mail['From'] = From
    mail.set_content(Body)

    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(my_email, password)
        smtp.send_message(mail)
        print("------------------------------")
        print(f"{To}'s email sent succesfully!")

# Counter to iterate through the dictionary and it's respective personalized portion
counter = 0

# Sending all emails
while(counter < len(recepients)):
    
    recepient_info = recepients.get(counter)

    send_emails(Subject="Enter your email subject here!",
                To = recepient_info["email"].strip(),
                From = my_email,
                Body = f'''Good Afternoon {recepient_info["name"]}, 

Here are your tasks: 
{recepient_info["context"]}
                                       
Let me know if you have any questions!''')

    # Move to next recepient content in list
    counter += 1


#To Do:
# Changing the name [DONE]
# Changing some context [DONE]
# Debug, test until program has correct output [DONE]
# Create a method and make it easier to digest [DONE]
# Make it possible to import names and emails and context from txt file [DONE]
# possible to import message from txt file [DONE]
# Complete read me Instructions [DONE]