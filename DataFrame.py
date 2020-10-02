"""DataFrames are like tables which can be created in Pandas. It is 2d rather than 3d for Numpy.
It can handle heterogenous data rather than handling just numbers in Numpy.

DataFrames can be created in three ways
            -> From a Empty DataFrame
            -> From a Dictionary
            -> From Files
"""
import pandas as pd
#Creating a Dataframe
countries=['India','China','US']
population=[130,180,30]
df=pd.DataFrame(list(zip(countries,population)),columns=['countries','population'])
print (df)

#From a Dictionary
L1=[1,2,3,4,5]
count=['count1','count2','count3','count4','count5']
dict={"l1":L1,
        "count":count}
df=pd.DataFrame(dict)
print (df)