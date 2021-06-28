import random
from pathlib import Path

# choice of a leader using random method
# members = ['Stenn', 'BAm', 'Henry', 'Michel']
# leader = random.choice(members)
# print(leader)

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

print('___________________________________________')
path = Path()
for file in path.glob('*.py'):
    print(file)