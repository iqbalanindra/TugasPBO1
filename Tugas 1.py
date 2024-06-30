class AudioPlayer:
    def __init__(self):
        self.volume_level = 5  # Set default volume level

    def volume_up(self):
        if self.volume_level < 10:
            self.volume_level += 1
            print(f"Volume increased to level {self.volume_level}")
        else:
            print("Maximum volume reached.")

    def volume_down(self):
        if self.volume_level > 0:
            self.volume_level -= 1
            print(f"Volume decreased to level {self.volume_level}")
        else:
            print("Minimum volume reached.")

# Menguji metode volume_up dan volume_down
player = AudioPlayer()
player.volume_up()
player.volume_up()
player.volume_down()
player.volume_down()
player.volume_down()  # Ini akan mencetak "Minimum volume reached."