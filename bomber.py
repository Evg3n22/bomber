from twilio.rest import Client
import time

# Твої дані з Twilio
account_sid = 'AC855adf7d853a4756b8dffdfd2c55eac3'  # Заміни на свій SID
auth_token = '0bff30dc0f2e4d6393e6ce72fe3ad0b6'    # Заміни на свій токен
twilio_number = '+13802338796'  # Номер, виданий Twilio
your_number =   '+380672610272'   # Твій український номер у форматі +380XXXXXXXXX

# Ініціалізація клієнта Twilio
client = Client(account_sid, auth_token)

# Кількість дзвінків
call_count = 2

for i in range(call_count):
    # Створення дзвінка
    call = client.calls.create(
        to=your_number,              # Твій номер
        from_=twilio_number,         # Номер Twilio
        url='http://demo.twilio.com/docs/voice.xml'  # URL із голосовим повідомленням
    )
    print(f"Дзвінок {i+1} запущено: {call.sid}")
    time.sleep(100)  # Пауза між дзвінками (10 секунд)

print("Тест завершено!")
