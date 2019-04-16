from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier


class SVMModel(object):
    def __init__(self):
        self.clf = self._init_pipeline()

    @staticmethod
    def _init_pipeline():
        f = open('vietnamese-stopwords-dash.txt', 'r')
        sw = f.read().splitlines()
        f.close()
        pipe_line = Pipeline([("vect",
                               CountVectorizer(
                                   min_df=5,
                                   max_df=0.7,
                                   stop_words=sw)),
                              ("tfidf", TfidfTransformer()),
                              ("clf-svm",
                               SGDClassifier(
                                   loss='log',
                                   penalty='l2',
                                   alpha=1e-3,
                                   random_state=None))])
        return pipe_line
