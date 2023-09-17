from collections import defaultdict


def groupAnagrams(input_strings):
    records = defaultdict(list)
    ans = []

    for word in input_strings:
        word_metadata = [0] * 128
        for letter in word:
            word_metadata[ord(letter)] += 1
        records[tuple(word_metadata)].append(word)

    for key in records:
        sub_ans = []
        for word in records[key]:
            sub_ans.append(records[key][word])
        ans.append(sub_ans)

    return ans
