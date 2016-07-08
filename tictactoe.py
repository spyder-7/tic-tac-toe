import os

class TicTacGame(object):
    boardNum=list(range(1,10))

    def __init__(self):
        while True:
            try:
                self.menu()
                menuSelection=int(input("Select the number from menu: => "))
            except:
                print("\nInvalid input: please select the number from menu\n")
                continue
            else:
                if not menuSelection in (1,2,3):
                    print("\nInvalid input: try again with number available in the menu\n")
                    continue
                else:
                    if menuSelection==1:
                        self.playGame()
                    if menuSelection==2:
                        print("Developed by: Spyder")
                        print("Version: 1.0")
                        print("Progamiing Language: Python\n")
                    if menuSelection==3:
                        break

    def menu(self):
        print("Welcome to TIC TAC TOE Game")
        print("1. Play Game")
        print("2. Credits")
        print("3. Quit\n")

    def printBoard(self):
        print(" {n7}  | {n8}  | {n9}  ".format(n7=TicTacGame.boardNum[6], n8=TicTacGame.boardNum[7], n9=TicTacGame.boardNum[8]))
        print("-------------")
        print(" {n4}  | {n5}  | {n6}  ".format(n4=TicTacGame.boardNum[3], n5=TicTacGame.boardNum[4], n6=TicTacGame.boardNum[5]))
        print("-------------")
        print(" {n1}  | {n2}  | {n3}  ".format(n1=TicTacGame.boardNum[0], n2=TicTacGame.boardNum[1], n3=TicTacGame.boardNum[2]))

    def playersTeams(self):
        teams=("X","O")
        p1Name=input("Player 1: please enter your name: => ").title()
        while True:
            p1Team=input("Player 1: please select your team (X or O): => ").upper()
            if p1Team=="X" or p1Team=="O":
                break
            else:
                print("Invalid team: try again with (X or O)")
                continue
        p2Name=input("Player 2: please enter your name: => ").title()
        if p1Team=="X":
            p2Team="O"
        else:
            p2Team="X"
        print("\n--------------------------------------")
        return p1Name,p1Team,p2Name,p2Team,teams

    def markGameBoard(self,playerNum,pName,pTeam,otherPlayer,mark):
        while True:
            try:
                num=int(input("Player {pNum}:({p}-Team:{t}) select num to place mark (1-9): => ".format(pNum=playerNum,p=pName,t=pTeam)))
            except:
                print("Invalid input: please try again with numbers (1-9)")
                continue
            else:
                if not num in range(1,10):
                    print("Invalid input: please try again with numbers (1-9)")
                    continue
                else:
                    if TicTacGame.boardNum[num-1] == pTeam:
                        print("Already marked by you, try again")
                        continue
                    elif TicTacGame.boardNum[num-1] == otherPlayer:
                        print("Already marked by second player, try again")
                        continue
                    else:
                        TicTacGame.boardNum[num-1] = mark
                        os.system("cls")
                        self.printBoard()
                        break

    def chkWin(self,pTeam):
        if TicTacGame.boardNum[0]==pTeam and TicTacGame.boardNum[1]==pTeam and TicTacGame.boardNum[2]==pTeam or TicTacGame.boardNum[3]==pTeam and TicTacGame.boardNum[4]==pTeam and TicTacGame.boardNum[5]==pTeam or TicTacGame.boardNum[6]==pTeam and TicTacGame.boardNum[7]==pTeam and TicTacGame.boardNum[8]==pTeam or TicTacGame.boardNum[0]==pTeam and TicTacGame.boardNum[3]==pTeam and TicTacGame.boardNum[6]==pTeam or TicTacGame.boardNum[1]==pTeam and TicTacGame.boardNum[4]==pTeam and TicTacGame.boardNum[7]==pTeam or TicTacGame.boardNum[2]==pTeam and TicTacGame.boardNum[5]==pTeam and TicTacGame.boardNum[8]==pTeam or TicTacGame.boardNum[0]==pTeam and TicTacGame.boardNum[4]==pTeam and TicTacGame.boardNum[8]==pTeam or TicTacGame.boardNum[2]==pTeam and TicTacGame.boardNum[4]==pTeam and TicTacGame.boardNum[6]==pTeam:
            return True
        else:
            if all(str(li) in "X,O" for li in TicTacGame.boardNum):
                return False

    def playAgain(self):
        TicTacGame.boardNum=list(range(1,10))
        while True:
            playAgain=input("Are you down for another one ? (Y or N): ").upper()
            if not playAgain=="Y" and not playAgain=="N":
                print("Invalid input: try again (Y or N)")
                continue
            else:
                if playAgain=="Y":
                    self.playGame()
                elif playAgain=="N":
                    break

    def playGame(self):
        self.printBoard()
        print("\nTeams (X or O)")
        p1Name,p1Team,p2Name,p2Team,teams=self.playersTeams()
        print("Player 1: {name} (Team: {team})".format(name=p1Name, team=p1Team))
        print("Player 2: {name} (Team: {team})\n".format(name=p2Name, team=p2Team))
        for inputs in range(0,9):
            if inputs%2==0:
                self.markGameBoard("1",p1Name,p1Team,p2Team,mark=p1Team)
                win=self.chkWin(p1Team)
                if win:
                    print("\nCONGRATULATIONS, {name} Wins".format(name=p1Name))
                    self.playAgain()
                    break
                if win==False:
                    print("\nGame Draw :(")
                    self.playAgain()
                    break
            else:
                self.markGameBoard("2",p2Name,p2Team,p1Team,mark=p2Team)
                win=self.chkWin(p2Team)
                if win:
                    print("\nCONGRATULATIONS, {name} Wins".format(name=p2Name))
                    self.playAgain()
                    break
                if win==False:
                    print("\nGame Draw")
                    self.playAgain()
                    break

startGame=TicTacGame()
