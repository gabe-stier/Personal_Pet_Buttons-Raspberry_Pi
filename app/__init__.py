from app.common import config, messages
from serial import Serial
from typing import Tuple, List, Dict, Union
from socket import socket, AF_INET, SOCK_STREAM

from app.managers.http import APIManager
from app.managers.sound import SoundManager
from datetime import datetime
import threading
ObjectHint = Tuple[List[str], Dict[str, Union[str, SoundManager]]]
restAPIActive = False


def main() -> None:
    serial = Serial(config.com_port, config.rate)
    api: APIManager = APIManager(config.ip, config.api_port, config.exponent, config.salt)
    test_port(config.ip, config.api_port)
    message_strings, msgs = init_objects(messages.messages)
    print(message_strings)
    while True:
        line = serial.readline().decode().replace("\n", "")
        if line in message_strings:
            task(line, msgs[line]["uri"], msgs[line]['sound'], api)            
            pass


def test_port(ip, port) -> None:
    global restAPIActive
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(ip, port)
        s.shutdown(2)
        restAPIActive = True
    except:
        restAPIActive = False


def task(msg: str, uri: str, sound: SoundManager, api: APIManager) -> bool:
    global restAPIActive
    sound_thread = threading.Thread(target=sound.play, args=())
    sound_thread.daemon = True
    sound_thread.start()

    message = {
        "message": msg,
        "time": datetime.now().strftime('%c')
    }
    print(message)
    if restAPIActive:
        if api.send_request(None, "post", uri):
            if api.send_request(None, "error", uri):
                return None

def init_objects(messages) -> ObjectHint:
    msgs = {}
    lines = []
    for message in messages:
        msgs[message[0]] = {"uri": message[1], "sound": SoundManager(message[2])}
        lines.append(message[0])

    return lines, msgs


if __name__ == "__main__":
    main()
