class Utils:
    def __inti__(self):
        pass

    def find_max(self, numbers):
        maximum = numbers[0]
        for number in numbers:
            if number > maximum:
                maximum = number

        return maximum