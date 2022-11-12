import pandas as pd

# grouping values in a column by a criteria
# and getting their mean using pandas

df = pd.DataFrame(
    [
        ["B", 8, 86],
        ["C", 8, 90],
        ["D", 8, None],
        ["E", 8, 91],
        ["F", 7, 66],
        ["G", 3, 44],
    ],
    columns=["Name", "IMDB Score", "Meta Score"],
)

df["Meta Score"] = df.groupby("IMDB Score")["Meta Score"].transform(
    lambda value: value.fillna(value.mean())
)

print(df)
