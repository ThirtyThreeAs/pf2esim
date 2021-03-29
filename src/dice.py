from random import randrange

class Dice:
    def __init__(self, sides=20, bonus=0):
        """
        Class to encapsulate dice rolls.
        :param sides: int, the number of sides on the die
        :param bonus: int, flat bonus that is added to the result
        """

        # class members
        self.bonus = bonus
        self.sides = sides

    def roll(self, num_of_dice=1):
        return sum([randrange(1,self.sides) for x in range(num_of_dice)])+self.bonus



