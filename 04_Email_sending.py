# https://www.youtube.com/watch?v=g_j6ILT-X0k

import smtplib
import ssl
from email.message import EmailMessage

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

import os
# os.getcwd()

# Define email sender and receiver
email_sender = 'python.robot.aws@gmail.com'
email_password = os.environ.get('EMAIL_PASSWORD')
email_receiver = 'python.robot.aws@gmail.com'


import pandas as pd
PriceMerge = pd.read_pickle("PriceMerge.pkl")


# Set the subject and body of the email
subject = 'Árösszehasonlító'

# =============================================================================
# body = """
# teszt 2
# """
# =============================================================================

html = """/
<html>
  <head>Árösszehasonlítás Masának</head>
  <br><br>
  <body>
    {0}
  </body>
</html>
""".format(PriceMerge.to_html())
body = MIMEText(html, 'html')
# em.attach(part1)


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())