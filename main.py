import paho.mqtt.client as mqtt
import json

HOST = "26.197.145.77"
PORT = 1883
KEEPALIVE = 1500

SUB_TOPICS = {
    '/iarduino_I2C_DSL/controls/Lux': 'Lux',
    '/iarduino_I2C_DSL/controls/Pulsation': 'Pulsation',
    '/iarduino_I2C_DSL/controls/Proximity': 'Proximity',
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
