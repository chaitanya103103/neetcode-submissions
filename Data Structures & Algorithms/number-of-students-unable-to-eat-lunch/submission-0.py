class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = sandwiches[::-1]   

        p = 0
        while queue and stack and p < len(queue):
            cur = queue[0]
            if cur == stack[-1]:
                stack.pop()
                queue.popleft()
                p = 0  
            else:
                queue.append(queue.popleft())
                p += 1

        return len(queue)