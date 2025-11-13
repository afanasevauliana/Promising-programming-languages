class Mail:
    def __init__(self, name, cnt, post_office):
        self.recipient_name = name
        self.mail_count = cnt
        self.post_office = post_office
    
    def destination(self, target_office):
        return str(self.post_office).lower() == str(target_office).lower()


if __name__ == "__main__":
    mail1 = Mail("Роман Турта", 3, 15)
    mail2 = Mail("Арина Круглова", 1, "Центральное")
    mail3 = Mail("Петр Гришин", 5, "15")
    
    print(f"Проверка {mail1.recipient_name} в отделении 15: {mail1.destination(15)}")
    print(f"Проверка {mail2.recipient_name} в отделении 'центральное': {mail2.destination('центральное')}")
    print(f"Проверка {mail3.recipient_name} в отделении 20: {mail3.destination(20)}")