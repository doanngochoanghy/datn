from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


class NBModel(object):
    def __init__(self):
        self.clf = self._init_pipeline()

    @staticmethod
    def _init_pipeline():
        f = open('vietnamese-stopwords-dash.txt', 'r')
        sw = f.read().splitlines()
        f.close()
        pipe_line = Pipeline([("vect",
                               CountVectorizer(
                                   min_df=5, max_df=0.7, stop_words=sw)),
                              ("tfidf", TfidfTransformer()),
                              ("clf", MultinomialNB())])
        return pipe_line
