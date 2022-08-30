#Javon Jackson




def instructions():
    #game intro and instructions
    print('~~~T A I N T E D      B L O O D~~~\n')

    print('Collect all 6 items and defeat the Vampire Lord!')
    print('You must collect all items before you fight the boss!\n')

    print('Movement commands: go north, go south, go east, go west\n')

    print('Item commands: grab \'item name\'')
    print('Items you can grab will be marked *like this*.\n')

    print('Type \'exit\' to quit the game.\n')


def start_game():
    #opening text
    print('You wake up in a cold, damp dungeon cell...')
    print('You feel drained of energy...')
    print('Suddenly, your cell door begins to open.')
    print('It seems like....you are free to go.')
    # separation line
    print('-' * 60)


def show_status(location, inv):
    #shows player location and inventory
    print('\nYou are in the {}.'.format(location))
    print('Inventory: {}'.format(inv))
    if location == 'Dungeon Cell':
        print('\nYou see the Mess Hall to the north.')
        print('You see the Guard Tower to the east.')
    elif location == 'Mess Hall':
        print('\nYou see the Garden to the north.')
        print('You see the Dungeon Cell to the south.')
        print('You see the Barracks to the east.')
        print('You see the Kitchen to the west.')
    elif location == 'Guard Tower':
        print('\nYou see the Dungeon Cell to the west.')
    elif location == 'Kitchen':
        print('\nYou see the Mess Hall to the east.')
    elif location == 'Barracks':
        print('\nYou see the Mess Hall to the west.')
    elif location == 'Sewers':
        print('\nYou see the Garden to the east.')
    elif location == 'Garden':
        print('\nYou see the Mess Hall to the South.')
        print('You see the Sewers to the west.')
        print('You see the Great Room to the east, it\'s radiating with a devilish aura.')



def item_check(items, current_room):
    #checks if the player has all items and notifies them of new items in their room
    if len(items) == 6:
        print('You feel like you have found everything you need to take on the Vampire Lord.')
        print('Maybe you should find the Great Room, where the vampire lord rests.')
    if current_room == 'Mess Hall' and 'Diary' not in items:
        print('\nThe room is dead silent.')
        print('You see a *book* sitting on one of the mess hall tables.')
        print('Maybe it has some useful information.')
    elif current_room == 'Guard Tower' and 'Guard Report' not in items:
        print('\nYou notice a stack of *papers* on the guard desk.')
        print('But not a soul in sight...')
    elif current_room == 'Barracks' and 'Crossbow' not in items:
        print('\nYou see a lone *crossbow* on the weapon rack.')
        print('Maybe you should grab it so you can defend yourself.')
    elif current_room == 'Kitchen' and 'Cloves of Garlic' not in items:
        print('\nYou smell a heavy stench of *garlic* coming from a barrel in the corner.')
        print('Maybe this will help ward off vampires.')
    elif current_room == 'Sewers' and 'Quiver of Silver Bolts' not in items:
        print('\nYou see a dead body with a *quiver* strapped to its back.')
        print('He has no use for it anymore...')
    elif current_room == 'Garden' and 'Wooden Stake' not in items:
        print('\nThe garden is filled with grapes, potatoes and wild berry bushes.')
        print('But no gardener in sight...')
        print('Theres a gardeners tool stand with a shovel, a wooden *stake*, and a garden trowel.')



def main():
    rooms = {  # rooms dictionary
        'Dungeon Cell': {'North': 'Mess Hall', 'East': 'Guard Tower'},
        'Guard Tower': {'West': 'Dungeon Cell', 'Item': 'Guard Report'},
        'Mess Hall': {'North': 'Garden', 'South': 'Dungeon Cell', 'East': 'Barracks', 'West': 'Kitchen',
                      'Item': 'Diary'},
        'Barracks': {'West': 'Mess Hall', 'Item': 'Crossbow'},
        'Kitchen': {'East': 'Mess Hall', 'Item': 'Cloves of Garlic'},
        'Garden': {'South': 'Mess Hall', 'East': 'Great Room', 'West': 'Sewers', 'Item': 'Wooden Stake'},
        'Sewers': {'East': 'Garden', 'Item': 'Quiver of Silver Bolts'},
        'Great Room': {'West': 'Garden', 'Item': 'Mad Vampire Lord'}
    }

    #set start room and empty starting inventory
    current_room = 'Dungeon Cell'
    items = []

    while True:
            #check inventory for missing items
            item_check(items, current_room)

            #show location and inventory
            show_status(current_room, items)



