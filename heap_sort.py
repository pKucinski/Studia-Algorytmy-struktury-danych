def last_parent(all_wordss):
    n = len(all_wordss)

    if n == 3:
        last_parent = 1

    elif (n % 2) == 0:
        last_parent = (n - 2) / 2

    else:
        last_parent = (n - 1) / 2


    last_parent = int(last_parent)
    return last_parent



def max_heap(all_wordss):
    for i in range(last_parent(all_wordss), -1, -1):
        try:
            if all_wordss[2 * i] > all_wordss[2 * i + 1]:
                if all_wordss[2 * i] > all_wordss[i]:
                    temporary = all_wordss[i]
                    all_wordss[i] = all_wordss[2 * i]
                    all_wordss[2 * i] = temporary
            else:
                if all_wordss[2 * i + 1] > all_wordss[i]:
                    temporary = all_wordss[i]
                    all_wordss[i] = all_wordss[2 * i + 1]
                    all_wordss[2 * i + 1] = temporary

        except IndexError:

            if all_wordss[2 * i] > all_wordss[i]:
                temporary = all_wordss[i]
                all_wordss[i] = all_wordss[2 * i]
                all_wordss[2 * i] = temporary\


def min_heap(all_wordss):
    if last_parent(all_wordss) == 0 and len(all_wordss) == 2:
        if all_wordss[0] < all_wordss[1]:
            temporary = all_wordss[0]
            all_wordss[0] = all_wordss[1]
            all_wordss[1] = temporary

    if last_parent(all_wordss) == 1:
        if all_wordss[0] < all_wordss[1]:
            temporary = all_wordss[0]
            all_wordss[0] = all_wordss[1]
            all_wordss[1] = temporary

    for i in range(0, last_parent(all_wordss)):
        if all_wordss[2 * i + 1] > all_wordss[2 * i + 2]:
            if all_wordss[2 * i + 1] > all_wordss[i]:
                temporary = all_wordss[i]
                all_wordss[i] = all_wordss[2 * i + 1]
                all_wordss[2 * i + 1] = temporary
                return min_heap(all_wordss)
        else:
            if all_wordss[2 * i + 2] > all_wordss[i]:
                temporary = all_wordss[i]
                all_wordss[i] = all_wordss[2 * i + 2]
                all_wordss[2 * i + 2] = temporary
                return min_heap(all_wordss)

    return all_wordss

def sort(all_wordss):
    max_heap(all_wordss)

    final_sort = []

    all_wordss[0], all_wordss[-1] = all_wordss[-1], all_wordss[0]
    final_sort.append(all_wordss[-1])
    all_wordss.pop(-1)

    for i in range(0, len(all_wordss)):
        min_heap(all_wordss)
        all_wordss[0], all_wordss[-1] = all_wordss[-1], all_wordss[0]

        final_sort.append(all_wordss[-1])
        all_wordss.pop(-1)

    final_sort.reverse()

    for word in final_sort:
        print(word,end = ' ')

    return final_sort


if __name__ == '__main__':
    all_words = input()
    all_words = all_words.split()

    final_sort = sort(all_words)




