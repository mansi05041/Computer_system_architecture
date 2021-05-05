#function for Exclusive OR of the first number by the second bitwise
def exclusive_or_operation(a,b):
    temp=[]
    for i in range(len(a)):
        if a[i]==b[i]:
            temp.append(0)
        else:
            temp.append(1)
    return temp
    
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

#function for AND of the first number by the second bitwise
def bitwise_and_operation(a,b):
    temp=[]
    for i in range(len(a)):
        if a[i]!=b[i]:
            temp.append(0)
        else:
             if a[i]==1:
                temp.append(1)
             else :
                temp.append(0)
    return temp

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
    print("in decimal: ",result)

#function to print list without parenthesis:
def result_binary(l):
    print("in binary: ",end="")
    for i in l:
        print(i,end="")
    print("")
    
#main-function
def main():
    num1=int(input("Enter a decimal number range [0,225] : "))
    num2=int(input("Number of bits to be performed : "))
    temp=0
    
    # checking the conditions
    if (num1 < 0) or (num1 > 255):
            print("Range should be [0,225]")
    if num2 < 0:
            print("invalid bits")  
    else: 
        temp=1
    if temp==0:
        exit()
    bin1=decimal_to_binary(num1)
    bin2=decimal_to_binary(num2)
    
    #code to make both binary number equal size of length
    if len(bin1)!=len(bin2):    
        max_length=max(len(bin1),len(bin2))
        while len(bin1)!=max_length or len(bin2)!=max_length:
                temp=bin1
                if len(bin1)>len(bin2):
                    temp=bin2
                rem_space=max_length-len(temp)
                for i in range(rem_space):
                    if max_length!=len(bin1):
                        bin1.insert(0,0)
                    if max_length!=len(bin2):
                        bin2.insert(0,0)
                        
    #calling the bitwise operations                    
    excl_or=exclusive_or_operation(bin1,bin2)
    bitwise_or=bitwise_or_operation(bin1,bin2)
    bitwise_and=bitwise_and_operation(bin1,bin2)
    
    #printing results
    print(num1,"",end="")
    result_binary(bin1)
    print(num2,"",end="")
    result_binary(bin2)
    print("")
    print("Exclusive OR :")
    result_binary(excl_or)
    binary_to_decimal(excl_or)
    print("")
    print("OR :")
    result_binary(bitwise_or)
    binary_to_decimal(bitwise_or)
    print("")
    print("AND :")
    result_binary(bitwise_and)
    binary_to_decimal(bitwise_and)
    print("")
    
#calling main function
if __name__ == "__main__":
    main()
