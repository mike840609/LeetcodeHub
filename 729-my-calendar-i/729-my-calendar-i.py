class MyCalendar:

    def __init__(self):
        self.arr = [] 

    def book(self, start: int, end: int) -> bool:
        idx1 = bisect.bisect_right(self.arr, start)
        idx2 = bisect.bisect_left(self.arr, end)
        
        if idx1 == idx2 and idx1%2 == 0:
            self.arr.insert(idx1, start)
            self.arr.insert(idx2+1, end)
            return True
        return False
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)