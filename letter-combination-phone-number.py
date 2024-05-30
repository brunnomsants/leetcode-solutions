class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digits = list(digits)
        for i in range(len(digits)):
            if(int(digits[i])>9 and int(digits[i])<2):
                return ""
        dic = {}
        dic['2'] = ['a', 'b', 'c']
        dic['3'] = ['d','e','f']
        dic['4'] = ['g','h','i']
        dic['5'] = ['j','k','l']
        dic['6'] = ['m','n','o']
        dic['7'] = ['p','q','r','s']
        dic['8'] = ['t','u','v']
        dic['9'] = ['w','x','y','z']
        result = []
        if(len(digits)==1):
            for i in range(len(dic[digits[0]])):
                result.append(dic[digits[0]][i])
        if(len(digits)==2):   
            for i in range(len(dic[digits[0]])):
                for j in range(len(dic[digits[1]])):
                    result.append(dic[digits[0]][i]+dic[digits[1]][j])      
        if(len(digits)==3):
            for i in range(len(dic[digits[0]])):
                for j in range(len(dic[digits[1]])):
                    for k in range(len(dic[digits[2]])):
                        result.append(dic[digits[0]][i]+dic[digits[1]][j] + dic[digits[2]][k])      
        if(len(digits)==4):
            for i in range(len(dic[digits[0]])):
                for j in range(len(dic[digits[1]])):
                    for k in range(len(dic[digits[2]])):
                        for l in range(len(dic[digits[3]])):
                            result.append(dic[digits[0]][i]+dic[digits[1]][j] + dic[digits[2]][k] + dic[digits[3]][l])                   
        return result