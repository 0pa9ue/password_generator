import random
import string


class Generator(object):
    def __init__(self):
        self.ascii_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.ascii_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.ascii_keyboard_lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                                         'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                                         'z', 'x', 'c', 'v', 'b', 'n', 'm']
        self.ascii_keyboard_uppercase = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                                         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                                         'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    def alphabet_sequence(self, mode='lower', counter=2):
        if mode == 'upper':
            result = self.ascii_uppercase.copy()
            for i in range(1, counter):
                temp_list = result.copy()
                result.clear()
                for j in range(26):
                    result.extend([str(temp_list[k] + chr(ord('A') + j)) for k in range(len(temp_list))])
        elif mode == 'hybrid':
            result = self.ascii_lowercase.copy() + self.ascii_uppercase.copy()
            for i in range(1, counter):
                temp_list = result.copy()
                result.clear()
                for j in range(26):
                    result.extend([str(temp_list[k] + chr(ord('a') + j)) for k in range(len(temp_list))])
                for j in range(26):
                    result.extend([str(temp_list[k] + chr(ord('A') + j)) for k in range(len(temp_list))])
        else:
            result = self.ascii_lowercase.copy()
            for i in range(1, counter):
                temp_list = result.copy()
                result.clear()
                for j in range(26):
                    result.extend([str(temp_list[k] + chr(ord('a') + j)) for k in range(len(temp_list))])
        return sorted(result)

    def alphabet_repeat_sequence(self, mode='lower', startcounter=2, endcouter=6):
        result = []
        if mode == 'upper':
            for counter in range(startcounter, endcouter + 1):
                for alphabet in self.ascii_uppercase:
                    result.append(str(alphabet) * counter)
        elif mode == 'lower':
            for counter in range(startcounter, endcouter + 1):
                for alphabet in self.ascii_lowercase:
                    result.append(str(alphabet) * counter)
        return result

    def alphabet_progressive_sequence(self, mode='lower', step=3):
        result = []
        if mode == 'upper':
            for i in range(len(self.ascii_uppercase) - step + 1):
                result.append(''.join(self.ascii_uppercase[i:i + step]))
        elif mode == 'lower':
            for i in range(len(self.ascii_lowercase) - step + 1):
                result.append(''.join(self.ascii_lowercase[i:i + step]))
        return result

    def keyboard_progressive_sequence(self, mode='lower', step=3):
        result = []
        if mode == 'upper':
            for i in range(len(self.ascii_keyboard_uppercase) - step + 1):
                result.append(''.join(self.ascii_keyboard_uppercase[i:i + step]))
        elif mode == 'lower':
            for i in range(len(self.ascii_keyboard_lowercase) - step + 1):
                result.append(''.join(self.ascii_keyboard_lowercase[i:i + step]))
        return result

    def number_sequence(self, counter=6):
        result = self.digits.copy()
        for i in range(1, counter):
            temp_list = result.copy()
            result.clear()
            for j in range(10):
                result.extend([str(temp_list[k] + chr(ord('0') + j)) for k in range(len(temp_list))])
        return sorted(result)

    def number_repeat_sequence(self, startcounter=2, endcouter=6):
        result = []
        for counter in range(startcounter, endcouter + 1):
            for digit in self.digits:
                result.append(str(digit) * counter)
        return result

    def number_progressive_sequence(self, step=3):
        result = []
        for i in range(len(self.digits) - step + 1):
            result.append(''.join(self.digits[i:i + step]))
        return result

    def year_sequence(self, startyear=1900, endyear=2022):
        result = []
        for year in range(startyear, endyear + 1):
            result.append(str(year))
        return sorted(result)

    def year_month_sequence(self, startyear=1900, endyear=2022):
        result = []
        for year in range(startyear, endyear + 1):
            result.extend([str(year) + str(month).zfill(2) for month in range(1, 12)])
        return sorted(result)

    def year_month_day_sequence(self, startyear=1900, endyear=2022):
        result = []
        for year in range(startyear, endyear + 1):
            for month in range(1, 13):
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    days = 31
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    days = 30
                elif month == 2:
                    if year % 4 == 0:
                        days = 29
                    else:
                        days = 28
                result.extend(str(year) + str(month).zfill(2) + str(day).zfill(2) for day in range(1, days))
        return result

    def mix_sequence(self, *args):
        result = args[0]
        for i in range(1, len(args)):
            temp_list = result.copy()
            result.clear()
            for j in range(len(temp_list)):
                result.extend([str(temp_list[j]) + str(args[i][k]) for k in range(len(args[i]))])
        return result

    def write_to_file(self, result):
        with open('./result.txt', 'a+') as f:
            for item in result:
                f.write(item + '\n')


if __name__ == '__main__':
    generator = Generator()

    print(generator.alphabet_sequence(mode='hybrid'))
    # ['AA', 'AB', ... , 'Ly', 'Lz', ... , 'zz']
    print(generator.alphabet_repeat_sequence(mode='lower'))
    # ['aa', 'bb', ... , 'iiiii', 'jjjjj', ... , 'zzzzzz']
    print(generator.alphabet_progressive_sequence(mode='lower'))
    # ['abc', 'bcd', ... , 'pqr', 'qrs', ... , 'xyz']

    print(generator.number_sequence())
    # ['000000', '000001', ... , '123456', '123457', ... , '999999']
    print(generator.number_repeat_sequence())
    # ['11', '22', ... , '111', '222', ... , '000000']
    print(generator.number_progressive_sequence(step=4))
    # ['1234', '2345', ... , '5678', '6789', '7890']

    print(generator.year_sequence(startyear=1998, endyear=2000))
    # ['1998', '1999', '2000']
    print(generator.year_month_sequence(startyear=1998, endyear=2000))
    # ['199801', '199802', ... , '199911', '199912', ... , '200012']
    print(generator.year_month_day_sequence(startyear=1998, endyear=2000))
    # ['19980101', '19980102', ... , '19991101', 19991102', ... , '20001231']

    print(generator.keyboard_progressive_sequence(step=3))
    # ['qwe', 'wer', ... ,'asd', 'sdf', ... , 'bnm']

    # alphabet_sequence = generator.alphabet_sequence(mode='lower')
    # number_squence = generator.number_sequence(counter=4)
    # result = generator.mix_sequence(alphabet_sequence, number_squence)
    # generator.write_to_file(result)
