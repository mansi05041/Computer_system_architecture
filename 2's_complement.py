#2's complement

#function to calculating 2's complement
def twos_complement(l):
    temp=l[::-1]
    beg=[] 
    end=[]

    #finding the first 1
    for i in range(len(temp)):
        ele=int(temp[i])
        if ele==1:
            for m in range(0,i+1):
                end.append(temp[m])
            for m in range(i+1,len(l)):
                beg.append(temp[m])
            break
        
    #reversing the list 
    end=end[::-1]
    beg=beg[::-1]

    #printing the values as desired
    for j in beg:
        if int(j)==1:
            print(0,end="")
        if int(j)==0:
            print(1,end="")
    for k in end:
        print(k,end="")
    print("")
 
#main function
def main():
    num=list(input("Enter the binary number:"))
    for i in num:
            print(i,end="")
    print(": 2's complement ----> ",end="")
    twos_complement(num)

#calling main function
if __name__ == "__main__":
    main()    
