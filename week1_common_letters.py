def charCount(string):
    lowers = string.lower()
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    counts = {}
    for i in characters:
        counts[i] = lowers.count(i)
    temp = sorted(counts.items(), key= lambda c: (-c[1],c[0]))[:3]
    print temp
