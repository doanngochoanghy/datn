from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn import svm


class SVMModel(object):
    def __init__(self, kernel):
        self.clf = self._init_pipeline(kernel)

    @staticmethod
    def _init_pipeline(kernel):
        f = open('vietnamese-stopwords-dash.txt', 'r')
        sw = f.read().splitlines()
        f.close()
        pipe_line = Pipeline([("vect",
                               CountVectorizer(
                                   min_df=5, max_df=0.7, stop_words=sw)),
                              ("tfidf", TfidfTransformer()),
                              ("clf",
                               svm.LinearSVC(
                                   C=1.0
                                   ))])
        return pipe_line
