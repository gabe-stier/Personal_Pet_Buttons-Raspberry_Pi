
from configparser import ConfigParser


class Config():
    def __init__(self) -> None:
        self.config = ConfigParser().read("config.ini")
        self.defaults = self.config["defaults"]
        self.com_port = self.defaults['interface']
        self.ip = self.defaults['ip']
        self.rate = self.defaults['baudrate']
        self.timeout = self.defaults['timeout']
        self.exponent = self.defaults['exponent']
        self.salt = self.defaults['salt']
        self.api_port = self.defaults['api_port']

class Messages():
    messages:list = []
    def __init__(self) -> None:
        message_conf = ConfigParser().read("messages.ini")
        sections = message_conf.sections()
        for section in sections:
            data = message_conf[section]
            self.messages.append((data['message'], data['uri'], data['sound']))