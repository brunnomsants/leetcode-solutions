class Solution:
    def reverse(self, x: int) -> int:
        y = [i for i in str(x)]
        if(y[0]=='-'):
            y.pop(0)
        y = list(reversed(y))
        z = int(''.join(y))
        if(-2147483648 < z and z > 2147483648 - 1):
            return 0
        if(x<0):
            return z * -1
        return z
