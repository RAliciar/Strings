# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Ned_1 = "Ruud Gullit"
Ned_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = Ned_1 + " " + str(goal_0) + ", " + Ned_2 + " " + str(goal_1) 
print (scorers)
report = f"{Ned_1} scored in the {goal_0}nd minute\n{Ned_2} scored in the {goal_1}th minute" 
print (report)
player = "Frank Rijkaard"
first_name = player[0:5]
print (first_name)
last_name_len = len(player[6:14])
print (last_name_len)
name_short = player[0]+"."+ " " + player[6:14]
print(name_short)
chant = (first_name + "! " ) *(len(first_name)-1)+(first_name + "!")
print (chant)
good_chant = chant[-1]!=" "
print(good_chant)
