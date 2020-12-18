import random
import sys
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def read_file(in_file):
    name_email = {}
    with open(in_file, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                pass

            parts = line.split(",")
            if len(parts) != 2:
                raise Exception ("make sure every line in the input file is: name, email")
            name_email[parts[0].strip()] = parts[1].strip()

    return name_email


def make_pairing(name_email, matches):
    people = list(name_email.keys())
    if len(people) <= 2:
        raise Exception ("make sure there are more than two people")

    random.shuffle(people)
    for i in range(len(people)):
        matches[people[i]] = people[(i+1)%len(people)]


def send_emails(name_email, matches):
    try:
        # Connect to email server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_PASSWORD)

        # Send emails
        for giver, receiver in matches.items():
            sent_from = GMAIL_USER
            to = name_email[giver]
            subject = "Secret Snowflake"
            body = "Hi " + giver + "! Get a gift for " + receiver +"."

            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, to, subject, body)

            server.sendmail(sent_from, to, email_text)

        server.close()
                    
    except:
        print("Was unable to send emails.")


def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python3 secret_snowflake.py <in_file>")

    name_email = read_file(sys.argv[1])
    matches = {}
    make_pairing(name_email, matches)
    send_emails(name_email, matches)


if __name__ == '__main__':
    main()
