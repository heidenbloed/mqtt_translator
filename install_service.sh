echo "Stop service"
sudo systemctl stop mqtt_translator.service
source venv/bin/activate
pip install -r requirements.txt
echo "Copy service"
sudo cp mqtt_translator.service /etc/systemd/system/
echo "Enable service"
sudo systemctl enable mqtt_translator.service
echo "Start service"
sudo systemctl start mqtt_translator.service
echo "Status of service"
sudo systemctl status mqtt_translator.service