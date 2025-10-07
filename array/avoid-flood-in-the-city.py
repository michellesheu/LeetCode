from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # The final answer array. Initialize with 1s, which will be the default
        # for any unused dry days.
        ans = [1] * len(rains)
        
        # Stores the day a lake became full.
        # Key: lake_number, Value: day_index
        full_lakes = {}
        
        # Stores the indices of available dry days.
        dry_days = []

        for day, lake in enumerate(rains):
            # Case 1: It's a rainy day.
            if lake > 0:
                # A rainy day can't be used to dry, so set it to -1.
                ans[day] = -1
                
                # Check if the lake that's getting rain is already full.
                if lake in full_lakes:
                    # This lake is full! We need to find a dry day to empty it.
                    # The dry day must have occurred *after* the last time it rained.
                    last_rain_day = full_lakes[lake]
                    
                    # Find the earliest dry day available after the last rain day.
                    # bisect_right finds an insertion point which is what we need.
                    # It efficiently finds the first element > last_rain_day.
                    idx = bisect.bisect_right(dry_days, last_rain_day)
                    
                    # If idx is at the end of the list, there are no available
                    # dry days after the last rainfall. A flood is unavoidable.
                    if idx == len(dry_days):
                        return [] # Flood!
                    
                    # We found a suitable dry day to use.
                    dry_day_to_use = dry_days.pop(idx)
                    
                    # Set the answer for that day to dry the current lake.
                    ans[dry_day_to_use] = lake
                    
                    # Update the last rain day for this lake to the current day.
                    full_lakes[lake] = day
                else:
                    # First time raining on this lake, just record it.
                    full_lakes[lake] = day
            
            # Case 2: It's a dry day.
            else:
                # Add the index of this dry day to our list of opportunities.
                dry_days.append(day)
                
        return ans
