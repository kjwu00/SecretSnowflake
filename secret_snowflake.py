import random
import sys
import smtplib

PORT = 587

def read_file(in_file):
    name_email = {}
    with open(in_file, 'r') as f:
        for line in f:
            parts = line.split(",")
            if len(parts) != 2:
                raise Exception ("make sure every line in the input file is: name, email")
            name_email[parts[0].strip()] = parts[1].strip()
    return name_email

def make_pairing(name_email, matches):
    people = list(name_email.keys())
    if len(people) < 2:
        raise Exception ("make sure there are more than two people")

    random.shuffle(people)
    for i in range(len(people)):
        matches[people[i]] = people[(i+1)%len(people)]

def send_emails(name_email, matches):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
    except:
        print("Was unable to setup server for emaiil.")
    
    

def main():
    if len(sys.argv) != 2:
        raise Exception("usage: python3 secret_snowflake.py <in_file>")

    name_email = read_file(sys.argv[1])
    matches = {}
    make_pairing(name_email, matches)
    send_emails(name_email, matches)

if __name__ == '__main__':
    main()
