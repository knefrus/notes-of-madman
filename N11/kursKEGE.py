"""from math import *
kod = 26 + 26 + 6
char = ceil( log2(kod) )
ob = ceil((char * 9) / 8 ) * 20


from math import *
kod = 26 + 26 + 10
char = ceil( log2(kod) ) * 11
ob = 1024 / (ceil( char / 8) + 13)
print(ob)
"""
from math import *
kod1 = 26 + 26 + 10
char1 = ceil( log2(kod1) )
lk = ceil(char1 * 11 / 8) #личный код байты

kod2 = 10
char2 = ceil( log2(kod2) )
np = ceil(char2 * 3)