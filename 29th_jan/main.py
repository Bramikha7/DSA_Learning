# 1. Given a list of scores, print how many students passed (>= 40).
def count_passed(marks):
    count = 0
    for i in range(len(marks)):
        if marks[i] >= 40:
            count +=1
    print(count)
count_passed([23,3,2,34,43,7,88,7,8,8,8,87,87,85,])
# 2.Given a list of product prices, count how many items cost more than 1000
def count_cost(prizes):
    count = 0
    for i in range(len(prizes)):
        if prizes[i] >= 1000:
            count += 1
    print(count)
count_cost([23453453,45,243535,234545,5,3,55,3,4,43435,53535,343223])
# 3. Given a list of cities, print only the cities whose names have more than 6 letters

def print_len_more_than_6(cities):
    for i in range(len(cities)):
        if len(cities[i]) >= 6:
            print(cities[i])
print_len_more_than_6(["chennai","london","delhi","mumbai","banguluru","pune","Washington DC"])

# Delete Last K Array Elements
# Given 2 inputs arr,,K
# print the array after deleting the last K elements.
# Include validations wherever required.
# Sample Input:
# [10,20,30,40,50] , 3
# Output:
# [10,20]
def delete_k(arr,k):
    result=[]
    for i in range(0,len(arr)-k):
        result.append(arr[i])
    print(result)
delete_k([10,20,30,40,50],1)

# Sum of Consecutive Pairs
# Given an array of numbers, find the sum of the sums obtained by considering all consecutive pairs of adjacent elements.
# Sample Input:
# 1 2 3 4 5
# Sample Output:
# 24
#explanation = (1+2) + (2 + 3) + (3 + 4) + (4 + 5)
def sum_consecutive_pairs(x):
    sum = 0
    for i in range(len(x)-1):
        sum = x[i] + x[i+1] + sum
    print(sum)
sum_consecutive_pairs([1,2,3,4,5])

# Finding the Count of K 
# Given an array nums[]  and a number K , find and print the count of the number K.
# If the number doesn’t exists, you can print -1
# Sample Input:
# nums = [4, 1, 1, 4, 2, 4, 3, 1, 5]
# K = 4
# Sample Output:
# 3
# explanation :
# Here 4 exists -> 3 times
def existance_of_k(arr,k):
    count = 0
    for i in range(len(arr)):
        if arr[i] ==k:
            count+=1
    print(count)
existance_of_k([4, 1, 1, 4, 2, 4, 3, 1, 5],4)

# Finding the Missing Element
# A system maintains a Master List of unique identification numbers for all registered entities. Due to a recent data transfer error, one ID is missing from the Current List—an otherwise identical copy of the Master List.
# You are provided with two lists of positive integers:
# The Master List: A complete list of N unique IDs, unsorted.
# The Current List: A list containing N-1 IDs, with exactly one ID missing.
# Your task is to identify and report the single missing ID number from the Current List.
# Sample Input:
# Master_list = [10,20, 30, 40, 50]
# Current_list = [40, 10, 20, 50]
# Output:
# 30
#explanation:  30 is the missing number in the Current List
def missing_numb(x, y):
    for i in x:
        if i not in y:
            return i
print(missing_numb([10, 20, 30, 40, 50], [40, 10, 20, 50]))

# A spy agency stores encrypted sentences where every word is separated by a random number of spaces.
# To decode the message, first break the sentence into clean words, then reconstruct it with exactly one space between each word.
# Print the corrected message.
# Bonus: Don’t use any inbuilt functions.
# Input:
# "Secret   mission   starts   now"
# Output:
# "Secret mission starts now"
def encrypt_sent(sent):
    words = "qwertyuioplkjhgfdsazxcvbnm"
    result_sent = ""
    for i in range(len(sent)):
        if sent[i] in words:
            result_sent += sent[i]
        else:
            if result_sent != "" and result_sent[-1] != " ":
                result_sent += " "
    return result_sent
print(encrypt_sent("secret   mission   starts   now"))


