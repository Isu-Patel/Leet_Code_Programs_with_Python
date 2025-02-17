class Solution:
    def reverse(self, x: int) -> int:
        reversenum = 0
        temp = abs(x)
        while temp:
            reversenum = reversenum * 10 + temp % 10
            temp //= 10
        reversenum = reversenum if x > 0 else -(reversenum)
        if reversenum < -2**31 or reversenum > 2**31 - 1:
            return 0
        else:
            return reversenum
