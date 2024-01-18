import random as r
import json
import message

number = ''
for i in range(6):
    number += str(r.randint(0, 9))
random_number = number

def send_message():
    data = {
        'messages': [
            {
                'to': '01034320132',
                'from': '01034320132',
                'text': f'인증번호 6자리: {random_number}'
            },
            # ...
            # 1만건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))