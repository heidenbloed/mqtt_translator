import paho.mqtt.client as mqtt
import mqtt_secrets


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}.")
    client.subscribe("#")


def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload}")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(mqtt_secrets.USER, mqtt_secrets.PASSWORD)
    client.connect(mqtt_secrets.HOST, mqtt_secrets.PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
