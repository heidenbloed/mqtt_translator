import paho.mqtt.client as mqtt
import json
import mqtt_secrets


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}.")
    client.subscribe("octoprint/progress/printing")


def on_message(client, userdata, msg):
    printing_progress_info = json.loads(msg.payload)
    progress = printing_progress_info["progress"]
    client.publish("lamps/tube/progress", str(progress))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(mqtt_secrets.USER, mqtt_secrets.PASSWORD)
    client.connect(mqtt_secrets.HOST, mqtt_secrets.PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
