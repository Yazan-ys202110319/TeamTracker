def deleteTeam(): # Option 8
    while True:
        team_id_from_user = int(input("Enter the team ID to delete: "))
        if checkUniqueTeamId(team_id_from_user) == False:
                fp = open("teams.txt", "r")
                data_team = fp.readlines()
                fp.close()
                fp = open("teams.txt", "w")
                for i in data_team:
                    if not i.startswith(str(team_id_from_user) + ","):
                        fp.write(str(i))
                fp.close()
                myFile = open("players.txt", "r")
                players_info = myFile.readlines()
                myFile.close()
                myFile = open("players.txt", "w")
                for k in players_info:
                    split_Data = k.split(",")
                    id_team = int(split_Data[5])
                    if id_team != team_id_from_user:
                        myFile.write(str(k))
                myFile.close()
                print(f"Team with ID {team_id_from_user} and its players deleted successfully.")
                break
        else:
            print("Error: Team with ID does not exist")
            break
        

# ---------------------------------------------------------------------------------------------

def deletePlayer(): # Option 7
    player_id = int(input("Enter the player ID to delete: "))
    while True:
        if checkUniquePlayerId(player_id) == False:
            fp = open("players.txt", "r")
            data_pl = fp.readlines()
            fp.close()
            fp = open("players.txt", "w")
            for i in data_pl:
                if not i.startswith(str(player_id) + ","): # If the Id in the file do not starts like the Id enterd by the
                    fp.write(str(i))                       # user then write it beecouse this is a diffrent player, else do not write it becouse this is the player.
            fp.close()
            print(f"Player with ID {player_id} deleted successfully.")
            break
        else:
            print("Error: Player with ID does not exist")
            break

# ---------------------------------------------------------------------------------------------

def showPlayersWithoutTeams(): # option 6
    fp = open("players.txt", "r")
    playerData = fp.readlines()
    fp.close()
    gap = " " * 3
    print("Players without a team:")
    heading = f"{'ID':3s}{gap}{'Name':20s}{gap}{'Goals':5s}{gap}{'Y-Cards':3s}{gap}{'R-cards':3s}"
    print(heading)
    print("----------------------------------------------------------")
    for line in playerData:
        playerData = line.rstrip("\n").split(",")
        id_team = int(playerData[5])
        if id_team == 0:
            teamName = getTeamName(id_team)
            rec = f"{playerData[0]:3s}{gap}{playerData[1]:20s}{gap}{playerData[2]:5s}{gap}{playerData[3]:7s}{gap}{playerData[4]:7s}{gap}"
            print(rec)

# ---------------------------------------------------------------------------------------------

def getTeamName(id_team):
    fp = open("teams.txt", "r")
    for line in fp:
        data = line.strip().split(",")
        if int(data[0]) == id_team:
            return data[1]
    return "No-Team"

def checkTeamIdInFile(new_team_id):
    fp = open("teams.txt", "r")
    for id in fp:
        if id.startswith(str(new_team_id) + ","):
            return True
    return False

def displayAllPlayers(): # Option 5
    fp = open("players.txt", "r")
    playerData = fp.readlines()
    fp.close()
    gap = " " * 3
    print("All Players:")
    heading = f"{'ID':3s}{gap}{'Name':20s}{gap}{'Goals':5s}{gap}{'Y-Cards':3s}{gap}{'R-cards':3s}{gap}{'Team':3s}"
    print(heading)
    print("------------------------------------------------------------------")
    for line in playerData:
        playerData = line.rstrip("\n").split(",")
        id_team = int(playerData[5])
        if id_team == 0:
            rec = f"{playerData[0]:3s}{gap}{playerData[1]:20s}{gap}{playerData[2]:5s}{gap}{playerData[3]:7s}{gap}{playerData[4]:7s}{gap}No-Team"
            print(rec)
        else: 
            teamName = getTeamName(id_team)
            rec = f"{playerData[0]:3s}{gap}{playerData[1]:20s}{gap}{playerData[2]:5s}{gap}{playerData[3]:7s}{gap}{playerData[4]:7s}{gap}{teamName}"
            print(rec)

