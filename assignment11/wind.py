import plotly.express as px
import plotly.data as pldata


df = pldata.wind(return_type="pandas")


print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

df["strength"] = (
    df["strength"]
    .str.replace("+", "", regex=False)
    .str.replace(r"(\d+)-(\d+)", r"\2", regex=True)
    .astype(float)
)

print("\nCleaned strength values:")
print(df[["direction", "strength", "frequency"]].head(10))

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs. Frequency"
)

fig.write_html("wind.html", auto_open=True)