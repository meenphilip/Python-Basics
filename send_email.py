import os
import smtplib
from email.message import EmailMessage
import imghdr


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "Check out Klopp our Manager"
msg['from'] = EMAIL_ADDRESS
msg['to'] = "ukilititus@gmail.com"
msg.set_content("Image attached here")

with open('klopp.jpeg', 'rb')as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image',
                   subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # subject = "Grab dinner this weekend?"
    # body = "How about dinner at 6pm this Saturday"
    # msg = f"Subject:{subject}\n\n{body}"
    # smtp.sendmail(EMAIL_ADDRESS, "mayenmeen@gmail.com", msg)
    smtp.send_message(msg)

print("send...")
