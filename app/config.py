
from configparser import ConfigParser

class Config():
    def __init__(self) -> None: 
        self.config = ConfigParser()
        self.config.read("config/config.ini")
        print(self.config)
        self.defaults = self.config["defaults"]
        self.com_port = self.defaults['interface']
        self.ip = self.defaults['ip']
        self.rate = self.defaults['baudrate']
        self.timeout = self.defaults['timeout']
        self.exponent = self.defaults['exponent']
        self.salt = self.defaults['salt']
        self.api_port = self.defaults['api_port']
        print(self.__dict__.__str__())

class Messages():
    messages:list = []
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read("config/messages.ini")
        sections = self.config.sections()
        for section in sections:
            data = self.config[section]
            self.messages.append((data['message'], data['uri'], data['sound']))