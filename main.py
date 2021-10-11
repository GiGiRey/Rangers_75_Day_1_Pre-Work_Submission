def hello_name(user_name):
    ### Print a simple greeting ###
   
    print (f"Hello_{user_name.upper()}!")
 
# hello_name("friend")

def first_100():
    numbers = list(range(0,201))
    for number in numbers:
        if number % 2 != 0:
            print(number)

# first_100()

def max_num(a_list):

    max_value = max(a_list)
    return (max_value)

print (max_num([2,3,5,8,9]))

def is_consecutive(a_list):

    i = 0
    status = True

    while i < len(a_list)-1:
        if a_list[i] + 1 == a_list[i+1]:
            i+=1
        else:
            status = False
            break
    print(status)

is_consecutive([1,2,3,4,5,7])
is_consecutive([1,2,3,4,5,6])