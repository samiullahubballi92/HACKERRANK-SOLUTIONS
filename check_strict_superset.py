"""
problem statement
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.

Input Format

The first line contains the space separated elements of set .
The second line contains integer , the number of other sets.
The next  lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set  is a strict superset of all other  sets. Otherwise, print False.
"""


#solution

def is_strict_superset(super_set, sub_set):
    if len(super_set) > len(sub_set) and super_set.issuperset(sub_set):
        return True
    else:
        return False


def check_strict_superset():
    super_set_a = set(list(input().lstrip().rstrip().split()))
    num_of_sets = int(input())
    result = True
    for i in range(num_of_sets):
        set_b = set(list(input().lstrip().rstrip().split()))
        result = result and is_strict_superset(super_set_a, set_b)
    print(result)
    return 0

if __name__ == '__main__':
    check_strict_superset()
