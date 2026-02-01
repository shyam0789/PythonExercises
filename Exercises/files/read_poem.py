word_occurrence_count_dict = {}
with open("poem.txt",mode="r") as poemfile:
    text = poemfile.read().replace("\n"," ")
    poem_word_list = text.split(" ")
    for word in poem_word_list:
        if word not in word_occurrence_count_dict:
            word_occurrence_count_dict[word] = 1
        else:
            word_occurrence_count_dict[word] +=1
    # print(max(word_occurrence_count_dict.values()))
    word = [k for k,v in word_occurrence_count_dict.items() if v == max(word_occurrence_count_dict.values())]
    print(f"Word(s) with max count is / are {word}")