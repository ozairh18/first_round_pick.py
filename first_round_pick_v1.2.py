'''
File:        first_round_pick.py
Author:      Ozair Hussain
Date:        10/1/24
Description: This program will ask users how many teams are in their .5 Points
             Per Reception (PPR) league, what number pick they have, what players were drafted,
             and who they want to draft with their first round pick.
'''

# Constant variables

# Running backs
rbs = ['Christian McCaffrey', 'Travis Etienne Jr.', 'Breece Hall', 'Joe Mixon', 'Rachaad White', 'Derrick Henry',
       'Bijan Robinson, 'James Cook', 'Tony Pollard', 'Jerome Ford']

# Wide receivers
wrs = ['CeeDee Lamb', 'Tyreek Hill', 'Amon-Ra St. Brown', 'Puka Nacua', 'Mike Evans', 'DJ Moore', 'A.J. Brown',
       'Stefon Diggs', 'Davante Adams', 'Ja\'Marr Chase']

# Tight ends
tes = ['Sam LaPorta', 'Evan Engram', 'George Kittle', 'David Njoku', 'Cole Kmet', 'Jake Ferguson', 'Trey McBride',
       'Dalton Kincaid', 'Kyle Pitts', 'Logan Thomas']
       
# Quarterbacks
qbs = ['Josh Allen', 'Jalen Hurts', 'Dak Prescott', 'Lamar Jackson', 'Jordan Love', 'Brock Purdy', 'Jared Goff',
       'Patrick Mahomes', 'Baker Mayfield', 'Tua Tagovailoa']

# Function to remove drafted players from available players
def remove_drafted_players(drafted_players, available_players):
    
    for drafted_player in drafted_players: # Iterate through drafted players
        if drafted_player in available_players: # Check if drafted player is an available player
            available_players.remove(drafted_player) # Remove drafted player from available players

# Function for user pick
def user_pick(available_players):

    print("\nAvailable Players:")
    for player in available_players: # Iterate through available players
        print(f'The available players are ' + player) # Print available players

    while True:
        selection = input('\nEnter the name of the player you want to draft: ').lower() # Ask user to enter name of player they want to draft

        for player in available_players:
        if player.lower == selection:
            return selection
        else:
            print(selection, 'is not in the list of available players.')
            return user_pick(available_players)

# Function to start draft
def start_draft():

    print('Welcome to your 2024-25 fantasy football league!')

    # Ask user for number of teams in league
    num_of_teams = int(input('How many teams are in your fantasy football league? (Enter a number between 1 - 12) '))

    if 1 > num_of_teams > 12: # Check if number of teams is less than 1 and greater than 12
        print('You need to enter a number between 1 - 12.')
        return

    # Ask user for number pick
    pick = int(input('What number pick do you have in the first round? (Enter a number between 1 - 12) '))

    if 1 > pick < 12: # Check if pick is less than 1 and greater than 12
        print('You need to enter a number between 1 - 12')
        return

    # Combine all available players into one list
    available_players = rbs + wrs + tes + qbs

    if pick > 1: # Check if user doesn't have first pick
        picks_before_user = pick - 1
        print(f'\nThere have been {picks_before_user} pick(s) before you.')
        drafted_players = input('Enter the names of the player(s) drafted before your pick: ').lower().split(',')
        stripped_players = [] # Initialize empty list for stripped players
        for player in drafted_players:
            stripped_players.append(player.strip()) # Append player with stripped whitespace to stripped players
        drafted_players = stripped_players # Set drafted players to stripped players
        remove_drafted_players(stripped_players, available_players)

    pick = user_pick(available_players) # Show available players and let user pick

    print(f'\nYou drafted {pick}!') # Print player drafted by user

    print(f'\nThe remaining players are', available_players) # Print remaining players
    

# Function to define main
if __name__ == '__main__':

    # Call start draft
    start_draft()
