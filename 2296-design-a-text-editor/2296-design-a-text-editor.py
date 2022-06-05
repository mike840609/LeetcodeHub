class TextEditor:

    def __init__(self):
        self.s = ''
        self.i = 0 
        

    def addText(self, text: str) -> None:
        self.s = self.s[:self.i] + text + self.s[self.i:]
        self.i += len(text)
        

    def deleteText(self, k: int) -> int:                
        new_i = max(0, self.i - k)
        res = k if self.i - k >= 0 else self.i
        self.s = self.s[:new_i] + self.s[self.i:]
        self.i = new_i
        return res 
        

    def cursorLeft(self, k: int) -> str:
        self.i = max(0, self.i - k)
        start = max(0, self.i-10)
        return self.s[start: self.i]
        

    def cursorRight(self, k: int) -> str:
        self.i = min(len(self.s), self.i+k)
        start = max(0, self.i - 10)
        return self.s[start: self.i]
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)