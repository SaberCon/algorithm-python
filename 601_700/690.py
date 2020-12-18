# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importances = {employee.id: (employee.importance, employee.subordinates) for employee in employees}

        def get_value(id):
            importance, subordinates = importances[id]
            return importance + sum(get_value(sid) for sid in subordinates)

        return get_value(id)
