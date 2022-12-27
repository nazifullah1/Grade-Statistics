# Write your solution here
import math
def user_input():
    my_list = []
    leas_than_10 = 0
    total1 = 0
    total2 = 0
    total_total = 0
    while True:
        my_input = input("Exam points and exercises completed: ")
        if(my_input == ""):
            break
        splite_input = my_input.split()
        splite_points = int(splite_input[0])
        excercise = int(splite_input[1])
        if(splite_points<10):
            leas_than_10+=splite_points
            excercise_point = math.floor(excercise * 10 /100)
            total1+=leas_than_10
            total1+=excercise_point
            total_total+=total1
            leas_than_10 = 0
            my_list.append(leas_than_10)
            leas_than_10 = 0
        else:
            excercise_point = math.floor(excercise * 10 /100)
            total2+=splite_points
            total2+=excercise_point
            total_total+=total2
            my_list.append(total2)
            total2 = 0
    average = total_total/len(my_list)
    my_list.insert(0, average)
    return my_list

def calculate_statistics(my_list: list):
    passing  = 0
    star_0 = 0
    star_1 = 0
    star_2 = 0
    star_3 = 0
    star_4 = 0
    star_5 = 0
    for i in range(1, len(my_list)):
        if(my_list[i]>=15):
            passing+=1
    print("Statistics:")
    average = my_list[0]
    my_passing = passing/(len(my_list)-1)*100
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {my_passing:.1f}")
    print("Grade distribution:")
    for points in range(1, len(my_list)):
        if(my_list[points]>=28 and my_list[points]<=30):
            star_5+=1
        elif (my_list[points] >=24 and my_list[points]<=27):
            star_4+=1
        elif (my_list[points]>=21 and my_list[points]<=23):
            star_3+=1
        elif (my_list[points] >=18 and my_list[points]<=20):
            star_2+=1
        elif (my_list[points]>=15 and my_list[points]<=17):
            star_1+=1
        elif (my_list[points]>=0 and my_list[points]<= 14):
            star_0+=1
    if(star_5>0):
        print("5: " + "*"*star_5)
    else:
        print("5: ")
    if(star_4>0):
        print("4: "+ "*"*star_4)
    else:
        print("4: ")
    if(star_3>0):
        print("3: " + "*"*star_3)
    else:
        print("3: ")
    if(star_2>0):
        print("2: "+ "*"*star_2)
    else:
        print("2: ")
    if(star_1>0):
        print("1: "+ "*"*star_1)
    else:
        print("1: ")
    if(star_0>0):
        print("0: " + "*"* star_0)
    else:
        print("0: ")

my_list1 = user_input()
calculate_statistics(my_list1)