# Password Generator

This small script is a weak password generator tool which can be used in bruteforce.

## Usage

```python
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

alphabet_sequence = generator.alphabet_sequence(mode='lower')
number_squence = generator.number_sequence(counter=4)
result = generator.mix_sequence(alphabet_sequence, number_squence)
generator.write_to_file(result)
```