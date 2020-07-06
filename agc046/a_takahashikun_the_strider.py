X = int(input())
K = 1
while True:
    if X*K %360 ==0:
        print(K)
        break
    K += 1
