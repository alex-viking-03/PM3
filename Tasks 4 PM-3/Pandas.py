import pandas

ages = pandas.Series([18, 21, 19, 20])
print(ages)

print()
print()

data = {
    "Name": ["Aibek", "Sofia", "Tamer", "Asik"],
    "Age": [18, 19, 18, 20],
    "Grade": [85, 92, 77, 64]
}

df = pandas.DataFrame(data)
print(df)

print()

print(df.head(2))

print()
print()

print(df.info())

print()
print()

print(df.describe())

print()
print()

print(df["Grade"])

print()
print()

print(df.loc[1])

print()
print()

print(df.iloc[1])

print()
print()

df["Group"] = ["A", "A", "B", "B"]
print(df)

print()
print()

df.loc[0, "Grade"] = 90
print(df)

print()
print()

df = df.drop("Group", axis=1)
print(df)

print()
print()

print(df[df["Grade"] > 80])

print()
print()

print(df[(df["Grade"] > 70) & (df["Age"] < 20)])

print()
print()

print(df.sort_values("Grade", ascending=False))

print()
print()

print(df["Grade"].mean())
print(df["Grade"].median())
print(df["Grade"].sum())
print(df["Grade"].max())
print(df["Grade"].min())

print()
print()

def category(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    else:
        return "Bad"

df["Desc"] = df["Grade"].apply(category)
print(df)

print()
print()

df["Group"] = ["A", "A", "B", "B"]
grouped = df.groupby("Group")["Grade"].mean()
print(grouped)