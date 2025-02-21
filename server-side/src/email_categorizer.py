class EmailCategorizer:
    def __init__(self):
        self.categories = {
            "Estágio":["estágio", "innership"],
            "Classroom":["sala de aula"],
            "Iniciação Científica":[" ic ", "iniciação científica"]
        }
    
    def email_categorizer(self, email):
        subject = email.get('Subject').lower()
        sender = email.get('From').lower()

        for category, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in subject or keyword in sender:
                    return category
        return "Outro"
        