import random
import sys
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def read_participants_file(in_file):
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

def read_message_file(in_file):
    if len(open(in_file).readlines(  )) < 2:
        raise Exception ("please include a subject in the first line and the body text in the subsequent lines")

    body_lines = []
    with open(in_file, 'r') as f:
        subject = f.readline()
        for line in f:
            body_lines.append(line)
    body = ''.join(body_lines)
    return subject, body        

def make_pairing(name_email, matches):
    people = list(name_email.keys())
    if len(people) <= 2:
        raise Exception ("make sure there are more than two people")

    random.shuffle(people)
    for i in range(len(people)):
        matches[people[i]] = people[(i+1)%len(people)]


def send_emails(name_email, matches, subject, body):
    try:
        # Connect to email server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(GMAIL_USER, GMAIL_PASSWORD)

        # Send emails
        for giver, receiver in matches.items():
            body = body.replace("<giver>", giver)
            body = body.replace("<receiver>", receiver)
            sent_from = GMAIL_USER
            to = name_email[giver]
            email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sent_from, to, subject, body)

            server.sendmail(sent_from, to, email_text)
        server.close()
                    
    except:
        print("Was unable to send emails.")


def main():
    if len(sys.argv) != 3:
        raise Exception("usage: python3 secret_snowflake.py <in_file>")

    name_email = read_participants_file(sys.argv[1])
    subject, body = read_message_file(sys.argv[2])
    matches = {}
    make_pairing(name_email, matches)
    send_emails(name_email, matches, subject, body)


if __name__ == '__main__':
    main()