# ---------------------------------------------------------------------------------------------

def checkUniqueTeamId(team_id): # To check the ID of the team.
    fp = open("teams.txt", "r")
    for ids in fp:
        if ids.startswith(str(team_id) + ","):
            return False 
    return True

def addTeam(): # Option 4 
    team_id = int(input("Enter team ID: "))
    team_name = input("Enter team name: ")
    if checkUniqueTeamId(team_id) == True:
        fp = open("teams.txt", "a")
        fp.write(f"{team_id},{team_name}\n")
    else:
        print("Error: This ID is already exists!")

# ---------------------------------------------------------------------------------------------

def showStatistics(): # Option 3
    try:
        total_goals = 0
        total_YC = 0
        total_RC = 0
        count = 0
        maxGoal = 0
        maxGoalName = ""
        maxY_Cards_number = 0
        maxY_Cards_Name = ""
        maxR_Cards_number = 0
        maxR_Cards_Name = ""
        fp = open("players.txt")
        for line in fp:
            info = line.rstrip().split(",")
            total_goals += int(info[2])
            total_YC += int(info[3])
            total_RC += int(info[4])
            count += 1

            if int(info[2]) > int(maxGoal): # to get the name and number of hieghest goal.
                maxGoalName = info[1]
                maxGoal = info[2]
            if int(info[3]) > int(maxY_Cards_number): # to get the name and number of Y cards.
                maxY_Cards_Name = info[1]
                maxY_Cards_number = info[3]
            if int(info[4]) > int(maxR_Cards_number): # to get the name and number of R cards.
                maxR_Cards_Name = info[1]
                maxR_Cards_number = info[4]

        avg_goals = format(total_goals / count, ".2f")

        s = "Statistics:"
        print(s)
        print("Total goals:",total_goals)
        print("Average goals per player:",avg_goals)
        print("Total yellow cards",total_YC)
        print("Total red cards",total_RC)
        print("Player with highest goals: {} ({} goals)".format(maxGoalName, maxGoal))
        print("Player with highest yellow cards: {} ({} yellow cards)".format(maxY_Cards_Name, maxY_Cards_number))
        print("Player with highest red cards: {} ({} red cards)".format(maxR_Cards_Name, maxR_Cards_number))

        myFile = open("statistics", "w")
        myFile.write("")
        myFile.close()

        myFile = open("statistics", "w")
        myFile.write(s + "\n")
        myFile.write(f"Total goals:" +" "+ "{}".format(str(total_goals)) + "\n")
        myFile.write("Average goals per player:" + " " + "{}".format(str(avg_goals)) + "\n")
        myFile.write("Total yellow cards:" + " " + "{}".format(str(total_YC)) + "\n")
        myFile.write("Total red cards:" + " " + "{}".format(str(total_RC)) + "\n")
        myFile.write("Player with highest goals: {} ({} goals)".format(str(maxGoalName), str(maxGoal)) + "\n")
        myFile.write("Player with highest yellow cards: {} ({} yellow cards)".format(str(maxY_Cards_Name), str(maxY_Cards_number)) + "\n")
        myFile.write("Player with highest red cards: {} ({} red cards)".format(str(maxR_Cards_Name), str(maxR_Cards_number)) + "\n")
        print("Statistics saved statistics.txt")
    except ZeroDivisionError:
        print("Error: There are no players!")

# ---------------------------------------------------------------------------------------------

