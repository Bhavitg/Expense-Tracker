import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(you="ishankiller10@gmail.com", amount=2500):
    # me is my email address
    # you is recipient's email address
    
    me = "expensetracker269@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "EXPENSE TRACKER - Daily Limit Exceeded"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    html = """\
    <html>
      <head></head>
      <body>
      <H1>Expense Tracker</H1>
      <h2>Daily Limit Exceeded!</H2>
        <p>Hi!<br>
           Your daily limit is exceeded <br>
           You spent """+ str(amount)+ """ today.
        </p>
      </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()
    mail.login('bhavitg12@gmail.com', 'bh@vit!@#')
    mail.sendmail(me, you, msg.as_string())
    print("Mail sent")
    mail.quit()
