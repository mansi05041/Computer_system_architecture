#binary subtraction

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

#function for calculating 1's complement
def ones_complement(l):
    for i in range(len(l)):
        if l[i]==0:
            l[i]=1
        else :
            l[i]=0
    return l   
    
#function for calculating 2's complement
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
    
    #implementing 1's complement in beg 
    begn=ones_complement(beg)
    
    #concate the begn and end 
    result=begn+end
    
    return result
    
#function for binary subtraction
def binary_sub(a,b):

    #getting 2's complement for negative number i.e., b
    b_com=twos_complement(b)
    carry = 0
    result =[]
    
    #adding binary bits 
    for i in range(len(a)-1, -1, -1):
        r = carry
        r += 1 if a[i] == 1 else 0
        r += 1 if b_com[i] == 1 else 0
        ele=(1 if r % 2 == 1 else 0)
        result.append(ele)
        carry = 0 if r < 2 else 1
    result=result[::-1]
    if carry!= 0:
        result.insert(0,1)
    
    #checking the number is positive or  negative
    if carry!=1:
        result=twos_complement(result)
    else:
        del result[0]
    
    return result
    
#main function
def main():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    
    #getting binary bits 
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
    
    #getting the result for binary subtraction
    bin_sub=binary_sub(bin1,bin2)
    
    #printing result
    print("binary subtraction")
    print(num1,"-",num2,"is")
    print("in binary ---> ",end="")
    if num1<num2:
            print("-",end="")
    for i in bin_sub:
        print(i,end="")
    print("")
    print("in decimal --->",end="")
    if num1<num2:
        print(" -",binary_to_decimal(bin_sub))
    else:
        print(binary_to_decimal(bin_sub))
        
#calling main function
if __name__ == "__main__":
    main()

    
    
