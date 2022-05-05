import re


class RegularExpression:

    def __init__(self):
        self.matches = []
        self.span = []
        self.len = 0
        self.find_condition = False
        self.subs_match_string = ''

    def find_matches(self, flags, delimiters, regex, test_string, subs_string):
        regex_flags = 0
        if regex == '':
            return
        if flags.m == 'checked':
            regex_flags |= re.MULTILINE
        if flags.i == 'checked':
            regex_flags |= re.IGNORECASE
        if flags.s == 'checked':
            regex_flags |= re.DOTALL
        if flags.u == 'checked':
            regex_flags |= re.UNICODE
        if flags.x == 'checked':
            regex_flags |= re.VERBOSE
        elif flags.a == 'checked':
            regex_flags |= re.ASCII
        if flags.g == 'checked':
            for m in re.finditer(rf'{regex}', test_string, flags=regex_flags):
                self.matches.append(m[0])
                self.span.append(m.span())
                if flags.function_substitution == 'checked':
                    self.subs_match_string = re.sub(regex, subs_string, test_string, flags=regex_flags)
        else:
            m = re.search(rf'{regex}', test_string, flags=regex_flags)
            if m is not None:
                self.matches.append(m[0])
                self.span.append(m.span())
                if flags.function_substitution == 'checked':
                    self.subs_match_string = re.sub(regex, subs_string, test_string, flags=regex_flags, count=1)
        self.len = len(self.matches)
        self.find_condition = True

