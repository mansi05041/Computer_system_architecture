#function of converting a to base 10 where a is greater than 10
def a_convert_decimal1(num,a,alphabet):
    temp=0
    l=list(num)
    i=len(l)-1
    for j in l:
        test=j.isnumeric()
        if test==False:
            j=j.upper()
            m=alphabet.get(j)  #replacing alphabets to number as according to dictionary
        else:
            m=int(j)
        temp+=m*pow(a,i)
        i-=1
    return temp

#function of converting a to base 10 where a is less than equal to 10
def a_convert_decimal2(num,a):
    temp=0
    i=0
    while (num!=0):
        re=num%10
        temp+=re*pow(a,i)
        num=num//10
        i+=1
    return temp
    
#function of converting 10 to base b
def decimal_convert_b(num,b):
    temp=[]
    while (num!=0):
        rem=num%b
        num=num//b
        temp.append(rem)
    result=temp[::-1]
    return result

#creating dictonary for the values greater than 9
alphabet={} 
val=10
for i in list(map(chr, range(97, 123))):
    key=i.upper()
    value=val
    val=val+1
    alphabet[key]=value

#convert a base to b base
a=int(input("enter the base of number:"))
if a>10:
    num=input("enter the number:") #input for the base greater than 10
else:
    num=int(input("enter the number:"))
b=int(input("enter the base to be converted:"))
if (a>10):
   temp=a_convert_decimal1(num,a,alphabet)
   result=decimal_convert_b(temp,b)
else:
    temp=a_convert_decimal2(num,a)
    result=decimal_convert_b(temp,b)
print(num,' of base',a,' into base',b,' is:',end="")
for i in result:
   if i>9:
       i=list(alphabet.keys())[list(alphabet.values()).index(i)] #replacing the values starting from 10
   print(i,end="")

