class GameStats():
    """Track statistics for Zenthos Elite."""
    
    def __init__(self, ai_settings):
        """Initialize stats."""
        self.ai_settings = ai_settings
        self.reset_stats()
    
        # Start game in inactive state
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_lives

