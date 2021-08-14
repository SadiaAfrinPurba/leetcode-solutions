"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {employee.id: employee for employee in employees}
        
        total_importance = mapping[id].importance
        
        queue = deque()
        for subordinate in mapping[id].subordinates:
            queue.append(subordinate)
            
        while queue:
            subordinate_employee = mapping[queue.pop()]
            total_importance += subordinate_employee.importance
            queue.extend(subordinate_employee.subordinates)
            
        return total_importance
            