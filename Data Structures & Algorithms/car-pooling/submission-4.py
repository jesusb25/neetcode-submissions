class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # overlap cannot exceed capacity
        if not trips:
            return True
        
        # Create a list of events: (time, passenger_change)
        events = []
        for passengers, start, dest in trips:
            events.append((start, passengers))
            events.append((dest, -passengers))
        
        # Sort events by time; for same time, drop-offs should happen before pick-ups
        events.sort()
        
        current_passengers = 0
        for time, change in events:
            current_passengers += change
            if current_passengers > capacity:
                return False
        
        return True