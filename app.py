# from random import choice
#
# players = ['Aron', 'Bob', 'Carla', 'David', 'Nick', 'James', 'Dimitri']
#
#
# for i in range(4):
#     print(choice(players))


from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)
