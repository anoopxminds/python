#Replace all punctuation with # symbol in a given string(Use string.punctuation)

import string

test_str = "/* the # string with special & charactors $.";

#res_string = str1.translate(str1.maketrans('', '', string.punctuation));
for punctuation in string.punctuation:
    test_str = test_str.replace(punctuation, '#')

print(test_str);