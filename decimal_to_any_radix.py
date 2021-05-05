#function of converting 10 to any radix
def decimal_convert_radix(num,b):
    temp=[]
    while (num!=0):
        rem=num%b
        num=num//b
        temp.append(rem)
    result=temp[::-1]
    return result
def main():
    num=int(input("Enter the decimal number:"))
    radix=int(input("enter the base to be converted:"))
    result=decimal_convert_radix(num,radix)
     
    #creating dictonary for the values greater than 9
    alphabet={} 
    val=10
    for i in list(map(chr, range(97, 123))):
        key=i.upper()
        value=val
        val=val+1
        alphabet[key]=value
    print(num,' of base',10,' into base',radix,' is:',end="")
    for i in result:
        if i>9:
            i=list(alphabet.keys())[list(alphabet.values()).index(i)] #replacing the values starting from 10
        print(i,end="")
#calling main function
if __name__ == "__main__":
    main()
