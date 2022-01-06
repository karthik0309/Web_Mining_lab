inverted_index={}

def file_to_list(*files):
    files_list=[]
    for file in files:
        files_list.append(open(file, "r").read());
    return files_list

def remove_punctuation(string):
    punc = '''!0-[]{};:'"\,>./7@#$%^&*_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string

def word_dictionary(files_list):
    for i, file in enumerate(files_list):
        for word in file.split():
            clean_word = remove_punctuation (word)
            if clean_word in inverted_index:
                inverted_index [clean_word].append(i+1)
            else:
                inverted_index [clean_word]=[i+1]

def add_freq_to_dict():
    for word, posting_list in inverted_index.items():
        freq = len(posting_list)
        posting_list=list(dict.fromkeys (posting_list))
        inverted_index [word] = (freq, posting_list)

def print_dict_as_table():
    print("WORD"," FREQ"," POSTING_LIST")
    for key, value in inverted_index.items():
        freq, posting_list = value
        print ("{:<10} {:<10}".format(key, freq), end=" ")
        print(posting_list)

def find_word_in_doc (word):
    if word in inverted_index:
        res = inverted_index [word] [1]
        print(word," is found in docs with ids:", res)
    else:
        print("No such word is found")

files_list=file_to_list("docs/file1.txt","docs/file2.txt")
word_dictionary(files_list)
add_freq_to_dict()
find_word_in_doc("American")
print_dict_as_table()