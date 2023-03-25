#include <Arduino.h>
#include <Liquidcrystal.h>
#include <Pubsubclient.h>
#include <Ethernet.h>
// определите МАС-адрес и I-адрес Ethernet-шита и адрес и порт брокера мотт и топик для передачи данных
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
const char* MQTT_BROKER = "konik";
const int MQTT_PORT = 5031;
const char* MQTT_TOPIC = "test finance";

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
// Создайте объект Ethernetclient для подключения к брокеру мотт
EthernetClient ethernet_client;
float balance;
// Создайте объект PubSubclient для работы с протоколом мотт
PubSubClient mqtt_client (ethernet_client);
// Функция, которая вызывается, когда получено новое сообщение из топика МОТт
void matt_callback(char* topic, byte* payload, unsigned int length){
// Получите значение переменной balance из сообщения
  balance = atof ((char*)payload);
// Выполните необходимые действия с полученным значением переменной balance
}

void setup() {
 Ethernet.begin(mac);

lcd.begin(16, 2);
// print a message to the LCD.
lcd.print (balance);
}

void loop() {
// Подключитесь к брокеру мотт, если необходимо.
if (!mqtt_client.connected()) {
 mqtt_client.connect ("Arduinoclient");
 mqtt_client.subscribe(MQTT_TOPIC);
}

lcd.setCursor(0, 1);
// обрабатывайте новые сообщения из топика МОтт
mqtt_client.loop();
}