def updatePlayerStatistics(): # Option 2
    player_id = int(input("Enter the ID of the player to update: "))
    while True:
        if checkUniquePlayerId(player_id) == False:
            while True:
                user = int(input(" \nUpdate options:\n1. Add goal\n2. Add yellow card\n3. Add red card\n4. Change team\nEnter your choice (1, 2, 3, or 4): "))
                if user not in [1,2,3,4]:
                    print("Error: Invalid option")
                    break
                else:
                    fp = open("players.txt", "r")
                    info = fp.readlines()
                    player_exist = False
                    fp.close()
                    fp = open("players.txt", "w")
                    for line in info:
                        data = line.rstrip().split(",")
                        if int(data[0]) == player_id:
                            player_exist = True
                            if user == 1: 
                                get_goal = int(data[2])
                                get_goal += 1 # Adding 1 goal
                                fp.write(f"{data[0]},{data[1]},{str(get_goal)},{data[3]},{data[4]},{data[5]}\n")
                            elif user == 2:
                                get_YC = int(data[3])
                                get_YC += 1 # Adding 1 YC
                                fp.write(f"{data[0]},{data[1]},{data[2]},{str(get_YC)},{data[4]},{data[5]}\n")
                            elif user == 3:
                                get_RC = int(data[4])
                                get_RC += 1 # Adding 1 RD
                                fp.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{str(get_RC)},{data[5]}\n")
                            elif user == 4:
                                file = open("teams.txt", "r")
                                team_ids = []
                                for line in file.readlines():
                                    team_ids.append(int(line.rstrip().split(",")[0]))
                                while True:
                                    new_team_id = int(input("Enter new team ID: "))
                                    if new_team_id == 0 or new_team_id in team_ids:
                                        fp.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{str(new_team_id)}\n")
                                        break
                                    else:
                                        print("Error: Team with ID does not exist")
                            print("Player data updated.")
                        else:
                            fp.write(line)
                    fp.close()
                    if not player_exist:
                        print("Error: Player not found!")
                    break
        else:
            print("Error: Player not found!")
        break
    
# ---------------------------------------------------------------------------------------------

def checkTeamNumber(team_id_s): # Realated to option 1
    fp = open("teams.txt", "r")
    for line in fp:
        fields = line.strip().split(',')
        if fields[0] == team_id_s:
            return True
    return False

def checkTeamZero(team_id): # Realated to option 1
    if team_id == 0:
        return True
    return False

def checkUniquePlayerId(player_id): # To check the ID of the player.
    fp = open("players.txt", "r")
    for ids in fp:
        if ids.startswith(str(player_id) + ","):
            return False
    return True

def addPlayer(): # Option 1 
    print("*************")
    player_id = int(input("Enter player ID: "))
    player_name = input("Enter player name: ")
    goal_number = int(input("Enter number of goals: "))
    yellow_cards = int(input("Enter number of yellow cards: "))
    red_cards = int(input("Enter number of red cards: "))
    team_id = int(input("Enter team ID (Enter 0 if no team): "))
    team_id_s = str(team_id)
    if checkUniquePlayerId(player_id) == True:  # to check the palayer id if it is in the file or not.
        if team_id == 0 or checkTeamNumber(team_id_s) == True:
            fp = open("players.txt", "a")
            fp.write(f"{player_id},{player_name},{goal_number},{yellow_cards},{red_cards},{team_id_s}\n")
        else:
            print("Error: Team with ID does not exist")
    else:
        print("Error: This ID is already exists!")

# ---------------------------------------------------------------------------------------------

def creat_file(): # To creat empty files
    fp = open("players.txt", "w")
    fp.write("")
    fp.close()
    fp = open("teams.txt", "w")
    fp.write("")
    fp.close()

def main(): # menu 
    creat_file()

    while True:
        print("\n")
        menu = int(input("Menu:\n\t1. Add Player\n\t2. Update Player Statistics\n\t3. Show statistics\n\t4. Add Team\n\t5. Display all players\n\t6. Show players without teams\n\t7. Delete a player\n\t8. Delete a team\n\t9. Exit\nEnter your choice (1, 2, 3, or 9): "))
        if menu == 1: 
            addPlayer() 
        elif menu == 2:
            updatePlayerStatistics()
        elif menu == 3:
            showStatistics()
        elif menu == 4:
            addTeam()
        elif menu == 5:
            displayAllPlayers()
        elif menu == 6:
            showPlayersWithoutTeams()
        elif menu == 7:
            deletePlayer()
        elif menu == 8:
            deleteTeam()
        elif menu == 9:
            print("Exiting...")
            break
main()