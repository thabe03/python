import random 
from sre_parse import SPECIAL_CHARS
import string

letter = string.ascii_letters
number = '0123456789'
SPECIAL_CHARS = '!'
all = letter+number+SPECIAL_CHARS
psw = ''.join(random.sample(all,6))
print(psw)