class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Lets look at my thought process. They are going to give me the amount of elements they want me to search for. Example being if K = 3 they want me to find the top 3 elements that show up the most. 

        So how I would approach this is i would create a for loop so that it loops through the elements and, I would use a hashmap to count all the elements, and i would add one to the count for every element that shows up. If the element is the same the count would go up higher and higher. At the end of the array I would return what ever K is and return the values from the hashmap.
        obviously at the end of my loop i want to sort the counts into its own thing to count it.
        so i will use the sort function that python give and sort the hashmap (counts) that i have created.
        
        Im going to make a variable named keys, and with this i want to make it assigned to the counts which will be sorted and also i want it from most frequent to least frequent. Im going to use reverse = True for that.
'''

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        keys = sorted(counts, key = counts.get, reverse = True)
        
        return keys[0:k]

        

            

            