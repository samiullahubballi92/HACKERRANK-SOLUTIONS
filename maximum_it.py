"""
Problem statement
You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and .
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

Constraints





Output Format

Output a single integer denoting the value .

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
"""
def max_sum(l,div):
	b = list()
	for i in range(0,l):
		a = list()
		a.extend(map(int,input().split()))
		b.append(max(a))
	su = 0 
	for j in b:
		su +=j*j
	
	res = su % div

	print ( res )
	return res 	
if __name__ == '__main__':
	n = list(map(int ,input().split()))
	l = n[0]
	div =n[1]

	result = max_sum(l,div)
