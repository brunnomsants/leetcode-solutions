class Solution:
    def myAtoi(self, s: str) -> int:
        listn = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if(s==""):
            return 0
        if(len(s)==1 and s not in listn):
            return 0
        x = list(s)
        y=""
        count=0
        if((s[0] not in listn) and s[0]!=" " and s[0]!="-" and s[0]!="+"):
            return 0
        for i in range(len(x)):
            if(x[i] in alphabet):
                break
            if(x[i] =="+" and x[i-1]!= " " and x[0]!= "+"):
                break
            if(x[i] =="-" and x[i-1]!= " " and x[0]!= "-"):
                break
            if(x[i] not in listn and count>=1):
                break
            if(x[i] in listn or x[i]=="+" or x[i]=="-"):
                if(x[i] in listn):
                    y+=x[i]
                count+=1
        if(y==""):
            return 0
        z = int(y)
        minus = "-"+y
        if(minus in s):
            z=  z*-1
        if(-2147483648 > z ):
            return -2147483648
        if(z > 2147483648 - 1):
            return 2147483648 - 1
        return z