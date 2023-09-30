# Import necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

# Define your data in a dictionary
data = {
    'Outlook': ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'sunny'],
    'Temperature': ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild'],
    'Humidity': ['high', 'high', 'high', 'high', 'Normal', 'Normal', 'Normal', 'high', 'Normal', 'Normal', 'Normal', 'high', 'Normal', 'high'],
    'Windy': [False, True, False, False, False, True, True, False, False, False, True, True, False, True],
    'Play': ['No', 'No', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# One-hot encode categorical features
categorical_columns = ['Outlook', 'Temperature', 'Humidity']
encoder = OneHotEncoder(drop='first', sparse=False)
encoded_features = encoder.fit_transform(df[categorical_columns])
encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_columns))

# Combine encoded features with non-categorical features
X = pd.concat([encoded_df, df['Windy']], axis=1)

# Target variable
y = df['Play']

# Create a DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Fit the model on the entire dataset
clf.fit(X, y)

# Create a sample test entry
sample_entry = {
    'Outlook': 'sunny',
    'Temperature': 'cool',
    'Humidity': 'Normal',
    'Windy': False
}

# Preprocess the sample test entry and make a prediction
sample_encoded = encoder.transform([[sample_entry['Outlook'], sample_entry['Temperature'], sample_entry['Humidity']]])
sample_data = pd.DataFrame(sample_encoded, columns=encoder.get_feature_names_out(categorical_columns))
sample_data['Windy'] = sample_entry['Windy']
prediction = clf.predict(sample_data)

# Output the prediction
if prediction[0] == 'yes':
    print("You should play.")
else:
    print("You should not play.")
