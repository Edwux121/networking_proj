import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)

#Starts the server
server.ehlo()

#Open the password of the encrypted txt file
with open("password.txt", "r") as file:
    password = file.read()

#Login to the server
server.login("#Email", password)

#Creating a message
msg = MIMEMultipart()
msg["From"] = "Edvinas"
msg["To"] = "#Email goes here"
msg["Subject"] = "Testing"

with open("message.txt", "r") as file:
    message = file.read()

msg.attach(MIMEText(message, "plain"))

#Preparing the Image
filename = "picture.jpg"

attachment = open(filename, "rb")

#Creating a payload
payload = MIMEBase("application", "octet-stream")
payload.set_payload(attachment.read())

encoders.encode_base64(payload)
payload.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(payload)

text = msg.as_string()
server.sendmail("#Email", "#Email", text)