"""Write a program to implement Selective Complement logical operation
using bit-wise operators."""

#function for converting decimal to binary 
def decimal_to_binary(a):
	temp=[]
	while (a!=0):
		rem=a%2
		a=a//2
		temp.append(rem)
	result=temp[::-1]
	return result
    
#function for selective complement logical operation 
def sel_comp(a,b):
    temp=[]
    for i in range(len(b)):
            if b[i]==1:
                    if a[i]==1:
                            temp.append(0)
                    else:
                            temp.append(1)
            else:
                    temp.append(a[i])
    return temp
    
#main function 
def main():
    num1=int(input("Enter the A(t) :"))
    num2=int(input("Enter the B :"))
    
    #obtaining binary number 
    bin1=decimal_to_binary(num1)
    bin2=decimal_to_binary(num2)
    
    #maintaing equal number of bits
    max_length=max(len(bin1),len(bin2))
    while len(bin1)!=max_length:
        if len(bin1)!=max_length :
                bin1.insert(0,0)
    while len(bin2)!=max_length:
        if len(bin2)!=max_length:
                bin2.insert(0,0)
    
    #calling function for selective complement logical operation
    temp=sel_comp(bin1,bin2)

    #printing values
    print("Selective Complement logical operation:")
    print("A(t) :",end="")
    for j in bin1:
        print(j,end="")
    print(" ")
    print("B :",end="")
    for j in bin2:
        print(j,end="")
    print(" ")
    print("A(t+1) :",end="")
    for j in temp:
        print(j,end="")
    print("")

#calling main function
if __name__ == "__main__":
    main()
