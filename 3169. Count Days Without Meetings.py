class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort(key=lambda x: x[0])
        merged =[]

        for start,end in meetings:
            if not merged or start > merged[-1][-1]:
                merged.append([start,end])
            else:
                merged[-1][-1] = max(merged[-1][-1],end)

        available_days = 0 

        if merged[0][0]>1:
            available_days += merged[0][0] - 1
        for i in range (1,len(merged)):
            gap = merged [i][0] - merged [i-1][1]-1
            if gap>0:
                available_days+=gap

        if merged[-1][1] < days:
            available_days += days - merged[-1][1]


        return available_days
