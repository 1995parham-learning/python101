from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame(
    {
        "gender": ["man", "women", "child", "man", "women", "child"],
        "age": [40, 40, 10, 50, 50, 8],
    }
)


def ordinal_encoding(genders):
    le = LabelEncoder()
    le.fit(genders)
    return le.transform(genders)


encoded_genders = ordinal_encoding(df["gender"])

print(encoded_genders)
