import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Settings for connecting to the mail server
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_email@gmail.com"
sender_password = "your_password"

# Recipient and subject of the email
recipient_email = "recipient_email@example.com"
subject = "Email Subject"
body = "Email body text"

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

# Attach the email body to the message
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error while sending the email: {e}")
finally:
    server.quit()
