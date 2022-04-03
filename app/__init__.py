from app.common import config, messages
from serial import Serial

def main():
    serial = Serial(config.com_port, config.rate)
    messages_list = messages.messages
    while True:
        line = serial.readline().decode()
        message_strings = [msg[0] for msg in messages_list]

    pass

def task(msg:str, uri:str, sound:str):
    pass


if __name__ == "__main__":
    main()
