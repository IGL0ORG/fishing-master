#2
# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 F = (y and(x!=w))and(not(z)or x)
#                 if F ==1:
#                     print(x,y,z,w)


# #5
# n=int(input())

# x=[]
# while n!=0:
#     x.append(n%2)
#     n=n//2

# a=0
# for i in range(len(x)):
#     a+=x[i]
# x.append(a%2)
# a=0
# for i in range(len(x)):
#     a+=x[i]
# x.append(a%2)
# a=''
# for i in range(len(x)):
#     a=a+str(x[i])
# r =(int(a,base=2))
# # print(r)
# s = int(input()) 
# s = s // 10 
# n = 1 
# while s < 51: 
#  s = s + 5 
#  n = n * 2 
# print(n)
#12 
# s = 70 * '8'
# while "2222" in s or "8888" in s:
#   if "2222" in s:
#     s = s.replace( "2222", "88", 1 )
#   else:
#     s = s.replace( "8888", "22", 1 )
# print(s)
#14
# n=(3*(4**38)+2*(4**23)+(4**20)+3*(4**5)+2*(4**4) +1)
# k=0
# while n:
#     if (n%16) == 0:
#         k+=1
#     n=n//16
# print(k)

#16

# def F(n):
#     if n==1:
#         return 1
#     elif n%2==0:
#         return n + F(n-1)
#     elif n%2==1:
#         return 2*F(n-2)
# print(F(26))

# 22

# x = int(input()) 
# Q = 9 
# L = 0 
# while x >= Q: 
#  L = L + 1 
#  x = x - Q 
# M = x 
# if M < L: 
#  M = L 
#  L = x 
# print(L) 
# print(M)

#24

#f=open('24.txt')
#x=[]
#for i in range(len(f)):
 #   x.append(f[i])
#print(x)

# for s in range(1,20):
#   n = 105
#   while n > s:
#     s = s + 3
#     n = n - 2
#   if n==67:
#     print(s)

# for i in range(201,1000):
#     s='1'*i
# while ('1111'in s):
#     s=s.replace('1111', '22',1)
#     s=s.replace('222', '1',1)
#     if s.count('1')==2:
#         print(i)

# filee=open('17-8.txt')
# s=[]
# for i in filee:
#     s.append(int(i))
# maxi=-100000000
# k=0
# for i in range(0,len(s)-1):
#     for b in range(0,len(s)-1):
#         if (abs(s[i]*s[b]))%26==0:
#             k+=1
#             maxi=max(maxi,s[i]+s[+1])
#             print(k,maxi)

# def F(n):
#     if n==1:
#         return 1
#     # elif n==2:
#     #     return 1
#     # elif n==3:
#     #     return 3
#     elif n>=2:
#         return F(n-1)*n
# print(F(6))



# for x in range(-100,1000):
#     start=x
#     a = 7*x+27
#     b = 7*x-33
#     while a!=b:
#         if a>b:
#             a-=b
#         else:
#             b-=a
#     if a==10 :
#         print(start)


# for x in range(0,1000):
#     start=x
#     a = 0
#     b = 0
#     while x>0: 
#         a+=1
#         if (b<(x%8)):
#             b=x%8
#         x//=8
#     if a==3 and b==2:
#         print(start)



s = 1
n = 0
while  2*s*s < 10*s:
    s = s + 1
    n = n + 2
print(n)