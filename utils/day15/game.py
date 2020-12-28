import typing


class Game:
    def __init__(self, starting_numbers: typing.List[int]):
        self.starting_numbers = starting_numbers
        self.counter = 0
        self.numbers_spoken = {}
        self.last_number_spoken = None

    def play(self, to: int) -> typing.Iterable[int]:
        return map(lambda _: self.speak(), range(to))

    def speak(self) -> int:
        if self.counter < len(self.starting_numbers):
            number = self.starting_numbers[self.counter]
        elif len(self.numbers_spoken.get(self.last_number_spoken, [])) == 1:
            number = 0
        else:
            last_number_spoken_at = self.numbers_spoken[self.last_number_spoken]
            assert len(last_number_spoken_at) >= 2
            number = last_number_spoken_at[-1] - last_number_spoken_at[-2]

        return self._speak(number)

    def _speak(self, number: int) -> int:
        spoken_previously = self.numbers_spoken.get(number, [])
        spoken_previously.append(self.counter)
        self.numbers_spoken[number] = spoken_previously

        self.counter += 1
        self.last_number_spoken = number
        return number

