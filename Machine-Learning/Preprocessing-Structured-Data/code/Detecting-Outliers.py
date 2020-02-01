import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=10,
                  n_features=2,
                  centers=1,
                  random_state=1)

X[0,0] = 10000
X[0,1] = 10000

outliner_detector = EllipticEnvelope(contamination=.1)
outliner_detector.fit(X)

print(outliner_detector.predict(X))
