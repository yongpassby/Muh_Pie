# https://www.codevscolor.com/python-remove-duplicate-lines-text-file/

import hashlib

in_file = ''
out_file = ''

completed_lines_hash = set()

with open(out_file, 'w') as op_file:
    with open(in_file, 'r') as in_file:
        for oneline in in_file:
            hashVl = hashlib.md5(oneline.rstrip().encode('utf-8')).hexdigest()
            if hashVl not in completed_lines_hash:
                op_file.write(oneline)
                completed_lines_hash.add(hashVl)
