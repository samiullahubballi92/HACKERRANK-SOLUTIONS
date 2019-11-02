"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
"""
n_m = input().split()
n_m = map(int, n_m)
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happines = 0
sad = 0 

for i in n:
    if i in A:
        happines += 1
    elif i in B:
        sad += 1

total = happines - sad
print (total)
