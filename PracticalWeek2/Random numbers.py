"""
Random Numbers
"""

import random

print(random.randint(5, 20))       # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))    # line 3

"""
 Line 1
 smallest number is 5
 biggest number is 20

 Line 2
 smallest number is 3
 biggest number is 9
 Line 2 can never produce 4, since it starts at 3 and steps by 2
 
 Line 3
 smallest number is 2.5
 biggest number is 5.49 = 5.5 depending on rounding
"""