#! venv/bin/python

import paho.mqtt.client as mqtt
import json
import mqtt_secrets

OCTOPRINT_PROGRESS_TOPIC = "octoprint/progress/printing"
TUBE_HEXCOLOR_TOPIC = "lamps/tube/hexcolor"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}.")
    client.subscribe(OCTOPRINT_PROGRESS_TOPIC)
    client.subscribe(TUBE_HEXCOLOR_TOPIC)


def on_message(client, userdata, msg):
    if msg.topic == OCTOPRINT_PROGRESS_TOPIC:
        printing_progress_info = json.loads(msg.payload)
        progress = printing_progress_info["progress"]
        client.publish("lamps/tube/progress", str(progress))
    elif msg.topic == TUBE_HEXCOLOR_TOPIC:
        hex_color = msg.payload.decode("utf-8").replace("#", "")
        try:
            red_val = int(hex_color[0:2], 16)
            green_val = int(hex_color[2:4], 16)
            blue_val = int(hex_color[4:6], 16)
            color_val = red_val * 256 * 256 + green_val * 256 + blue_val
            client.publish("lamps/tube/color", str(color_val))
        except ValueError:
            print(f'The message "{msg.payload}" is not a valid hex color.')
    else:
        print(f'Message from unknown topic "{msg.topic}".')


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(mqtt_secrets.USER, mqtt_secrets.PASSWORD)
    client.connect(mqtt_secrets.HOST, mqtt_secrets.PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()
