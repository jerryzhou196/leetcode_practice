from typing import List


class Solution:
    def parseWords(self, input_text):
        word = ""
        ans = []
        for i, char in enumerate(input_text):
            if char == " ":
                if word:
                    ans.append(word)
                    word = ""
            elif char == "-":
                if word:
                    ans.append(word + "-")
                elif len(ans) >= 1:
                    ans[len(ans) - 1] += "-"
            elif char.isalnum():
                word += char

        if word:
            ans.append(word)

        print(ans)

        return ans

    def combineSentences(self, sentence, maxWidth, sentence_total):
        spacing = maxWidth - sentence_total
        if len(sentence) == 1:
            for i in range(spacing):
                sentence[0] = sentence[0] + "_" if i % 2 == 0 else "_" + sentence[0]
        else:
            group_size = spacing // (len(sentence) - 1)
            remaining = spacing % (len(sentence) - 1)
            underscore = group_size * "_"
            for i in range(len(sentence) - 1):
                sentence[i] += underscore
            sentence[len(sentence) - 1] += remaining * "_"

        return "".join(sentence)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sentence_total = 0
        sentence = []
        ans = []

        last_word_has_hypen = False

        for word in words:
            if last_word_has_hypen:
                if (len(word) + sentence_total + (len(sentence) - 1)) > maxWidth:
                    ans.append(
                        self.combineSentences(sentence, maxWidth, sentence_total)
                    )
                    sentence_total = len(word)
                    sentence = [word]
                else:
                    sentence_total += len(word)
                    sentence[-1] += word
            else:
                if (len(word) + sentence_total + len(sentence)) > maxWidth:
                    ans.append(
                        self.combineSentences(sentence, maxWidth, sentence_total)
                    )
                    sentence_total = len(word)
                    sentence = [word]
                else:
                    sentence_total += len(word)
                    sentence.append(word)

            last_word_has_hypen = True if word[-1] == "-" else False

        print(sentence)
        ans.append(self.combineSentences(sentence, maxWidth, sentence_total))

        return ans


s = Solution()
print(s.fullJustify(s.parseWords("auto-complete is my go - to"), 8))
print(s.fullJustify(s.parseWords("human!"), 8))
print(s.fullJustify(s.parseWords("cat is an animal and so is a dog"), 12))
print(s.fullJustify(s.parseWords("a cat is an animal"), 6))
