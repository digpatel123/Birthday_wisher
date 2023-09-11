import csv
import datetime
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_birthday_email():
    today = datetime.datetime.now()
    with open('birthdays.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if int(row[3]) == today.month and int(row[4]) == today.day:
                send_email(row[1], row[0])


def send_email(to_email, name):
    random_choice = random.choice([1, 2, 3])
    filename = f'letter_templates/letter_{random_choice}.txt'

    with open(filename, 'r') as template_file:
        template = template_file.read()
    template = template.replace('[NAME]', name)
    msg = MIMEMultipart()
    msg['From'] = 'digp1993@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = 'Happy Birthday!'
    msg.attach(MIMEText(template, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'password_here')
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    send_birthday_email()