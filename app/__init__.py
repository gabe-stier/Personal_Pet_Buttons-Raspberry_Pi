from app.common import config, messages
from serial import Serial

from app.managers.http import APIManager

def main():
    serial = Serial(config.com_port, config.rate)
    messages_list = messages.messages
    api: APIManager = APIManager(config.ip, config.api_port, config.exponent, config.salt)
    while True:
        line = serial.readline().decode()
        message_strings = [msg[0] for msg in messages_list]
        if line in message_strings:
            pass

    pass

def task(msg:str, uri:str, sound:str, api:APIManager):
    pass


if __name__ == "__main__":
    main()
