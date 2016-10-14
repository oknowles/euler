names_file = open('p022_names.txt', 'r')
names = []
for line in names_file:
    names += line.split(",")

def insertion_sort_alphabetically(words):
    ordered_list = []
    for word in words:
        index = binary_search_index(word, ordered_list)
        ordered_list.insert(index, word)
    return ordered_list

def binary_search_index(word, ordered_list):
    tail = 0
    head = len(ordered_list) - 1
    mid = head / 2
    while (head >= tail):
        # print '[h,m,t] = [{},{},{}]'.format(head,mid,tail)
        cur_word = ordered_list[mid]
        if (cur_word < word):
            tail = mid + 1
            mid = tail + (head - tail) / 2
        elif (cur_word > word):
            head = mid - 1
            mid = tail + (head - tail) / 2
        else:
            head = tail
    return mid + abs(head-tail)


def get_char_position(char):
    return ord(char) - 97

def get_score(name, index):


def get_scores(unordered_names):
    ordered_names = insertion_sort_alphabetically(unordered_names)
    scores = [get_score(ordered_names[i], i) for i in range(len(ordered_names))]



# print binary_search_index('z', ['a','b','g'])
print insertion_sort_alphabetically(['sdfdsfg','gha','bdf','z','fdcfg'])
