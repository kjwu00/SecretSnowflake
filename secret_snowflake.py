NAME_EMAIL = {
    'Katherine': 'kjwu00#stanford.edu',
    'Leon': 'leonbi@stanford.edu',
    'Michael': 'mchang6@stanford.edu',
    'Saw':'sawkyaw@stanford.edu'
}

def detect_cycle(matches):
    pass

def make_pairing(matches):
    matches.clear()

    people = set(NAME_EMAIL.keys())
    people_giving_left = set(NAME_EMAIL.keys())
    people_getting_left = set(NAME_EMAIL.keys())


    if (detect_cycle(matches)):
        make_pairing(matches)

def send_emails(matches):
    pass

def main():
    matches = {}
    make_pairing(matches)
    send_emails(matches)

if __name__ == '__main__':
    main()
