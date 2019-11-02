"""
Task
Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints


Output Format

Output the total number of students who are subscribed to the English newspaper only.
"""
numbers1 = int(input())
set1 = set(map(int,input().split()))
numbers2 = int(input())
set2 = set(map(int,input().split()))
set3 = set1.difference(set2)
length_of_difference_set = len(set3)
print( length_of_difference_set )