# Great Room/boss check
            if current_room == 'Great Room':
                print('\nYou have entered the vampires resting place...')
                if len(items) < 6:
                    print('But without all of the right tools!')
                    print('Without fear, the vampire lord takes you down swiftly!')
                    print('You have been defeated! Try again!')
                    break
                elif len(items) == 6:
                    print('With all of the tools necessary to defeat the vampire lord!')
                    print('\nThe lord is stunned by the heavy stench of garlic and drops to his knees.')
                    print('You take this opportunity to barrage him with silver crossbow bolts!')
                    print('The vampire lord screams in anguish, as the silver bolts pierce his once impenetrable skin.')
                    print('The lord is completely immobilized on the cold stone floor and begs for his life.')
                    print('You ignore the mad lord\'s cry for mercy and drive the wooden stake through his heart.')
                    print('\nYou have defeated the mad vampire lord! Congratulations!')
                    print('\nThank you for playing!')
                    break

            #command prompt
            action = input('What will you do?: ')
            print()
            # separation line
            print('-' * 60)

            #convert action to lowercase for readability
            action = action.lower()

            #exit command check
            if action == 'exit':
                current_room = 'Exit'

            if current_room == 'Exit':
                print('Thank you for playing Tainted Blood!')
                break


#Dungeon Cell
            elif current_room == 'Dungeon Cell':
                if 'go' in action:
                    if 'north' in action:
                        current_room = rooms['Dungeon Cell']['North']
                    elif 'east' in action:
                        current_room = rooms['Dungeon Cell']['East']
                    else:
                        print('\nInvalid action. Select a valid action.')
                else:
                    print('\nInvalid action. Select a valid action.')



# Mess Hall
            elif current_room == 'Mess Hall':
                if 'go' in action:
                    if 'north' in action:
                        current_room = rooms['Mess Hall']['North']
                    elif 'south' in action:
                        current_room = rooms['Mess Hall']['South']
                    elif 'east' in action:
                        current_room = rooms['Mess Hall']['East']
                    elif 'west' in action:
                        current_room = rooms['Mess Hall']['West']


            #Mess Hall item 'book/diary'
                elif 'grab' in action:
                    if 'book' in action:
                        if 'Diary' in items:
                            print('You already have everything useful from this area.')
                        elif 'Diary' not in items:
                            items.append(rooms['Mess Hall']['Item'])
                            del rooms['Mess Hall']['Item']
                            print('\nYou pick up a diary.')
                            print('You turn to a marked page that reads:')
                            print('\"Thank the heavens! I think the doctor finally found a way to kill the vampire lord.\"')
                            print('\"We have been stocking up on garlic in the kitchen to weaken him.\"')
                            print('\"Then we can use silver crossbow bolts to pierce his skin and do some damage.\"')
                            print('\"And when he\'s finally weak enough, we can drive a wooden stake through his heart and finish the job.\"')
                            print('\"That is, if he doesn\'t just suck the life out of every guard first. We\'re already down 60 men this month.\"')
                    else:
                        print('\nInvalid action. Select a valid action.')
                else:
                    print('\nInvalid action. Select a valid action.')

