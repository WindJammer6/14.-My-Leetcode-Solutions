class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort()

        conference_rooms = []

        for i in range(len(intervals)):
            added_room = False
            
            for room in conference_rooms:
                if intervals[i][0] >= room[-1][1]:
                    room.append(intervals[i])
                    added_room = True 
                    break
            
            if added_room == False:
                conference_rooms.append([intervals[i]])

            # print(conference_rooms)

        return len(conference_rooms)
                    

solution = Solution()
print(solution.minMeetingRooms([[0,30],[5,10],[15,20]]))                                                    # 2
print(solution.minMeetingRooms([[7,10],[2,4]]))                                                             # 1
print(solution.minMeetingRooms([[13,15],[1,13]]))                                                           # 1
print(solution.minMeetingRooms([[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]]))     # 4