from regular_expression import RegularExpression
from forms import *
import re as re

if __name__ == '__main__':
    flags = FlagsForm()
    # flags.g = 'checked'
    flags.a = 'checked'
    flags.i = 'checked'
    flags.x = 'checked'
    match = RegularExpression()
    print(re.finditer(rf'[abc]+', 'a bb ccc', re.ASCII, re.VERBOSE, re.IGNORECASE))
    # match.find_matches(flags, '', '[abc]+', 'a bb ccc')
    # print(match.matches)
    # print(match.span)
