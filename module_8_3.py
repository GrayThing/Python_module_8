class Car:
    def __init__(self, model: str, vin: int, numbers: str ):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number: int):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber(f'Expected class int, got {type(vin_number).__name__} instead')
        if vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber(f'Vin number must be in range 1000000 - 9999999, got {vin_number}')
        return True

    def __is_valid_numbers(self, numbers: str):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'Expected class str, got {type(numbers).__name__} instead')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f'Numbers must be equal 6, got {len(numbers)}')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
