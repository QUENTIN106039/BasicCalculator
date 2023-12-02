# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 02:48:12 2023

@author: user
"""


import sys, math

if __name__ == '__main__':
    
    formulaStr = input("Please input a math formula with only two operands:\n")
           #formulaStr 是輸入的算式，資料型態為字串
    operandsStr = []
    #operandsStr 是個列表，用來儲存兩個運算元
    answerStr = ""
    #answerStr 是用來儲存答案的字串
    
    #你要做的事TODO
 
    #1. 判斷formulaStr中的運算子是+-*/中的哪一個
    if formulaStr.find("+") != -1: 
       operandsStr = formulaStr.split("+")
       print(operandsStr)
       answerStr = str(int(operandsStr[0]) + int(operandsStr[1]))
    if formulaStr.find("-") != -1:
       operandsStr = formulaStr.split("-")
       print(operandsStr)
       answerStr = str(int(operandsStr[0]) - int(operandsStr[1]))
    if formulaStr.find("*") != -1:
          operandsStr = formulaStr.split("*")
          print(operandsStr)
          answerStr = str(int(operandsStr[0]) * int(operandsStr[1]))
    if formulaStr.find("/") != -1:
             operandsStr = formulaStr.split("/")
             print(operandsStr)
             answerStr = str(int(operandsStr[0]) / int(operandsStr[1]))
   # if formulaStr.find ("*"):
            
    #if formulaStr.find ("/"):    
     #2. 根據對應的運算子用string.split(<delimeter>) 來分割運算元並儲存在operandsStr
    #3. 根據運算子對operandsStr中的兩個運算元做計算並儲存在answerStr
    #4. 注意操作時的資料型態，若需要integer 轉 string 可使用int()，若需要string 轉integer 可使用string()

    
    
    
    
    print("result : " + answerStr)
