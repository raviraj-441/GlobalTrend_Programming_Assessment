import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def clean_preprocess(df):
    df = df.fillna(df.mean(numeric_only=True)) 
    df = df.fillna('Unknown')  

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df

data = {
    'Age': [25, 30, 22, None],
    'Salary': [50000, 60000, 55000, 45000],
    'Gender': ['Male', 'Female', None, 'Male']
}
df = pd.DataFrame(data)
print(clean_preprocess(df))
