#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#	
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Import Module
import random

print """
=====================================
+	Welcome To Tic-Toc-Toi Game 	+
=====================================
			 :-  Created By Bitforestinfo


You Just Need To Enter Number of place,
where you want your mark.

Numbers System Is given below,
 

	1 | 2 | 3
	---------
	4 | 5 | 6
	---------
	7 | 8 | 9

So, let's Start Our Game

"""

#
# list of fields
board = [" " for i in range(1,10)]

# Get Input From Player and process
def get_player_input(board):
	# Get input
	p=int(raw_input("[+] Your Turn! Enter Your Number : "))-1
	# Check Input Field
	if board[p]==" ": 
		board[p] = 'X'
		return True
	else:
		print "[+] Wrong Input! Hahahaha !"
		return

# Print Current Status of Board
def print_current_stuation(board):
	print """
	==================================
	+ This Is Present Status Of Game +
	==================================

	 {} | {} | {}
	 ------------
	 {} | {} | {}
	 ------------
	 {} | {} | {}

	""".format(*board)
	return

# Computer Player
def computer_ai(board):
	empty = []
	# Get List Of Empty Fields
	for n, p in enumerate(board):
		if p == " ":
			empty.append(n)
	# Check, if their is any empty field
	if empty:
		# choice random field
		p=random.choice(empty)
		print "[=] Computer AI Turn[=]"
		board[p] = 'O'
		return True
	# if their is no empty field
	else:
		print "[+] Nothing Left! Game Tie#"
		exit(0)
	return

# Check Games Status
def check_game(board):
	# Get list of empty field
	empty = [i for i in board if i==" "]
	if not empty:
		# If Empty field not found
		print "[+] --- Game Over --- [+]"
	# Situation For Winning This Game
	situation = [
	[0,4,8],
	[0,1,2],
	[3,4,5],
	[6,7,8],
	[0,3,6],
	[1,4,7],
	[2,5,8],
	[2,4,6],
	]
	# Check Situations of game
	for a,b,c in situation:
		if board[a]!=" " and board[a]== board[b] and board[b]==board[c]:
			if board[a]=="O":
				print "[+] hehehe! Loser! \n[+] Computer AI Is Game Winner"
			else:
				print "[+] Good! Good! You Winned This Game"
			exit(0)
	return

# Main Function 
def main():
	# loop for players turn again and again
	while True:
		# loop for taking input from you
		while True:
			a = get_player_input(board)
			if a:
				# if your provide input is valid
				break
		# print current game situation
		print_current_stuation(board)
		# check Game situations
		check_game(board)
		# computer turn
		computer_ai(board)
		# check game situation
		print_current_stuation(board)
		# check game situation
		check_game(board)

# Main Trigger 
if __name__ == '__main__':
	main()