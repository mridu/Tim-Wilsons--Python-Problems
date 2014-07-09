import random
import string

def choose_computer():
	valid = ["r","p","s"]
	return random.choice(valid)

def choose_human():
	human = string.lower(raw_input("\nChoose (R)ock, (P)aper, or (S)cissors? "))
	valid = ["r","p","s"]
	while human not in valid:
		print "Incorrect choice!, please try again."
		human = string.lower(raw_input("\nChoose (R)ock, (P)aper, or (S)cissors? "))
	return human
	
def win(choice_human, choice_computer, human_name):
	win_computer = "Computer Wins!"
	win_human = human_name + " Wins!"
	windict = {
		'rp' : win_computer,
		'rs' : win_human,
		'pr' : win_human,
		'ps' : win_computer,
		'sr' : win_computer,
		'sp' : win_human
	}
	key = choice_human + choice_computer
	return windict[key]
	
print "\nWelcome to Rock, Paper, Scissors!\n"
point = int(raw_input("How many points are required for a win? "))
name = raw_input("\nWhat is your name? ")
comp_point = 0
human_point = 0
opt_dict = {
	"r":"Rock",
	"p":"Paper",
	"s":"Scissors"
}

while comp_point < point and human_point < point:
	print "point=%d,h=%d,c=%d"%(point,human_point,comp_point)
	human_choice = choose_human()
	comp_choice = choose_computer()
	
	print "%s: %s\tComputer: %s\t" %(name,opt_dict[human_choice],opt_dict[comp_choice])
	
	if human_choice == comp_choice:
		print "It's a draw."
	else:
		winner = win(human_choice, comp_choice, name)
		print winner
		if winner == "Computer Wins!":
			comp_point += 1
		else:
			human_point += 1

print "\nFinal Score: %s  %d\tComputer  %d" %(name,human_point,comp_point)