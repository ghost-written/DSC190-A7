import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    return (df,)


@app.cell
def _(df, plt):
    plt.hist(df["duration_minutes"], bins=30); plt.xlabel("duration (min)")
    plt.ylabel("count")
    plt.gca()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
