import random
import smtplib
import datetime as dt

my_gmail = "digp1993@gmail.com"
password = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

        print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs="digpatel123@myyahoo.com",
                            msg=f"Subject:Motivation\n\n{quote}")

