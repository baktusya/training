def single_root_words(root_word, *other_words):
    same_words = list()
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
        else:
            continue
    print(same_words)
    return same_words


single_root_words('вол', 'воЛна', 'бАнан', 'безВолие', 'волЕВой')
single_root_words('барИТон', 'Тон', 'барТер', 'Фантом', 'баР')