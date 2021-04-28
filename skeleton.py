from transliterate import translit, get_available_language_codes


class Translit:
    def __init__(self, main_string, language1, language2):
        self.text = main_string
        self.l1 = language1
        self.l2 = language2

    def replace(self):
        if self.l1 == 'rus' and self.l2 == 'eng':
            cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I' \
                    '|K|L|M|N|O|P|R|S|T|U|F|Kh|Tc|Ch|Sh|Shch||Y||E|Iu|Ia'.split('|')
            return self.text.translate({ord(k): v for k, v in zip(cyrillic, latin)})
        elif self.l1 == 'eng' and self.l2 == 'rus':
            return translit(self.text, 'ru')
