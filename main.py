import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# define a server that takes in the smtp server  for your provider and the port
server = smtplib.SMTP('smtp.gmail.com:587')

# this command starts the program
server.ehlo()

server.starttls()
# this takes in the password already saved in a text file
with open('password.txt', 'r') as f_obj:
    password = f_obj.read()

# pass in the gmail and password
server.login('walebakre10@gmail.com', password)

# create message
msg = MIMEMultipart()
# message headers
msg['From'] = 'Abdulroqeeb'
msg['To'] = 'roqeeb.raylizz@gmail.com'
msg['Subject'] = 'Testing my python skills'

# read from the message file
with open('message.txt', 'r') as fi_obj:
    message = fi_obj.read()

# attach the contents of the message file as plain text
msg.attach(MIMEText(message, 'plain'))

# adding an attachment, jpeg in this case
filename = 'starknet.png'

# we use 'rb' instead of 'r' cos we are reading in a picture not text
attachment = open(filename, 'rb')

# create a payload object, the 'octet-stream' is the stream to process the image
p = MIMEBase('application', 'octet-stream')

# set payload by reading content of attachment
p.set_payload(attachment.read())

# encode the image data
encoders.encode_base64(p)

# add header to p
p.add_header('Content-Disposition', f'attachment; filename={filename}')

# attach payload to message
msg.attach(p)

# this gets the whole mail as a string
text = msg.as_string()

# send the mail
server.sendmail('walebakre10@gmail.com', 'roqeeb.raylizz@gmail.com', text)






