y=1
a=0   
print("Piramide tipo 1,2,3 o 4 : ", end="")
a=int(input())
while a in range(1,5):
    if a==1:
        print("tamaño de la Piramide: ", end="")
        n=int(input())
        while y<= n:
            print (" " *(n-y), "*" * int(2*y-1))  
            y = y+1
    elif a==2:
        print("tamaño de la Piramide: ", end="")
        n=int(input())
        while y<= n:
            print (" " *(n-y), "*" * int(2*y-1)) 
            y = y+1
        y=1  
        while y<=n-1:
            print(" " *y, "*" * int(2*(n-y)-1))
            y=y+1
    elif a==3:
        print("tamaño de la Piramide: ", end="")
        n=int(input())
        while y<= n-1:
            print("*" *y," " *int(2*(n-y)-2),"*" *y)
            y=y+1
        print("*" *int(2*n))
        y=1
        while y<= n-1:
            print("*" *int(n-y), " " *int(2*(y-1)), "*" *int(n-y))
            y=y+1   
    else:
        print("tamaño de la Piramide: ", end="")
        n=int(input())
        while y<=n:
            print(" "*int(y-1), "*" * int(2*(n-y+1)))
            y=y+1
        y=1
        while y<=n-1:
            print(" " * int(n-y-1), "*" *2*(y+1))
            y=y+1
    input()
    exit()
