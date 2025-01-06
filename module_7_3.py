class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                string = file.read().lower()
                for i in punctuation:
                    string = string.replace(i, ' ')
                words = string.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        results = {}
        word = word.lower()

        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                results[file_name] = position

        return results

    def count(self, word):
        all_words = self.get_all_words()
        results = {}
        word = word.lower()

        for file_name, words in all_words.items():
            if word in words:
                count = words.count(word)
                results[file_name] = count

        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

