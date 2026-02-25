#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Julian_Date(D, M, Y):
    M = int(M)
    Y = int(Y)
    
    JD= ( 367* Y - 7*(Y+(M+9)// 12)// 4 -3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 +D +1721029 - 0.5)
    return JD
if __name__ == "__main__":
    Y = int(input("Year (Y): "))
    M = int(input(" Month (M): "))
    D = float(input(" Date (D): "))
    
    jd= Julian_Date(D, M, Y)
    print(f"Julian Date = {jd}")

