import sys
class Settings():
    '''Class stores all settings for the game'''

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 20, 60, 60
        self.bullets_on_screen = 5
