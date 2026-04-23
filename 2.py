import pandas as pd

from sklearn.model_selection import train test split

from sklearn.metrics import accuracy_score

from sklearn.tree import Decision TreeClassifier

from sklearn.preprocessing import LabelEncoder

# Assuming you have the dataset stored in a CSV file named 'credit-g_csv.csv' dataset = pd.read_csv('credit-g_csv.csv')

# Performing label encoding for categorical attributes

label encoder = LabelEncoder()

for column in dataset.columns:

if dataset[column].dtype == 'object': dataset[column] = label encoder.fit transform(dataset[column])

# Splitting the dataset into input features (X) and target variable (y)

X= dataset.drop('class', axis=1)

y = dataset['class']

# Splitting the dataset into training and testing sets X train, X test, y_train, y test = train_test_split(X, y, test size-0.2, random state-42)

# Creating the OneR classifier

oneR = DecisionTreeClassifier(max_depth=6) oneR.fit(X train, y train)

# Get the feature importances (information gain values) importance = oneR.feature_importances

# Create a dictionary to store the attribute and its information gain value attribute ig= {}

for i, feature in enumerate(X.columns): attribute_ig[feature] = importance[i]

# Sort the information gain values in descending order

sorted_ig = sorted(attribute_ig.items(), key=lambda x: x[1], reverse=True)

#Display the sorted information gain values for attribute, ig in sorted ig: print(f"Information Gain for {attribute}: {ig}")
