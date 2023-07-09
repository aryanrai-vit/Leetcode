class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            letter = chr(columnNumber % 26 + ord('A'))
            title = letter + title
            columnNumber //= 26
        return title