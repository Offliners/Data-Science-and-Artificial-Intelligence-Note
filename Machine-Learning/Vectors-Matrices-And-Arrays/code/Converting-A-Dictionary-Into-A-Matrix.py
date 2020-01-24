from sklearn.feature_extraction import DictVectorizer

data_dict = [{'Red' : 2, 'Blue' : 4},
             {'Red' : 4, 'Blue' : 3},
             {'Red' : 1, 'Yellow' : 2},
             {'Red' : 2, 'Yellow' : 2}]

dictvectorize = DictVectorizer(sparse=False)

features = dictvectorize.fit_transform(data_dict)

print(features)

print(dictvectorize.get_feature_names())
