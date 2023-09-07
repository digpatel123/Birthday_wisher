import smtplib

my_gmail = "digpatel123@myyahoo.com"
password = ""
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_gmail, password=password)
    connection.sendmail(from_addr=my_gmail, to_addrs="digp1993@gmail.com", msg="Subject:Hello\n\nThis is the email body.")
