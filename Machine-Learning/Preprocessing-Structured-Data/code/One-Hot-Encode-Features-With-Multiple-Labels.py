from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

y = [('Texas', 'Florida'), 
     ('California', 'Alabama'), 
     ('Texas', 'Florida'), 
     ('Delware', 'Florida'), 
     ('Texas', 'Alabama')]

one_hot = MultiLabelBinarizer()
print(one_hot.fit_transform(y))
print(one_hot.classes_)
