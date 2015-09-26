#!/usr/bin/env python3.4
#
#  2015/09/25 13:43:29
#
import sys

def isprime(n):
   if type(n)!=int or n in {-1, 0, 1}: return False
   if abs(n)==2: return True
   divisors = list(range(3,int(abs(n)**0.5+1),2))
   divisors.insert(0,2)
   count = 1
   for num in divisors:
      if n%num==0:
         count+=1
   return count==1

def make_1d_list(lst):
   new=[]
   for inside_list in lst:
      for elem in inside_list:
         new.append(elem)
   return new

if __name__=="__main__":
   if len(sys.argv)!=2:
      sys.exit(-1)
   n=int(sys.argv[1])
   if isprime(n):
      print("%d é primo" %n)
   else:
      print("%d não é primo" %n)
