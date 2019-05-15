import pandas as pd
import codecs
from sklearn.model_selection import train_test_split  
import time
from model.svm_model import SVMModel
import pickle

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

data = pd.read_csv(
    codecs.open('../train_data/data_dantri.csv', 'r', 'utf-8'))
data = data.append(pd.read_csv(
    codecs.open('../train_data/vnexpress.csv', 'r', 'utf-8')),ignore_index=True)

data = data.loc[data.sample(frac=1).groupby('label').cumcount() <= 2000]
         
X, y = data.content, data.label
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

start = time.time()
model = SVMModel('rbf')
clf = model.clf.fit(X_train,y_train)

print(time.time() - start)
pkl_filename = "svm_model.pkl"  
with open(pkl_filename, 'wb') as file:  
    pickle.dump(clf, file)
data = pd.read_csv(codecs.open('train_data/vietnamnet.csv', 'r', 'utf-8'))         
X_test, y_test = data.content, data.label
y_pred = clf.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))
