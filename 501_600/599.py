class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {item: i for i, item in enumerate(list1)}
        commons = {item: i + dict1[item] for i, item in enumerate(list2) if item in dict1}
        least = min(commons.values())
        return [item for item, i in commons.items() if i == least]
