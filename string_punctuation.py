#Replace all punctuation with # symbol in a given string(Use string.punctuation)

import string

str1 = "/* the # string with special & charactors $.";

res_string = str1.translate(str1.maketrans('', '', string.punctuation));

print(res_string);