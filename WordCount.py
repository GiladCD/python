def read_file_content_to_dictionary(file_path):
    with open(file_path, encoding='utf-8') as file:
        d = {}
        for line in file:
            splited = line.split()
            for word in splited:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
        return d  

def sort_words(words_dict, n):
    sorted_items = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    top_n_items = sorted_items[:n]
    return dict(top_n_items)

file_path = "C:\\Users\\gilad\\Downloads\\11-0.txt"
x = read_file_content_to_dictionary(file_path)
n = int(input("enter N: "))
sorted_x = sort_words(x, n)
print(sorted_x)
