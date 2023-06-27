t = int(input())
for _ in range (t):
    x,y = map(int,input().split())
    if (y*10< x):
        print("yes")
    else:
        print("no")
