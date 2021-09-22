import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

def send_email(*args):
    email.set_content(html.substitute(name=args.name))

    email['from'] = args.from_who
    email['to'] = args.to
    email['subject'] = args.subject
    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(args.mail, args.pswd)
            smtp.send_message(email)
            print('Email sent..!!')
    except smtplib.SMTPAuthenticationError:
        print('Ooops..authentication error')
    else:
        print('Oooh no, something went wrong')
