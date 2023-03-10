import paho.mqtt.client as mqtt
import json
import datetime

HOST = "192.168.2.24"
PORT = 1883
KEEPALIVE = 1500

SUB_TOPICS = {
    '/devices/wb-msw-v3_21/controls/Current Motion': 'Motion',
    '/devices/wb-ms_11/controls/Air Quality (VOC)': 'Air Quality',
    '/devices/wb-msw-v3_21/controls/Humidity': 'Humidity',
    '/devices/wb-ms_11/controls/Temperature': 'Temperature',
}

JSON_DICT = { value: 0 for value in SUB_TOPICS.values() }


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    for topic in SUB_TOPICS.keys():
        client.subscribe(topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic

    param_name = SUB_TOPICS[topic]
    JSON_DICT[param_name] = payload
    JSON_DICT['Time'] = str(datetime.datetime.now())
    JSON_DICT['Number'] = 24
#    print(topic + " " + payload)

    with open('data.json', 'w') as file:
        file.write(json.dumps(JSON_DICT))

    with open('data.json', 'r', encoding='utf-8') as file:
        text = json.load(file)
        for d in text.keys():
            print(d, ':', text.get(d))
        print()

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, KEEPALIVE)

    client.loop_forever()


if __name__ == "__main__":
    main()
