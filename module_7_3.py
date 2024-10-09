class WordsFinder:
    def __init__(self, *args):
        self.file_names = args
        print(self.file_names)

    def get_all_words(self):
        all_words = {}
        remove_list = ['\n', ',', '.', '=', '!', '?', ';', ':']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                stroka = file.read().lower()
                all_words[file_name] = stroka.translate(str.maketrans({ord(r): " " for r in remove_list})).replace(
                    ' - ', ' ').split()
        return all_words

    def find(self, word):
        all_find = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_find[name] = words.index(word.lower()) + 1
            else:
                all_find[name] = 'Нету'
        return all_find

    def count(self, word):
        all_find = {}
        for name, words in self.get_all_words().items():
            all_find[name] = words.count(word.lower())
        return all_find


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
