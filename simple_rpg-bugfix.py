from random import randint

class Character:
    def __init__(self):
        self.name = ''
        self.health = 1
        self.health_max = 1
    def do_damage(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0: print(str("%s evades %s's attack.") % (enemy.name, self.name))  # ## 2to3 ##
        else: print(str("%s cleaves %s with a large blade!") % (self.name, enemy.name)) # ## 2to3 ##
        return enemy.health <= 0

class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = 'Skeleton'
        self.health = randint(1, player.health)

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.state = 'Normal'
        self.health = 10
        self.health_max = 10
    def quit(self):
        print(str("%s can't find the way back home, and dies of starvation.\nR.I.P.") % self.name) # ## 2to3 ##
        self.health = 0 # this would be a good place to return a score() function
    def help(self): print(Commands.keys()) ### prints correct statement but needs conversion to non dict_keys type
    def status(self): print(str("%s's health: %d/%d") % (self.name, self.health, self.health_max)) # ## 2to3 ##
    def fart(self):
        fart_potential = randint(0,1)
        if fart_potential == 0:
            print (str("%s lets out a moderate toot.") % (self.name)) # ## 2to3 ##
        if fart_potential == 1: # further potentials removed due to being test feature. n_potential == module
            print (str("The universe splits in two as %s's ass blasts a new big bang.") % (self.name)) # ## 2to3 ##
    def tired(self):
        print (str("%s feels tired.") % self.name) # ## 2to3 ##
        self.health = max(1, self.health - 1)
    def rest(self):
        if self.state != 'Normal': print(str("%s can't rest now!") % self.name); self.enemy_attacks() #self.state prints (str) w/ modulo statement
        else:
            print (str("%s rests.") % self.name) #print()->print(str)
            if randint(0, 1):
                self.enemy = Enemy(self)
                print(str("%s is awakened by %s!") % (self.name, self.enemy.name)) #Python 2 to 3 conversion
                self.state = 'fight'
                self.enemy_attacks()
            else:
                if self.health < self.health_max:
                    self.health = self.health + 1
                else: print(str("%s slept too much.") % self.name); self.health = self.health - 1 #another print(str)
    def explore(self):
        if self.state != 'Normal':
            print(str("%s is too busy right now!") % self.name) #changed to print(str(%s 'str' % self.name))
            self.enemy_attacks()
        else:
            print(str("%s explores a twisty passage in a cavern.") % self.name) #changed to print(str)
            if randint(0, 1):
                self.enemy = Enemy(self)
                print(str("%s encounters %s!") % (self.name, self.enemy.name)) #print() changed to print(str)
                self.state = 'fight'
            else:
                if randint(0, 1): self.tired()
    def flee(self): #self.state changed to print(str)
        if self.state != 'fight': print(str("%s exhausts their body running around for no reason.") % self.name); self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.enemy.health):
                print(str("%s flees from %s.") % (self.name, self.enemy.name)) # ## 2to3 ##
                self.enemy = None
                self.state = 'Normal' #next else: statement changed to print(str)
            else: print(str("%s couldn't escape from %s!") % (self.name, self.enemy.name)); self.enemy_attacks()
    def attack(self):
        if self.state != 'fight': print(str("%s swings a sword wantonly in the air at nothing.") % self.name); self.tired()
        else:
            if self.do_damage(self.enemy):
                print(str("%s executes %s!") % (self.name, self.enemy.name)) # ## 2to3 ##
                self.enemy = None
                self.state = 'Normal'
                if randint(0, self.health) < 10:
                    self.health = self.health + 1
                    self.health_max = self.health_max + 1
                    print(str("%s feels stronger!") % self.name) #print('%s n') % o changed to print(str('%s n') % o)) ## prints(playername modulo given string output) 
                else: self.enemy_attacks()
    def enemy_attacks(self):
        if self.enemy.do_damage(self): print(str("%s was slaughtered by %s!/nR.I.P.") % (self.name, self.enemy.name)) # ## 2to3 ## str

Commands = {
    'quit'   : Player.quit,
    'help'   : Player.help,
    'status' : Player.status,
    'rest'   : Player.rest,
    'explore': Player.explore,
    'flee'   : Player.flee,
    'attack' : Player.attack,
    'fart'   : Player.fart,
    }

p = Player()
p.name = input("Name your character: ")
print(str("(type help to get a list of actions)\n")) # ## 2to3 ##
print(str("%s enters a dark cave, searching for adventure.") % p.name) # ## 2to3 ##

while(p.health > 0):
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](p)
                commandFound = True
                break
        if not commandFound:
            print(str("%s doesn't understand the suggestion.") % p.name) # ## 2to3 ##
