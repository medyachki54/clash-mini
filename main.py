from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Unit:
    def __init__(self, x, team):
        self.x = x
        self.hp = 100
        self.team = team

class Game(Widget):
    player_hp = NumericProperty(100)
    enemy_hp = NumericProperty(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player_units = []
        self.enemy_units = []
        Clock.schedule_interval(self.update, 1/30)

    def spawn_player(self):
        self.player_units.append(Unit(100, "player"))

    def spawn_enemy(self):
        self.enemy_units.append(Unit(800, "enemy"))

    def update(self, dt):
        for u in self.player_units:
            u.x += 1
        for u in self.enemy_units:
            u.x -= 1

        for p in self.player_units:
            for e in self.enemy_units:
                if abs(p.x - e.x) < 30:
                    e.hp -= 1
                    p.hp -= 1

        self.player_units = [p for p in self.player_units if p.hp > 0]
        self.enemy_units = [e for e in self.enemy_units if e.hp > 0]

class ClashMiniApp(App):
    def build(self):
        return Game()

if __name__ == "__main__":
    ClashMiniApp().run()