# Guard Tower
            elif current_room == 'Guard Tower':
                if 'go' in action:
                    if 'west' in action:
                        current_room = rooms['Guard Tower']['West']
                    else:
                        print('\nInvalid action. Select a valid action.')


            # Guard tower item 'guard report'
                elif 'grab' in action:
                    if 'papers' in action:
                        if 'Guard Report' in items:
                            print('You already have everything useful from this area.')
                        elif 'Guard Report' not in items:
                            items.append(rooms['Guard Tower']['Item'])
                            del rooms['Guard Tower']['Item']
                            print('\nYou see that the papers are the latest guard report.')
                            print('The report reads: ')
                            print('\"I can\'t believe this madness. The Vampire lord is sucking the life from anyone in sight. Even the guards.\"')
                            print('\"The Captain is fed up with losing his men to that mad man while we wait for the prisoner with the special blood to wake up.\"')
                            print('\"When the merchant finally gets here through the secret entrance in the sewers, we\'ll finally have those silver bolts to kill the bastard.\"')
                            print('\"I\'m supposed to meet him in the sewers tonight, I hope he doesn\'t get caught before I get to him\"')
                            print('\"....or die.\"')

                    else:
                        print('\nInvalid action. Select a valid action.')
                else:
                    print('\nInvalid action. Select a valid action.')



# Garden
            elif current_room == 'Garden':
                if 'go' in action:
                    if 'south' in action:
                        current_room = rooms['Garden']['South']
                    elif 'east' in action:
                        current_room = rooms['Garden']['East']
                    elif 'west' in action:
                        current_room = rooms['Garden']['West']
                    elif 'north' in action:
                        print('\nInvalid action. Select a valid action.')


            #Garden item 'stake'
                elif 'grab' in action:
                    if 'stake' in action:
                        if 'Wooden Stake' in items:
                            print('You already have everything useful from this area.')
                        elif 'Wooden Stake' not in items:
                            items.append(rooms['Garden']['Item'])
                            del rooms['Garden']['Item']
                            print('\nYou pick up a wooden stake.')
                    else:
                        print('\nInvalid action. Select a valid action.')
                else:
                    print('\nInvalid action. Select a valid action.')



# Barracks
            elif current_room == 'Barracks':
                if 'go' in action:
                    if 'west' in action:
                        current_room = rooms['Barracks']['West']
                    else:
                        print('\nInvalid action. Select a valid action.')

            #Barracks item 'crossbow'
                elif 'grab' in action:
                    if 'crossbow' in action:
                        if 'Crossbow' in items:
                            print('You already have everything useful from this area.')
                        elif 'Crossbow' not in items:
                            items.append(rooms['Barracks']['Item'])
                            del rooms['Barracks']['Item']
                            print('\nYou pick up a heavy crossbow.')
                    else:
                        print('\nInvalid action. Select a valid action.')
                else:
                    print('\nInvalid action. Select a valid action.')


# Kitchen
            elif current_room == 'Kitchen':
                if 'go' in action:
                    if 'east' in action:
                        current_room = rooms['Kitchen']['East']
                    else:
                        print('\nInvalid action. Select a valid action.')

            #Kitchen item 'garlic'
                elif 'grab' in action:
                    if 'garlic' in action:
                        if 'Cloves of Garlic' in items:
                            print('You already have everything useful from this area.')
                        elif 'Cloves of Garlic' not in items:
                            items.append(rooms['Kitchen']['Item'])
                            del rooms['Kitchen']['Item']
                            print('\nYou pick up the pouch full of garlic cloves.')
                            print('You attach the pouch to your belt, hoping it will ward off any vampires.')
                    else:
                        print('\nInvalid action. Select a valid action.')

                else:
                    print('\nInvalid action. Select a valid action.')

# Sewers
            elif current_room == 'Sewers':
                if 'go' in action:
                    if 'east' in action:
                        current_room = rooms['Sewers']['East']
                    else:
                        print('\nInvalid action. Select a valid action.')

            #Sewer item 'quiver'
                elif 'grab' in action:
                    if 'quiver' in action:
                        if 'Quiver of Silver Bolts' in items:
                            print('You already have everything useful from this area.')
                        elif 'Quiver of Silver Bolts' not in items:
                            items.append(rooms['Sewers']['Item'])
                            del rooms['Sewers']['Item']
                            print('\nYou pick up a quiver full of bolts.')
                            print('They are shiny, heavy and.... made of silver!')
                            print('These will be perfect for taking down a vampire!')
                    else:
                        print('\nInvalid action. Select a valid action.')
                else:
                    print('\nInvalid action. Select a valid action.')



instructions()
start_game()
main()
