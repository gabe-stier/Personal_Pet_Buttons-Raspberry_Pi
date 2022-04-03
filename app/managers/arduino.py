from abc import abstractmethod
import serial_asyncio
from app.serial_communications.reader import Reader
from app.serial_communications.writer import Writer
from typing import Union

from app.managers.sound import SoundManager
from app.managers.http import APIManager


class ArduinoManager:

    def __init__(self, name, loop, serial_manager: Union[Reader, Writer], message: str, sound_manager: SoundManager, api_manager: APIManager, rate: int = 19200) -> None:
        self.name = name
        self.loop = loop
        self.serial_manager = serial_manager
        self.rate = rate
        self.message = message
        self.sound_manager = sound_manager
        self.api_manager = api_manager

    def create_loop(self):
        if isinstance(self.serial_manager, Reader):
            self.serial_manager.set_message(self.message)
            self.serial_manager.set_task(self.task)
        self.serial = serial_asyncio.create_serial_connection(
            self.loop, self.serial_manager, self.name, buadrate=self.rate)

    def get_serial(self):
        return self.serial

    def task(self) -> bool:
        self.sound_manager.play()
        return True
