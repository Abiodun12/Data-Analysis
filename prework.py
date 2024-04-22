# Question 1
def hello_name(user_name):
    print("hello_" + user_name + "!")


# Question 2
def first_odds():
    for num in range(1, 101, 2):
        print(num)


# Question 3
def max_num_in_list(a_list):
    return max(a_list)


# Question 4
def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False


# Question 5
def is_consecutive(a_list):
    return all(a_list[i] == a_list[i - 1] + 1 for i in range(1, len(a_list)))
