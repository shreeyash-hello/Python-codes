n=int(input())
roll1=set(map(int,input().split()))

n2=int(input())
roll2=set(map(int,input().split()))

union=roll1.union(roll2)

print(len(union))
