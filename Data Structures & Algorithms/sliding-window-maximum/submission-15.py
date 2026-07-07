class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() #index
        result = []

        for i in range(len((nums))):
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i + 1 >= k:
                if (i - k) == q[0]:
                    q.popleft()
                result.append(nums[q[0]])
            

        return result