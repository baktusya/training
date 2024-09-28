def send_email(massage, recipient,*, sender = "university.help@gmail.com"):
    domen = ['.com', '.ru','.net']
    if any(word in recipient for word in domen) and '@' in recipient and any(word in sender for word in domen) and '@' in sender:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
            return
        elif sender != "university.help@gmail.com":
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <', sender, '> на адрес <', recipient, '>')
            return
        else:
            print('Письмо успешно отправлено с адреса <', sender, '> на адрес <', recipient, '>.')
    else:
        print('Невозможно отправить письмо с адреса <',sender,'> на адрес <', recipient, '>.')


send_email('Это сообщение для проверки связи', 'test@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.de')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')