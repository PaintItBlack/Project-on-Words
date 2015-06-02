def dist (l_words, l_sen): #Another way would be to have 
    length = len(l_words)
    d_mat = zeros(length,length)
    for i in range(length):
        word1=l_words[i]
        for j in range(i):
            word2=l_words[j]
            for sentence in l_sen:
                test1 = word1 in sentence
                test2 = word2 in sentence
                if ((not test1) and test2) or (test1 and (not test2)):
                    d_mat[i][j] += 1
    return d_mat
