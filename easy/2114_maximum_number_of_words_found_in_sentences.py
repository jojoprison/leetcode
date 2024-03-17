from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        total_words_len = []

        for sentence in sentences:
            total_words_len.append(len(sentence.split(' ')))

        print(max(total_words_len))

    # faster!
    def mostWordsFound_2(self, sentences: List[str]) -> int:
        max_words_len = 0

        for sentence in sentences:
            words_len = len(sentence.split(' '))
            if words_len > max_words_len:
                max_words_len = words_len

        return max_words_len

    def mostWordsFound_3(self, sentences: List[str]) -> int:
        max_words_len = 0

        for sentence in sentences:
            if max_words_len < len(sentence.split(' ')):
                max_words_len = len(sentence.split(' '))

        return max_words_len


if __name__ == '__main__':
    Solution().mostWordsFound(['lol', 'fad', 'lol kk l'])