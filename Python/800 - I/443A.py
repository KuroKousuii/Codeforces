import re
print(len(set(re.sub("[\s/,{}]", "", input()))))
