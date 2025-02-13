.PHONY: install
install:
	sudo cp flask_webhook.service /etc/systemd/system/flask_webhook.service
	sudo systemctl daemon-reload
	sudo systemctl enable flask_webhook.service
	sudo systemctl start flask_webhook.service

.PHONY: uninstall
uninstall:
	sudo systemctl stop flask_webhook.service
	sudo systemctl disable flask_webhook.service
	sudo rm /etc/systemd/system/flask_webhook.service
