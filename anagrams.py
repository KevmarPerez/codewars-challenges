def anagrams(word, words):
    size= len(word)
    mylist = []
    for elem in words:
        word = ''.join(sorted(word))
        sorted_elem = ''.join(sorted(elem))
        print('{} : {}'.format(sorted_elem,  (word==sorted_elem)))
        if size == len(elem) and word==sorted_elem:
            mylist.append(elem)
    return(mylist)

def anagrams1(word, words):
        return([elem for elem in words if ''.join(sorted(word)) == ''.join(sorted(elem))])
    
print(anagrams1('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) )
print(anagrams1('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams1('laser', ['lazing', 'lazy',  'lacer']))