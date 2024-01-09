import smtplib
import os

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("python.robot.aws@gmail.com", os.environ.get('EMAIL_PASSWORD'))
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("python.robot.aws@gmail.com", "python.robot.aws@gmail.com", message)
# terminating the session
s.quit()


