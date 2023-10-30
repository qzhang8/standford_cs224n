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
        pos = 0
        for word in doc:
            #find the index for word
            row_index = words.index(word)
            #now, find the surrounding word
            for s in range(-window_size,  window_size):
                if (s == 0):
                    continue   #ignore the central word itself

                if ((pos + s < 0) or (pos + s > len(doc) -1)) :
                    word2ind[word] = row_index
                    pos = pos + 1
                    continue
                sur_word = doc[pos+s]
                col_index = words.index(sur_word)

          
                M[row_index, col_index] = M[row_index, col_index] + 1
                M[col_index, row_index] = M[col_index, row_index] + 1
               
                word2ind[word] = row_index
                pos = pos + 1
  
    ### SOLUTION END

    return M, word2ind

#Question 1.3    
def reduce_to_k_dim(M, k=2):
    """ Reduce a co-occurence count matrix of dimensionality (num_corpus_words, num_corpus_words)
        to a matrix of dimensionality (num_corpus_words, k) using the following SVD function from Scikit-Learn:
            - http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html
    
        Params:
            M (numpy matrix of shape (number of unique words in the corpus , number of unique words in the corpus)): co-occurence matrix of word counts
            k (int): embedding size of each word after dimension reduction
        Return:
            M_reduced (numpy matrix of shape (number of corpus words, k)): matrix of k-dimensioal word embeddings.
                    In terms of the SVD from math class, this actually returns U * S
    """    
    n_iters = 10     # Use this parameter in your call to `TruncatedSVD`
    M_reduced = None
    print("Running Truncated SVD over %i words..." % (M.shape[0]))
    
    ### SOLUTION BEGIN
    svd = TruncatedSVD(n_components=k, n_iter=n_iters)
    M_reduced = svd.fit_transform(M)
    ### SOLUTION END

    print("Done.")
    return M_reduced

    #Question 1.4
    def plot_embeddings(M_reduced, word2ind, words):
    """ Plot in a scatterplot the embeddings of the words specified in the list "words".
        NOTE: do not plot all the words listed in M_reduced / word2ind.
        Include a label next to each point.
        
        Params:
            M_reduced (numpy matrix of shape (number of unique words in the corpus , 2)): matrix of 2-dimensioal word embeddings
            word2ind (dict): dictionary that maps word to indices for matrix M
            words (list of strings): words whose embeddings we want to visualize
    """

        ### SOLUTION BEGIN
        for w in words:
            idx = word2ind[w]
            x = M_reduced[idx][0]
            y = M_reduced[idx][1]
            plt.scatter(x, y, marker='x', color='red')
            plt.text(x, y, w, fontsize=9)
        plt.show()
        
        ### SOLUTION END
