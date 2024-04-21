class Hobby:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("This is a hobby.")


class Music(Hobby):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def describe(self):
        print(f"This is a type of music: {self.genre}.")


class Sport:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("This is a sport.")


class Football(Sport):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def describe(self):
        print(f"This is a football team: {self.team}.")


class Tool:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("This is a tool.")


class Hammer(Tool):
    def __init__(self, name, material):
        super().__init__(name)
        self.material = material

    def describe(self):
        print(f"This is a {self.material} hammer.")


class Instrument:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("This is an instrument.")


class Guitar(Instrument):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def describe(self):
        print(f"This is a {self.brand} guitar.")


class Sound:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print("This is a sound.")


hobby = Hobby("Painting")
hobby.describe()

music = Music("Listening", "Rock")
music.describe()

sport = Sport("Running")
sport.describe()

football = Football("Playing", "Manchester United")
football.describe()

tool = Tool("Hammer")
tool.describe()

hammer = Hammer("Nail", "Metal")
hammer.describe()

instrument = Instrument("Piano")
instrument.describe()

guitar = Guitar("Playing", "Fender")
guitar.describe()

sound = Sound("Music")
sound.describe()