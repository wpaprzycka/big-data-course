import re

WORD_RE = re.compile(r'[\w]+')

words = WORD_RE.findall('Big data 1 234 !! Weronika@# ale jaja_123')
print(words)