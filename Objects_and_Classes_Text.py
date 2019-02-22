#Python language basics 7
#Classes and objects
#Class Fields, methods, and constructors
#Object instatioation

'''
    Object:
        some entity within the code that has state and behavior that we might need to keep track of. An Onject is an instance of a class that keeps track of all
        the fields, methods, and constructors of that particular object.
    State:
        represented thorugh field (global vairables, variables etc.)
    Behavior:
        implemented through functions that do things (called methods when inside of a class).
    Constructors:
        create new instances of objects (Object Insatiation) through the us of constructors. Constructors are a special type of method
        that help set up all of the fields of a class.
    Class:
        the implimentation of fields, methods, and constructors. The "Blue Print".
'''

#Class is not inheriting from anything thus ending with a colon.
class GameCharacter:

    #We dont have to pass in the value into the constructor (assinged this value when class is instantiated).
    speed = 5
    
    #self refers to this class (GameCharacter) and is necessary for all the methods within the class.
    def __init__(self, name, width, height, x_pos, y_pos):
        #there will be a global variable within the GameCharacter class called name and we are assigning it the value of name
        self.name = name
        #Can always name the varuable after self. differently ex: self.not_same = width
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

character_0 = GameCharacter('char_0', 50, 100, 100, 100)
character_0.name    # 'char_0'
character_0.name= 'char_1'
character_0.name    # 'char_1'

character_0.move(50, 100)
print(character_0.x_pos)
print(character_0.y_pos)

# Python language basics 8
# subclasses, superclasses, and inheritance

'''
    Subclasses:
        inherit from superclasses (gets access to all of the attributes/fields, behaviors/methods, and constructor)
'''

class PlayerCharacter(GameCharacter):

    speed = 10
    
    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)     #calls the super classe's __init__ method and has width and height pre set

    def move(self, by_y_amount):    #method overriding
        super().move(0, by_y_amount)

player_character = PlayerCharacter('P_character', 500, 500)
print(player_character.name)
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)
