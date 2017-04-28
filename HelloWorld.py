from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
#0 = apple, 1 = orange
labels = [0, 0, 1, 1]
#Creates classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#print(clf.predict([[160, 0]]))
weight = input("Enter the objects weight: ")
texture = input("Enter 0 if smooth, 1 if bumpy: ")
if clf.predict([[weight, texture]]) == 1:
	print("It is an orange!")
else:
	print("It is an apple!")