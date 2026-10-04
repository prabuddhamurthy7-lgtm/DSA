class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            result = 0

            while num > 0:
                ld = num % 10
                result = result + ld
                num = num // 10

            num = result

        return num
        