input_word = "poop"
n = len(input_word)


def permute(layer, input_word, ans):
    if layer == n - 1:
        print("".join(input_word))
        ans[0] += 1

    for i in range(layer, n):
        input_word[i], input_word[layer] = input_word[layer], input_word[i]
        permute(layer + 1, input_word, ans)
        input_word[layer], input_word[i] = input_word[i], input_word[layer]


ans = [0]
permute(0, list(input_word), ans)
print(f"total permutations of {input_word} is {ans}")
