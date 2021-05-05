#Write a program to implement Selective Set logical operation using bit-wise operators.

#function for converting decimal to binary 
def decimal_to_binary(a):
	temp=[]
	while (a!=0):
		rem=a%2
		a=a//2
		temp.append(rem)
	result=temp[::-1]
	return result

#function for OR of the first number by the second bitwise
def bitwise_or_operation(a,b):
    temp=[]
    for i in range(len(a)):
        if a[i]!=b[i]:
            temp.append(1)
        else:
            if a[i]==1:
                temp.append(1)
            else :
                temp.append(0)
    return temp
    
# main function 
def main():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    
    #converting decimal number to binary 
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
    
    #calling bitwise OR operation
    selective_set=bitwise_or_operation(bin1,bin2)
    
    #printing result
    print("Selective set logical operation ")
    print("A(t):",end="")
    for i in bin1:
        print(i,end="")
    print("")
    print("B:",end="")
    for i in bin2:
        print(i,end="")
    print("")
    print("A(t+1):",end="")
    for i in selective_set:
        print(i,end="")
    
#calling main function
if __name__ == "__main__":
    main()

