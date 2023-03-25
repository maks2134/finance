
import requests
from bs4 import BeautifulSoup

# Укажите URL для получения баланса
BELARUSBANK_BALANCE_URL = "https://belarusbank.by/ru/private/mybank/finances/balance"

# Укажите свои учетные данные для входа в интернет-банк Беларусьбанка
BELARUSBANK_USERNAME = "your_username_here"
BELARUSBANK_PASSWORD = "your_password_here"

# Формируем параметры запроса 
params = {
    "login": BELARUSBANK_USERNAME,
    "password": BELARUSBANK_PASSWORD
}

# Выполняем POST запрос для входа в интернет-банк Беларусьбанка
session = requests.session()
response = session.post(BELARUSBANK_BALANCE_URL, data=params)

# Про
if "Мверяем, что вход выполнен успешноои счета и карты" in response.text:
    # Используем BeautifulSoup для парсинга HTML страницы и получения баланса
    soup = BeautifulSoup(response.text, "html.parser")
    balance = soup.find("span", {"class": "balance__num js-balance"}).text
    # Выводим баланс на экран
    print("Your balance is:", balance)
else:
    # Если произошла ошибка, выводим ее на экран
    print("Error occurred while fetching Belarusbank balance.")


import paho.mqtt.client as mqtt

# ...

# Определите адрес брокера MQTT и топик для передачи данных
MQTT_BROKER = "konik"
MQTT_TOPIC = "test_finance"

# Создайте клиент MQTT
mqtt_client = mqtt.Client()

# Подключитесь к брокеру MQTT
mqtt_client.connect(MQTT_BROKER)

# Опубликуйте значение переменной balance в топик MQTT
mqtt_client.publish(MQTT_TOPIC, balance)

# Отключитесь от брокера MQTT
mqtt_client.disconnect()
