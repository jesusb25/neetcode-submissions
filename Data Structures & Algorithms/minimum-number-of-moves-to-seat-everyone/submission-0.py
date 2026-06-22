class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        heapq.heapify(seats)
        heapq.heapify(students)

        res = 0

        while seats:
            seat = heapq.heappop(seats)
            student = heapq.heappop(students)
            res += abs(student - seat)
        return res