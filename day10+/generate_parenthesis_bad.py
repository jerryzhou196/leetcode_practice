from dataclasses import dataclass
from copy import copy


@dataclass
class combinationData:
    close_counter: int
    open_counter: int


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = ["("]
        metadata = {"(": combinationData(0, 1)}
        answer = []

        while len(combinations) > 0:
            did_anything = False
            combination = combinations.pop()
            data = metadata.pop(combination)

            if data.open_counter < n:
                combinations.append(combination + "(")
                metadata[combination + "("] = copy(data)
                metadata[combination + "("].open_counter += 1
                did_anything = True

            if data.close_counter < data.open_counter:
                combinations.append(combination + ")")
                metadata[combination + ")"] = copy(data)
                metadata[combination + ")"].close_counter += 1
                did_anything = True

            if not did_anything:
                answer.append(combination)

        return answer
