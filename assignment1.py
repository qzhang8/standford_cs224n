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
