from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle
from sklearn.externals import joblib

iris = datasets.load_iris()

X,y = iris.data, iris.target

clf = LogisticRegression(random_state=0)
clf.fit(X,y)

saved_model = pickle.dumps(clf)

print(saved_model)

clf_from_pickle = pickle.loads(saved_model)
print(clf_from_pickle.predict(X))

joblib.dump(clf, 'Saved_model.pkl')
clf_from_joblib = joblib.load('Saved_model.pkl')
print(clf_from_joblib.predict(X))
