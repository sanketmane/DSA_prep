from heapq import heappush, heappop, heapify
from functools import cmp_to_key

"""
This is Leetcode minimum meeting rooms II problem(Medium level)
We will solve this problem using Heaps.
Solution is also nicely explained here: https://www.youtube.com/watch?v=NKf1OJhEZj0
Idea is to sort the intervals array based on start time.
We will then maintain a heap that contains end time of the meeting.
If at any time, a new meeting which overlaps with existing meeting comes, we will add it heap which denotes that a new meeting room is being assigned for that meeting.
If the previous meeting is over, the associated meeting room is assigned to a new meeting by removing previous meeting from the heap and adding the end time for the new meeeting.
Whatver stays in the heap is count of meetings.
"""

def compare(v1, v2):
    a = v1[0]
    b = v2[0]
    if a < b:
        return -1
    else:
        return 1

def min_meeting_rooms(intervals):
        # Write your code here
        intervals = sorted(intervals, key=cmp_to_key(compare))
        n = len(intervals)
        heap = []
        heapify(heap)
        heappush(heap, intervals[0][1])
        for i in range(1, n):
            if intervals[i][0] < heap[0]:
                heappush(heap, intervals[i][1])
            else:
                heappop(heap)
                heappush(heap, intervals[i][1])
        return len(heap)

# intervals = [(0,30),(5,10),(15,20)]
intervals = [(2,7)]
ans = min_meeting_rooms(intervals)
print(ans)
