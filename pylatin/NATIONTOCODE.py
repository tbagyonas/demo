import random
class intDict(object):
    def __init__(self, numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    def addEntry(self, dictKey, dictVal):
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
    def getValue(self, dictKey):
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in self.buckets:
                for e in b:
                    result = result + str(e[0]) + ':' + str(e[1]) + ','
            return result[:-1] + '}'
D = intDict(29)
for i in range(20):
    key = random.randint(0, 10**5)
    D.addEntry(key, i)
print ("The value of the intDict is:")
print (D)
print('\n', "the bucket are:")
for hashBucket in D.buckets:
    print ('  ', hashBucket)
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])
def domain_name(email):
    return email.split('@')[1]
print(domain_name('user@domain.com'))

def findDog(s):
    return 'dog' in s.lower().split()
print(findDog('Is there a dog there'))

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count +=1
    return count
print(countDog('This dog runs faster than the ohter DOG dog dude!'))
