#Pre-work Grove:Rangers-75

#Task 3 Question 1

def hello_name(user_name):
    ### Print a simple greeting ###
   
    print (f"Hello_{user_name.upper()}!")
 
hello_name("friend")

#Task 3 Question 2

#Print first 100 odd numbers in Python    
### using a variable to set the range ###  

list_max = 200
a_list = [x for x in range(list_max) if x %2 != 0]
print(a_list)

# Task 3 Question 3

def max_num_in_list(a_list):
    ### To return the maximum number in a list ###
    ### a_list created in task 2 ###

    return {max(a_list)}

print(max_num_in_list(a_list))

# Task 3 Question 4

def is_leap_year(a_year):

    ### Test if a specific year is a leap year with Boolean type output ###
 
    if a_year > 0: 
        if a_year % 4 == 0:
            if a_year % 100 == 0:
                if a_year % 400 == 0:
                    return True
                return False
            return True
        return False
    return False

print(is_leap_year(2028))

# Task 3 Question 5

def is_consecutive(a_list):
    ### Check to see if a list of numbers is consecutive ###
    ### list(range) function creates a list of numbers###
    ### compare created list to input list ###
    ### a_list created in task 2 ###

    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

print(is_consecutive(a_list))

