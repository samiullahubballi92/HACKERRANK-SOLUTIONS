"""
Problem statement


Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N , the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and , the price of the shoe.

Constraints
0 < X < 10^3
0 < N < 10^3
20 < xi < 100
2 < shoe size < 20

Output Format

Print the amount of money earned by Raghu.

Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
"""


from collections import Counter
if __name__ == '__main__':
    number_of_shoes = int(input())
    list_of_shoe_size = map(int,input().split())
    number_of_customer = int(input())
    size_and_price_of_shoe = map(tuple,(map(int,input().split()) for _ in range(number_of_customer)))
    n = Counter(list_of_shoe_size)
    p =0
    for i in size_and_price_of_shoe:
        if i[0] in n.keys() and n[i[0]] >0 :
            n[i[0]] = n[i[0]]-1
            p = p+i[1]
          
    print(p)
