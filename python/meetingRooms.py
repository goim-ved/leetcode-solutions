class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
def meetingRooms(intervals: list[Interval]) -> bool:
    intervals.sort(key=lambda i: i.start)
    for i in range(len(intervals) - 1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True