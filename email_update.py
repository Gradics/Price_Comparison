import smtplib
import os

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("python.robot.aws@gmail.com", "iifn vier yytr fgnv")
# message to be sent
message = """\
Subject: Hi there

This message is sent from Python."""
# sending the mail
s.sendmail("python.robot.aws@gmail.com", "python.robot.aws@gmail.com", message)
# terminating the session
s.quit()



