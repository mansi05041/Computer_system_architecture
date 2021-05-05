#1's complement

#function to calculating 1's complement
def ones_complement(l):
    for i in range(len(l)):
        if int(l[i])==0:
            print(1,end="")
        if int(l[i])==1:
            print(0,end="")
    print("")   
    
#main function
def main():
    num=list(input("Enter the binary number:"))
    for i in num:
            print(i,end="")
    print(": 1's complement ----> ",end="")
    ones_complement(num)

#calling main function
if __name__ == "__main__":
    main()    
