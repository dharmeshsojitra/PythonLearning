class Utils:
    def __inti__(self):
        pass

    def find_max(self, numbers):
        max = numbers[0]
        for number in numbers:
            if number > max:
                max = number

        return max