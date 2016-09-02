names_file = open('p022_names.txt', 'r')
names = []
for line in names_file:
    names += line.split(",")

# run through original list and pick out each entry
# individually and insert into new ordered list
def insertion_sort_alphabetically(words):
    ordered_list = []
    for word in words:
        ordered_list = insert_into_list(word, ordered_list)

def insert_into_list(word, ordered_list):
    index = find_index(word_ordered_list)
    print index
