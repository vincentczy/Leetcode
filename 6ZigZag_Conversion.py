class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        length = len(s)
        result = ""
        times = 0
        period = 2 * (numRows - 1)
        # first line
        while times * period < length:
            result += s[times * period]
            times += 1
        # middle lines
        for j in range(1, numRows-1):
            times = 0
            while times * period + j < length:
                index = times * period + j
                if index >= length: break
                result = result + s[index]
                index = (times + 1) * period - j
                if index >= length: 
                    times += 1
                    continue
                result = result + s[(times + 1) * period - j]
                times += 1
        # last line
        times = 0
        while times * period + numRows - 1 < length:
            result += s[times * period + numRows - 1]
            times += 1
        return result