from abc import abstractmethod
import serial_asyncio
from asyncio import AbstractEventLoop
from app.serial.reader import Reader
from app.serial.writer import Writer
from typing import Union

class ArduinoManager:

    def __init__(self, name, loop, serial_manager:Union[Reader, Writer], rate:int=19200) -> None:
        self.name = name
        self.loop = loop
        self.serial_manager = serial_manager
        self.rate = rate
        
    def create_loop(self):
        self.serial = serial_asyncio.create_serial_connection(self.loop, self.serial_manager, self.name, buadrate=self.rate)

    def get_serial(self):
        return self.serial

    @abstractmethod
    def task(self):
        pass

    