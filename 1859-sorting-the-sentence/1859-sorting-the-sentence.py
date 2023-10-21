class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()

        words.sort(key=lambda word: int(word[-1]))

        original_sentence = ' '.join(word[:-1] for word in words)

        return original_sentence
