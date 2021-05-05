#binary addition

#function for converting decimal to binary 
def decimal_to_binary(a):
	temp=[]
	while (a!=0):
		rem=a%2
		a=a//2
		temp.append(rem)
	result=temp[::-1]
	return result

#function of converting binary to decimal
def binary_to_decimal(l):
    result=0
    j=len(l)-1
    for i in l:
        result+=i*pow(2,j)
        j-=1
    return result
    
#function to calculate binary addition
def bianry_addition(a,b):
    carry = 0
    result =[]
    for i in range(len(a)-1, -1, -1):
        r = carry
        r += 1 if a[i] == 1 else 0
        r += 1 if b[i] == 1 else 0
        ele=(1 if r % 2 == 1 else 0)
        result.append(ele)
        carry = 0 if r < 2 else 1
    result=result[::-1]
    if carry != 0:
        result.insert(0,1)
    return result

#main function
def main():
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))

    #getting binary values
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

    #calling function for binary addition
    add=bianry_addition(bin1,bin2)
        
    #printing result
    print("Binary addition:")
    print(num1,"+",num2," is equal")
    print("in binary ---> ",end="")
    for i in add:
            print(i,end="")
    print("")
    print("in decimal ---> ",binary_to_decimal(add))
 
#calling main function
if __name__ == "__main__":
    main()
