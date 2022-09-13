def generate_hashtag(s):
    if len(s) != 0 and len(s) < 140:
        s = s.title()
        li = list(s.split())
        li.insert(0, "#")
        listToStr = "".join(map(str, li))
        return listToStr
    else: 
        return False
 
string = " Hello there thanks for trying my Kata"
print(generate_hashtag(string))