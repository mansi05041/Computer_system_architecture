#5 bit binary up counter

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
    print("in decimal ---->",result)

#function of binary addition 
def binary_addition(l,m):
        print("Binary counter up")
        temp=1
        a = [0,0,0,0,1]
        while (m<32):
                carry = 0
                result =[]
                print(temp,"counter up")
                temp+=1
                for i in range(4, -1, -1):
                        r = carry
                        r += 1 if l[i] == 1 else 0
                        r += 1 if a[i] == 1 else 0
                        ele=(1 if r % 2 == 1 else 0)
                        result.append(ele)
                        carry = 0 if r < 2 else 1
                result=result[::-1]
                if carry != 0:
                        result.insert(0,1)
                m+=1
                for i in result:
                    print(i,end="")
                print("")
                binary_to_decimal(result)
                l=result
#main-function
def main():
    num=int(input("Enter the decimal number :"))
    if num>=0 and num<32 :
        binary=decimal_to_binary(num)
        while len(binary)!=5:
            binary.insert(0,0)
        binary_addition(binary,num)
        
#calling main function
if __name__ == "__main__":
    main()

        
    
