# List of quarterbacks
qbs = [
    'Josh Allen', 'Jalen Hurts', 'Dak Prescott', 'Lamar Jackson', 
    'Jordan Love', 'Brock Purdy', 'Jared Goff', 'Patrick Mahomes', 
    'Baker Mayfield', 'Tua Tagovailoa'
]

# List of wide receivers
wrs = [
    'CeeDee Lamb', 'Tyreek Hill', 'Amon-Ra St. Brown', 'Puka Nacua', 
    'Mike Evans', 'DJ Moore', 'A.J. Brown', 'Stefon Diggs', 
    'Davante Adams', 'Ja\'Marr Chase'
]

# List of tight ends
tes = [
    'Sam LaPorta', 'Evan Engram', 'George Kittle', 'David Njoku', 
    'Cole Kmet', 'Jake Ferguson', 'Trey McBride', 'Dalton Kincaid', 
    'Kyle Pitts', 'Logan Thomas'
]

# Function to remove drafted players from the available pool
def remove_drafted_players(drafted_players, available_players):
    for drafted_player in drafted_players:
        if drafted_player in available_players:
            available_players.remove(drafted_player)

# Getting user pick
def get_user_pick(available_players):
    print("\nAvailable Players:")
    for i, player in enumerate(available_players, 1):
        print(f"{i}. {player}")

    choice = int(input("\nEnter the number of the player you want to draft: ")) - 1
    if 0 <= choice < len(available_players):
        return available_players[choice]
    else:
        print("Invalid choice. Try again.")
        return get_user_pick(available_players)

# Main draft pick function
def fantasy_draft_pick():
    print("Welcome to your 12-team fantasy football draft!")
    user_team_pick = int(input("Enter your draft position (1-12): "))
    
    if not 1 <= user_team_pick <= 12:
        print("Invalid position. Please enter a number between 1 and 12.")
        return

    # Combine all positions into one list
    available_players = qbs + wrs + tes
    
    # If the user doesn't have the first pick, ask them which players have already been drafted
    if user_team_pick > 1:
        picks_before_user = user_team_pick - 1
        print(f"\nThere have been {picks_before_user} picks before your turn.")
        drafted_players = input("Enter the names of the players drafted before your pick, separated by commas: ").split(",")
        drafted_players = [player.strip() for player in drafted_players]
        remove_drafted_players(drafted_players, available_players)
    
    # Show available players and let the user choose
    user_pick = get_user_pick(available_players)
    print(f"\nYou have selected {user_pick}!")

# Main function to run the program
def main():
    fantasy_draft_pick()

if __name__ == "__main__":
    main()
