inputs = "bcdef\nabcdefg\nbcde\nbcdef"

    def wordCount(inputs):
        from collections import OrderedDict as OD
        words = inputs.split('\n')
        counts = OD()
        for i, word in enumerate(words):
            if word in counts.keys():
                counts[word] += 1
            else:
                counts[word] = 1
        print counts.values()

wordCount(inputs)
