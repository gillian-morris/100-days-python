# Day 3 - Treasure Island
# Using conditional operators to create a little text based game
print(r'''
    ___ __
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
user_input = input("Would you like to go 'left' or 'right'? ")
if user_input != "left":
    print("You fell into a hole. Game over.")
else:
    user_input = input("Would you like to 'swim' or 'wait' to cross the river? ")
    if user_input != "wait":
        print("Attacked by trout. Game over.")
    else:
        user_input = input("Which door? 'red', 'yellow', or 'blue' ")
        if user_input == "red":
            print("Burned by fire. Game over.")
        elif user_input == "blue":
            print("eaten by bees. Game over.")
        elif user_input == "yellow":
            print("You win!")
        else:
            print("Game over.")
