from email_fetcher import EmailFetcher
from email_categorizer import EmailCategorizer
from utils import clean_email

IMAP_SSL_HOST = 'imap.gmail.com'
IMAP_SSL_PORT = 993

def main():
    username = input("Digite seu email: ")
    password = input("Digite sua senha: ")
    limit = int(input("Quantos emails?: "))

    fetcher = EmailFetcher(IMAP_SSL_HOST, IMAP_SSL_PORT, username, password)
    fetcher.login()
    emails = fetcher.fetch_emails(limit)
    fetcher.logout()

    categorizer = EmailCategorizer()


    for email in emails:
        message = clean_email(email)
        category = categorizer.email_categorizer(message)
        
        print(f"FROM: {message.get('From')}\n")
        print(f"SUBJECT: {message.get('Subject')}\n")
        print(f"CATEGORY: {category}\n")
        print(f"BODY:\n{message.get('Body')}")
        print(f"{"#" * 50}\n")

if __name__ == "__main__":
    main()
