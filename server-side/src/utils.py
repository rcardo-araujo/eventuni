from email.header import decode_header

def clean_email(email):
    sender, _ = decode_header(email.get('From'))[0]
    if isinstance(sender, bytes):
        sender = sender.decode('utf-8')
    
    sender = sender.split('<')[0].strip()

    subject, _ = decode_header(email.get('Subject'))[0]
    if isinstance(subject, bytes):
        subject = subject.decode('utf-8')

    body = ""
    for part in email.walk():
        if part.get_content_type() == "text/plain":
            body += part.get_payload(decode=True).decode('utf-8')
    
    cleaned_email = {
        "From":sender,
        "Subject":subject,
        "Body":body
    }

    return cleaned_email
