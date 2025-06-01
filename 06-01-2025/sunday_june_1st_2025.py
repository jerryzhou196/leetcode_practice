from typing import *


class Codec:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s))
            ans += "/"
            ans += s
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            word = length = ""
            while s[i] != "/":
                length += s[i]
                i += 1

            i += 1
            for _ in range(int(length)):
                word += s[i]
                i += 1

            ans.append(word)

        return ans


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode(["5"])))
