from playsound import playsound
from os import path
from sys import modules


class SoundManager:

    dir = path.dirname(__file__)

    def __init__(self, sound_file):
        if "__main__" in modules and hasattr(modules["__main__"],"__file__"):
            self.dir = path.join(path.dirname(modules["__main__"].__file__),"sounds")
        self.sound_file = path.join(self.dir, sound_file)

    def play(self):
        try:
            playsound(self.sound_file)  
        except:
            pass

    def change_sound(self, sound_file):
        self.sound_file = path.join(self.dir, sound_file)