import pandas as pd

df = pd.read_csv("softwareeng.csv")

df = df[["content", "category"]]

desired_row_count_per_category = 350

df = df.groupby('category').apply(
    lambda x: x.sample(desired_row_count_per_category))

# Reset the index of the resulting DataFrame.
df.reset_index(drop=True, inplace=True)

content = df["content"]

category = df["category"]

df = pd.DataFrame(zip(content, category), columns=['prompt', 'completion'])

df.to_json("categories.jsonl", orient='records', lines=True)
