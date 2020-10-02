#Indexing and slicing in Numpy works exactly same to indexing in Lists
#Indexing
import numpy as np
a=np.array([[1,2,3],
            [4,5,6]])

print (a[1,1])
#Slicing

import numpy as np
a=np.array([[1,2,3,10],
            [4,5,6,11],
            [7,8,9,12]]
        )

print (a[1])
print (a[1,0:3])
print (a[0:2,1:3])

a1=np.array([
            [[1,2,3,10],
            [4,5,6,11],
            [7,8,9,12]],
            # [['a','b','c'],
            # ['d','e','f'],
            # ['g','h','i']]
            [[13,14,15,16],
            [17,18,19,20],
            [21,22,23,24]]
            ]            
        )
print (a1[1,1:3,2:4])

# import numpy as np. You cannot have characters in any list in Numpy
# a1=np.array([
#             [[1,2,3,10],
#             [4,5,6,11],
#             [7,8,9,12]],
#             [['a','b','c'],
#             ['d','e','f'],
#             ['g','h','i']]
#             ]

