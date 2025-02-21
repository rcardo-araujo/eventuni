import imaplib
import email

class EmailFetcher:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.mail = imaplib.IMAP4_SSL(self.host)
    
    def login(self):
        self.mail.login(self.username, self.password)
        self.mail.select('INBOX')

    def fetch_emails(self, limit):
        _, msgnums = self.mail.search(None, "ALL")

        msgnums = msgnums[0].split()[::-1]

        messages = []
        for msgnum in msgnums[:limit]:
            _, data = self.mail.fetch(msgnum, "(RFC822)")

            message = email.message_from_bytes(data[0][1])
            messages.append(message)
        
        return messages
    
    def logout(self):
        self.mail.logout()
