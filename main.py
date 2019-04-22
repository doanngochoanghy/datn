#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from model.svm_model import SVMModel
import codecs


class TextClassificationPredict(object):
    def __init__(self):
        self.test = None

    def get_train_data(self):
        # Tạo train data
        df_train = pd.read_csv(
            codecs.open('filtered_data/vnexpress.csv', 'r', 'utf-8'))
        model = SVMModel()

        clf = model.clf.fit(df_train["content"], df_train.label)
        return clf


if __name__ == '__main__':
    tcp = TextClassificationPredict()
    tcp.get_train_data()
