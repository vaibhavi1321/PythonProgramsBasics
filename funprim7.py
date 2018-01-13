#A simple program for checking if given number is prime or not using python
def prim1(user):
        prime=True
        for i in range(2,user):
                if (user%i)==0:
                        prime=False
                        print("not a prime")
        if prime:
                print("prime number")
                
prim1(input("enter numbers="))
