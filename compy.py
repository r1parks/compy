#!/usr/bin/env python

def run():
    import sys
    import re
    if len(sys.argv) != 2:
        print "gimme a file idiot"
        sys.exit(1)
    with open(sys.argv[1]) as source_file:
        source_code = [line[:-1] for line in source_file.readlines()]
    variable_base = '_tmp_'
    for line_number in range(len(source_code)):
        line = source_code[line_number]
        regex = r'^(?P<indent>\s*)\|>\s*(?P<before>.*)\$(?P<after>.*)'
        match = re.match(regex, line)
        if match:
            assert line_number > 0
            variable = variable_base + str(line_number)
            source_code[line_number] = "{}{}{}{}".format(
                match.group('indent'),
                match.group('before'),
                variable,
                match.group('after'))
            previous_line = source_code[line_number-1]
            regex = r'(?P<indent>\s*)(?P<code>.+)'
            match = re.match(regex, previous_line)
            source_code[line_number-1] = "{}{} = {}".format(
                match.group('indent'),
                variable,
                match.group('code'))
    python_filename = 'valid_' + sys.argv[1]
    with open(python_filename, 'w') as valid_python_file:
        for line in source_code:
            print >>valid_python_file, line
    import os
    os.system('ipython ' + python_filename)

if __name__ == '__main__':
    run()
