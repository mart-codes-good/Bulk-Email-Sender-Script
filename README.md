# Multiple Email Writer Script

This Python script helps send emails with a similar structure to multiple recipients.
It reads from a recipients.csv file to get each recipient’s name, email, and context (the personalized part of the email that changes for each person).

You will need:
  An email address, and an Gmail app password.

The detailed instrcutions on how to use it is in the read me file in the source code :)

# Instructions:
1) Create a .env file with your email and app password

2) Update the Subject in the script to your desired email subject.

3) Draft your email body in the template provided in the script. Adjust spacing as needed.

4) Add recipients to recipients.csv in this format (no spaces after commas)

5) Run the script. Each recipient will receive a personalized email.

6) If an error occurs, only emails sent before the error will be delivered.

7) Check the console to see which emails were successfully sent. Happy sending!
