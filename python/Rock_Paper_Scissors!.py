def rps(p1, p2):
    if p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == p2:
        return "Draw!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    
#We use a if statement block to check the users choices with eachother and return the winner based on rules of,
#the game however if both inputs are the same it will result in a draw


#####TASK#######

#Rock Paper Scissors
#Let's play! You have to return which player won! In case of a draw return Draw!.

#Examples(Input1, Input2 --> Output):
#"scissors", "paper" --> "Player 1 won!"
#"scissors", "rock" --> "Player 2 won!"
#"paper", "paper" --> "Draw!"
