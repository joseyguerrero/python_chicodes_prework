# Question 1 - Write a function to print "Hello_USERNAME"
def hello_name(user_name):
    print ("Hello, " + user_name.upper() + "!")

hello_name('Josey')


# Question 2 - Print first odd numbers between 1 and 100
def odd_numbers():
    for i in range(0,101,2):
        print(i)

odd_numbers()

# Question 3 write a function returns the max number in a given list

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))


# Question 4 - Write a FUnction to return if the given year is a leap year

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print (f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')



def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)

is_leap_year(2019)







# Question 5 -  Write a function to check if all numbers in a list are consecutive

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)
