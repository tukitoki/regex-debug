
class FlagsForm:

    _REGEX_DESCRIPTION = ['g modifier: global. All matches (don\'t return after first match)',
                          'm modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)',
                          'i modifier: insensitive. Case insensitive match (ignores case of [a-zA-Z])',
                          'x modifier: extended. Spaces and text after a # in the pattern are ignored',
                          's modifier: single line. Dot matches newline characters',
                          'u modifier: unicode. Make \w, \W, \b, \B, \d, \D, \s and \S perform matching with Unicode semantic (redundant in Python 3)',
                          'a modifier: ascii. Force the escape sequences \w, \W, \b, \B, \d, \D, \s and \S to perform ASCII-only matching instead of full Unicode matching']

    def __init__(self):
        self.g = 'unchecked'
        self.m = 'unchecked'
        self.i = 'unchecked'
        self.x = 'unchecked'
        self.s = 'unchecked'
        self.u = 'unchecked'
        self.a = 'unchecked'
        self.function_match = 'unchecked'
        self.function_substitution = 'unchecked'
        self.subs_display = False
        self.flag_str = ''
        self.flag_description = []
        self.flag_description_len = 0

    def checker(self, flags, function=['match']):
        for string in flags:
            match string:
                case 'global':
                    self.g = 'checked'
                    self.flag_str += 'g'
                    self.flag_description.append(self._REGEX_DESCRIPTION[0])
                case 'multiline':
                    self.m = 'checked'
                    self.flag_str += 'm'
                    self.flag_description.append(self._REGEX_DESCRIPTION[1])
                case 'insensitive':
                    self.i = 'checked'
                    self.flag_str += 'i'
                    self.flag_description.append(self._REGEX_DESCRIPTION[2])
                case 'extended':
                    self.x = 'checked'
                    self.flag_str += 'x'
                    self.flag_description.append(self._REGEX_DESCRIPTION[3])
                case 'single-line':
                    self.s = 'checked'
                    self.flag_str += 's'
                    self.flag_description.append(self._REGEX_DESCRIPTION[4])
                case 'unicode':
                    self.u = 'checked'
                    self.flag_str += 'u'
                    self.flag_description.append(self._REGEX_DESCRIPTION[5])
                case 'ascii':
                    self.a = 'checked'
                    self.flag_str += 'a'
                    self.flag_description.append(self._REGEX_DESCRIPTION[6])
        if function[0] == 'match':
            self.function_match = 'checked'
            self.subs_display = False
        else:
            self.function_substitution = 'checked'
            self.subs_display = True
        self.flag_description_len = len(self.flag_description)


class StringForm:

    def __init__(self):
        self.test_string = ''
        self.regex_string = ''
        self.subs_string = ''


class FlagExampleForm:

    _EXAMPLES = [('this', 'match this and again this'),
                 ('^d.+\d{3}$', 'digits coming up 443'),
                 ('a', 'A or a'),
                 ('a#comment here', 'a#comment here'),
                 ('e.*r', 'one \
two \
three'),
                 ('α', 'aαbeta'),
                 ('w+', 'αbeta')]

    def get_regex_and_str(self, flag):
        match flag:
            case 'global':
                return self._EXAMPLES[0].__getitem__(0), self._EXAMPLES[0].__getitem__(1)
            case 'multiline':
                return self._EXAMPLES[1].__getitem__(0), self._EXAMPLES[1].__getitem__(1)
            case 'insensitive':
                return self._EXAMPLES[2].__getitem__(0), self._EXAMPLES[2].__getitem__(1)
            case 'extended':
                return self._EXAMPLES[3].__getitem__(0), self._EXAMPLES[3].__getitem__(1)
            case 'single-line':
                return self._EXAMPLES[4].__getitem__(0), self._EXAMPLES[4].__getitem__(1)
            case 'unicode':
                return self._EXAMPLES[5].__getitem__(0), self._EXAMPLES[5].__getitem__(1)
            case 'ascii':
                return self._EXAMPLES[6].__getitem__(0), self._EXAMPLES[6].__getitem__(1)

