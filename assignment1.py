#Question 1.1
def distinct_words(corpus):
    """ Determine a list of distinct words for the corpus.
        Params:
            corpus (list of list of strings): corpus of documents
        Return:
            corpus_words (list of strings): sorted list of distinct words across the corpus
            n_corpus_words (integer): number of distinct words across the corpus
    """
    corpus_words = []
    n_corpus_words = -1
    
    ### SOLUTION BEGIN
    undup_words_set = set()
    
    for x in corpus:
        for y in x:
            undup_words_set.add(y)
    
    for w in undup_words_set:
        corpus_words.append(w)
    
    corpus_words.sort()
    n_corpus_words = len(corpus_words)
    
    ### SOLUTION END

    return corpus_words, n_corpus_words

#Question 1.2
def compute_co_occurrence_matrix(corpus, window_size=4):
    """ Compute co-occurrence matrix for the given corpus and window_size (default of 4).
    
        Note: Each word in a document should be at the center of a window. Words near edges will have a smaller
              number of co-occurring words.
              
              For example, if we take the document "<START> All that glitters is not gold <END>" with window size of 4,
              "All" will co-occur with "<START>", "that", "glitters", "is", and "not".
    
        Params:
            corpus (list of list of strings): corpus of documents
            window_size (int): size of context window
        Return:
            M (a symmetric numpy matrix of shape (number of unique words in the corpus , number of unique words in the corpus)): 
                Co-occurence matrix of word counts. 
                The ordering of the words in the rows/columns should be the same as the ordering of the words given by the distinct_words function.
            word2ind (dict): dictionary that maps word to index (i.e. row/column number) for matrix M.
    """
    words, n_words = distinct_words(corpus)
    M = None
    word2ind = {}
    
    ### SOLUTION BEGIN
    M = np.zeros((n_words, n_words))
    
    ### we should try to scan the corpus once to calculate the co-occurence.
    for doc in corpus:
        for word in doc:
            #find the index for word
            row_index = words.index(word)
            #now, find the surrounding word
            for s in range(-window_size,  window_size):
                 if (s == 0):
                    continue   #ignore the central word itself
                pos = doc.index(word)  #position in the doc
                if (pos < window_size - 1) or (pos > len(doc) - window_size):
                    continue
                sur_word = doc[pos+s]
                col_index = words.index(sur_word)
                M[row_index, col_index] = M[row_index, col_index] + 1
             
                word2ind[word] = (row_index, col_index)
  
    ### SOLUTION END

    return M, word2ind
