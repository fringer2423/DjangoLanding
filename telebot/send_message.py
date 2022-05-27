import requests
from .models import TeleSettings


def send_telegram(name, phone):
    if TeleSettings.objects.get(pk=2):
        settings = TeleSettings.objects.get(pk=2)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        text = f'{text} от {name}. Номер телефона: {phone}'
        api = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=-{chat_id}&text={text}'
        try:
            req = requests.post(api, data={
                'chat_id': chat_id,
                'text': text
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print("Ошибка отправки сообщения telegram")
            elif req.status_code == 500:
                print("Ошибка 500")
            else:
                print("Сообщение отправлено")
