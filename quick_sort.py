def quick_sort(all_words):
    n = len(all_words)

    if n <= 1:
        return all_words

    position = 0

    for i in range(1, n):
        if all_words[i] <= all_words[0]:
            position += 1
            all_words[i], all_words[position] = all_words[position], all_words[i]

    all_words[0], all_words[position] = all_words[position], all_words[0]

    left = quick_sort(all_words[0:position])
    right = quick_sort(all_words[position + 1:n])

    all_words = left + [all_words[position]] + right

    return all_words


if __name__ == '__main__':
    all_words = input()
    all_words = all_words.split()

    all_words = quick_sort(all_words)

    for word in all_words:
        print(word, end=' ')