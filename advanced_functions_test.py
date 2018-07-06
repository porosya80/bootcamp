def word_lengths(phrase):
    # return list(map(len, phrase.split()))
    return [len(x) for x in phrase.split()]


def filter_words(word_list, letter):
    return [x for x in l if x[0] == letter]


def concatenate(a, b, c):
    return list(w1+c+w2 for (w1,w2) in zip(a, b))


if __name__ == "__main__":
    print(word_lengths("How long are the words in this phrase"))
    l = ["hello", "are", "cat", "dog", "ham", "hi", "go", "to", "heart"]
    print(filter_words(l, "h"))
    print(concatenate(["A", "B"], ["a", "b"], "-"))
