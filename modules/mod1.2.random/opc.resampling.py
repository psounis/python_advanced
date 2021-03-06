"""
game: two dice
source: http://hplgit.github.io/primer.html/doc/pub/random/._random-readable004.html#sec:random:twodicesumguess
"""

import random, sys

class Dice:
    def __init__(self, n=1):
        self.n = n   # no of dice

    def throw(self):
        return [random.randint(1,6) for i in range(self.n)]

class Player(object):
    def __init__(self, name, capital, guess_function, ndice):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)

    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.guess
        else:
            self.capital -= 1
        self.message()
        self.broke()

    def message(self):
        print('%s guessed %d, got %d' % (self.name, self.guess, self.throw))

    def broke(self):
        if self.capital == 0:
            print('%s lost!' % self.name)
            sys.exit(0)  # end the program

def computer_guess(ndice):
    # All guesses have the same probability
    return random.randint(ndice, 6*ndice)

def player_guess(ndice):
    return int(input('Guess the sum of the no of eyes in the next throw: '))

def play(nrounds, ndice=2):
    player = Player('YOU', nrounds, player_guess, ndice)
    computer = Player('Computer', nrounds, computer_guess, ndice)

    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        print('Status: user has %d euro, machine has %d euro\n' % (player.capital, computer.capital))

    if computer.capital > player.capital:
        winner = 'Machine'
    else:
        winner = 'You'
    print(winner, 'won!')


play(8, 1)