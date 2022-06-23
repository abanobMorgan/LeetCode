class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])

        maxHeap = [] 
        totalSum = 0 
        for i in range(len(courses)):
            
            heappush(maxHeap,-1*courses[i][0])
            totalSum += courses[i][0]
            
            if totalSum > courses[i][1]:	
            
                totalSum += heappop(maxHeap)

		
        return len(maxHeap)
        
        
