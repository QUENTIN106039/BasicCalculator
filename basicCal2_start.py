# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:40:44 2023

@author: user
"""
import sys, math
IS_DEBUG = True

def bugPrint(_inpStr):
    if IS_DEBUG:
        bugPrint(_inpStr)

if __name__ == '__main__':
    formulaStr = input("Please input a math formula with operator + and -:\n")
    total = 0.0;  #代表總值
    forSize = len(formulaStr)  #輸入字串長度
    if IS_DEBUG:
        bugPrint("forSize = " + str(forSize))
    digitCount = 0  #用來計算運算元的長度
    numberTotal = 0 #用來計算運算元的值
    for r in range(0, forSize): #倒著依序訪問(存取)輸入的string(字串)
        i = forSize-r - 1
        bugPrint(str(i) + "," + str(formulaStr[i]))
        #TODO
        if formulaStr[i]=="+":#如果碰到加號，把總值加上運算元值，並且重新計算運算元值和長度
            total =total +numberTotal
            bugPrint("total:" + str(total))
            digitCount = 0#重新計算運算元值和長度
            numberTotal= 0
            #如果碰到減號，把總值減運算元值，並且重新計算運算元值和長度
        if formulaStr[i] == '-':
            total = total - numberTotal
            bugPrint("total:" + str(total))
            numberTotal=0
            dightCount=0
        #如果碰到數字，運算元長度加一，運算元值加上數字*10^digitCount
    else:
        numberTotal = numberTotal + int(formulaStr[i])*pow(10, dightCount)
        dightCount =  dightCount + 1 
        bugPrint("numTotal:"+ str(numberTotal) + "digitCount:" + str(digitCount))
        #TODO END
    total = total + numberTotal
    print(str(total))
    