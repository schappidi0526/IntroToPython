#find the last token of any given url
# https://ajaytech.com/just-enough-python/numpy?a=b

def last_token(url) :
    listurl=url.split('/')
    print (listurl)
    count=0
    for word in listurl:
        count=count+1
    return listurl[count-1]


print (last_token('https://ajaytech.com/just-enough-python/numpy'))
