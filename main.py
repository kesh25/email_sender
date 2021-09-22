import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Kinyua Nyaga'
email['to'] = 'kinyua.nyaga254@gmail.com'
email['subject'] = 'Greetings...!!!'

email.set_content('Hello there gread sir..!!\nRegards, Kinyua Nyaga')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dixxon.kesh@gmail.com', '#Sechaktiyu765_$d')
    smtp.send_message(email)
    print('all good..!!')