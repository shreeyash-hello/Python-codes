#  Given 2 sets of integers,M and N, print their symmetric difference in ascending order. 
#  The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
#  sample input
#  The first line of input contains an integer, M .
#  The second line contains M space-separated integers.
#  The third line contains an integer,N .
#  The fourth line contains N space-separated integers.


m=int(input())
inp1=map(int,input().split())

n=int(input())
inp2=map(int,input().split())

set1=set(inp1)
set2=set(inp2)

a=set1.difference(set2)
b=set2.difference(set1)

final_set=set()
final_set.update(a)
final_set.update(b)

s=list(final_set)
s.sort()

for i in range(len(s)):
    print(s[i])
