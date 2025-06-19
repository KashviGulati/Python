# x= (int(input("Enter value of x: ")))
# y= (int(input("Enter value of y: ")))
# for i in range(0,10):
#     if(x==y):
#         print("They are equal")
#     else:
# 	    print("They are unequal")


# for i in range(1,11):
#     if(i%2!=0):
#         print(i)


# n= int(input("Enter a number: "))
# for i in range(1,n,2): 
#     print(i)


# for i in range(1,11):
#     print("7 *", i, "=", 7*i)

# fact=1
# for i in range(1,6):
#     fact= fact*i
# print(fact)

#Factorial of a number
# n= int(input("Enter a number: "))
# fact=1
# i=1
# while(i<=n):
#     fact= fact*i
#     i=i+1
# print(fact)


#Reverse of a number
# n= int(input("Enter a number"))
# r=0
# while(n>0):
#     rem= n%10
#     r= r*10+rem
#     n= n//10
# print(r)


# n= int(int(input("Enter a number: ")))
# i=1
# while(i<=n):
#     i=i+1
#     if(i==5):
#         continue #skips to the next value
#     print(i)


# p=1
# for i in range(1,11):
#     p=p*i
    
# print(p)


#To print the sum of first n natural numbers
# n= int(input("Enter a number"))
# s=0
# for i in range(1, n+1):
#     s=s+i
# print(s)


#To print the product of first n natural numbers
# n= int(input("Enter a number"))
# p=1
# for i in range(1,n+1):
#     p=p*i
# print(p)



# fruits= ['apple','mango','cherry']
# for i in fruits:
#     print(i)


# a= [10, 20, 30, 40, 50]
# print(a[0]) #to access the first element
# print(a[-1]) #to access the last element

# a=[] #initialising an empty list

# a.append(10) #adding elements to it
# print("After adding 10: ", a)
# a.append(20)
# print("After adding 20: ", a)
# a.append(30)
# print("After adding 30: ", a)

# a.insert(1,45)
# print("After inserting: ", a)

# a.extend([15, 35, 50])#adds multiple elememts at the end of the list
# print("After extending: ", a)


# a= []
# a.append(10)
# a.append(20)
# a.extend([15,25])
# print("First element: ", a[0])
# print("Last element: ", a[-1])


# t= ("apple","cherry", "mango")
# print(t[0])
# print(len(t))
# print(type(t))
# t= ("apple",)
# print(type(t))




# a= ["apple", "mango", "cherry", "orange"]
# a.reverse() 
# print(a)


# a=["apple", "mango", "cherry", "orange"]
# print(a.index("cherry"))
# print(len(a))


# a= [34, 54, 16, 8,76, 64]
# a.sort()
# print(a)


# a= [1, 6, 7, 6, 8, 9, 6]
# print(a.count(6))


# a=[12, 45, 54, 38, 76]
# a.append(15)
# a.insert(3, 59)
# a.remove(45)
# print(a)


# list= [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(list)): #i- index
#     if (i%2==0):
#         print(list[i]) #element-list[i]


# list1= [6,7,8,9]
# print(list1*2) #repetition
# list1*=2 #list1= list*2
# print(list1)

#WRITE A PROGRAM TO READ ALIST OF N INTEGERS AND FIND THEIR AVERAGE

# n= int(input("Enter a number"))
# s=0
# for i in range (0,n+1):
#     s=s+i
# avg= s/n
# print(avg)



# num=[12, 46, 87, 34, 9, 76]
# num.sort(reverse=True)
# print(num[0])
# print(num[1])



# dict1={'a': 10, 'b': 23, 'c': 56, 'd': 8}
# dict1.sorted(reverse=True)
# print(dict[0])



# l= ['Aman', 'A-36', [56, 88, 99, 72, 69], 72.9]
# print(l[3])
# print(l[2][4])
# print(max(l[2]))
# print(l[1])
# l[0]="Ravi"
# print(l)



# n= int(input())
# if(n%3==0):
#     print("Fizz")
# elif(n%5==0):
#     print("Buzz")
# elif(n%3==0 and n%5==0):
#     print("Fizz BUzz")
# else:
#     print("Invalid")


sum=0
for i in range(1, 51):
    if(i%2!=0):
        sum=sum+i
print(sum)


n= int(input())
product=1
for i in range(1, n+1):
    if(n%2!=0):
        product=product*i
print(product)


