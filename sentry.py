from typing import List
import re


class Solution:
    def fullJustify(self, input_text, maxWidth: int) -> List[str]:
        input_text = re.sub(r"\s*-\s*", "-", input_text.strip())
        words = input_text.split(" ")

        print(words)
        res = []
        sentence = []
        sentence_total = 0

        for word in words:
            if (sentence_total + len(sentence) + len(word)) > maxWidth:
                switch = True
                for i in range(maxWidth - sentence_total):
                    if len(sentence) == 1:
                        if switch:
                            sentence[0] = sentence[0] + " "
                            switch = False
                        else:
                            sentence[0] = " " + sentence[0]
                            switch = True
                    else:
                        sentence[i % (len(sentence) - 1)] += " "
                res.append("".join(sentence))

                sentence = [word]
                sentence_total = len(word)
            else:
                sentence.append(word)

        switch = True
        for i in range(maxWidth - sentence_total):
            if len(sentence) == 1:
                if switch:
                    sentence[0] = sentence[0] + " "
                    switch = False
                else:
                    sentence[0] = " " + sentence[0]
                    switch = True
            else:
                sentence[i % (len(sentence) - 1)] += " "
        res.append("".join(sentence))
        return res


s = Solution()
print(s.fullJustify("auto-complete is my go - to", 8))
