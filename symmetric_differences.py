"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
"""
if __name__ == '__main__':
	numbers1 = int(input())
set1 = set(map(int,input().split()))
numbers2 = int(input())
set2 = set(map(int,input().split()))
set3 = set1.difference(set2)
set4= set2.difference(set1)
set5 = set3.union(set4)
for i in sorted(list(set5)):
        print (i)
