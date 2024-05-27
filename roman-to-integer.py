class Solution:
    def romanToInt(self, s: str) -> int:
        romanvaluelist = list(s)
        result = 0
        lastsum = []
        for i in range(len(romanvaluelist)):
            if(romanvaluelist[i] == "M"):
                result += 1000
                lastsum.append(1000) 
            if(romanvaluelist[i] == "D"):
                result += 500
                lastsum.append(500) 
            if(romanvaluelist[i] == "C"):
                result += 100
                lastsum.append(100) 
            if(romanvaluelist[i] == "L"):
                result += 50
                lastsum.append(50) 
            if(romanvaluelist[i] == "X"):
                result += 10
                lastsum.append(10) 
            if(romanvaluelist[i] == "V"):
                result += 5
                lastsum.append(5)
            if(romanvaluelist[i] == "I"):
                result += 1
                lastsum.append(1) 
            if(lastsum[i-1] < lastsum[i]):
                result -= lastsum[i-1]*2
        return result
    
print(Solution.romanToInt(0, "MCMXCIV"))