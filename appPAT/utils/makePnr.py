import random


class MakePNR:
    numbers = [chr(i) for i in range(48, 58)]
    letters = [chr(i) for i in range(65, 91)]
    all_characters = numbers + letters

    def __init__(self) -> None:
        self.pnr = random.choices(population=self.all_characters, k=6)
        self.pnr = ''.join(self.pnr)
