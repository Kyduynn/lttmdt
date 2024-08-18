# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:16:43 2024

@author: Student
"""

distance = float(input("Nhập điểm trung bình (GDA) từ bàn phím:"))
 
if distance < 3.5:
    print("Học lực kém")
elif distance <= 3.5 and distance < 5.0:
    print("Học lực yếu")
elif distance <= 5.0 and distance < 7.0:
    print("Học lực Trung Bình")
elif distance <= 7.0 and distance < 8.0:
    print("Học lực Khá")
elif distance <= 8.0 and distance < 9.0:
    print("Học lực Giỏi")
elif distance <= 9.0 and distance <= 10:
    print("Học lực Xuất Sắc")