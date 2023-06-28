# Python Optional Code Challenge Question 1
# Codecademy, Learn Python 3, Module 1 "Modulo"
# 6/27/2023
# Jovanay Carter

# Instructions: You're trying to divide a group onto four teams. All of you count off.
    # Person 1 goes to team 1
    # Person 2 goes to team 2
    # Person 3 goes to team 3
    # Person 4 goes to team 4, and so forth
    # You're number 27, out of a total of 28. 
    ###
    # Write an algorithm that determines separates the group of 28 into 4 groups and prints who's in what group
    # Print what team you are on, if you are number 27 in line, as well as the team of the person at 14 and 23.


## Challenge Question ##

#Defining Variables for the Group
people = 28;
teams = 4;
count = 1; #starting count off number

#Creating List Holders
list_team_1 = [];
list_team_2 = [];
list_team_3 = [];
list_team_4 = [];

#Conditional to break people into groups
while count <= people: 
    # if the remainder after division is 1, them put into team 1; then increase count number by 1; then repeat for 4 groups
    if (count % teams) == 1: 
        list_team_1.append(count)
        count += 1
    elif (count % teams) == 2:
        list_team_2.append(count)
        count += 1
    elif (count % teams) == 3:
        list_team_3.append(count)
        count += 1
    elif (count % teams) == 0:
        list_team_4.append(count)
        count += 1

#print results after lists are created in entirity
print ("List 1:", list_team_1)
print ("List 2:", list_team_2)
print ("List 3:", list_team_3)
print ("List 4:", list_team_4)


#get your team
# my_team = 27 % 4
# print ("My team:", my_team)


