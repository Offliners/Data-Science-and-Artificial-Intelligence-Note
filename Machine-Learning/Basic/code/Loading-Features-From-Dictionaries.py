from sklearn.feature_extraction import DictVectorizer

staff = [{'name': 'Steve Miller', 'age': 33.},
         {'name': 'Lyndon Jones', 'age': 12.},
         {'name': 'Baxter Morth', 'age': 18.}]

vec = DictVectorizer()

vec.fit_transform(staff).toarray()

print(vec.get_feature_names())
