class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = index2 = -1
        min_distance = len(wordsDict)

        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i

            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))

        return min_distance
