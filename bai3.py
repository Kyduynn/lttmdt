# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:16:54 2024

@author: Student
"""
import math

print("Nhập 3 kích thước xem có phải tam giác không?")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a==b==c:
    print("Đây là tam giác đều! ")
elif a==b and a==c and b==c:
         print("Đây là tam giác cân")
 elif a**2 == b**2 + c**2 and b**2 = a**2 + c**2 and c**2 = b**2 = a**2:
         print("Đây là tam giác vuông! ")
        if a==b and a==c and b==c:
            print("Đây là tam giác vuông cân! ")
else:
    print("a,b,c không là 3 cạnh của một tam giác")
         
     