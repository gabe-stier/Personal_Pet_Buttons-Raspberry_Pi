from playsound import playsound

class SoundManager:
    def __init__(self, sound_file):
        self.sound_file = sound_file

    def play(self):
        playsound(self.sound_file)  

    def change_sound(self, sound_file):
        self.sound_file = sound_file