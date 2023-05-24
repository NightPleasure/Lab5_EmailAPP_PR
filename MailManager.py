import smtplib
import imaplib
import email

# Setări pentru conexiunea SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'barbaian.victor@gmail.com'
SMTP_PASSWORD = 'PAROLA'

# Setări pentru conexiunea IMAP
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993


def send_email(subject, body, to_addr, reply_to=None):
    # Creează un obiect de mesaj
    msg = email.message.EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_addr

    # Conectare la serverul SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)


def receive_emails():
    # Conectare la serverul IMAP
    with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.select()

        # Căutare și obținere mesaje
        _, message_numbers = server.search(None, 'ALL')
        for num in message_numbers[0].split():
            _, data = server.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Procesare mesaj
            print('Subiect:', msg['Subject'])
            print('De la:', msg['From'])
            print('La:', msg['To'])
            print('Mesaj:', msg.get_payload())


# Exemplu de utilizare
send_email('Subiect', 'test mesaj', 'jade.santrope@gmail.com', reply_to='barbaian.victor@gmail.com')
receive_emails()