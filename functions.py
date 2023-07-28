from datetime import date
import pandas as pd 

store = pd.read_csv("./data/store.csv")

def competition_since(df):
    """makes a new feature that counts month since the competition is present"""

    # Fill NaN values inplaces
    df.CompetitionOpenSinceYear.fillna(0, inplace=True)
    df.CompetitionOpenSinceMonth.fillna(0, inplace=True)

    # Round and type convert
    df.CompetitionOpenSinceYear = df.CompetitionOpenSinceYear.round().astype("int")
    df.CompetitionOpenSinceMonth = df.CompetitionOpenSinceMonth.round().astype("int")

    today = date.today()

    # new feature -> Calculate since when there is competition in month
    df["Competition_Since_X_months"] = (
        today.year - df.CompetitionOpenSinceYear
    ) * 12 + (today.month - df.CompetitionOpenSinceMonth)

    # competition dating from the 80' does not count
    months_since = (today.year - 1980) * 12 + today.month
    df.loc[
        df["Competition_Since_X_months"] > months_since, ["Competition_Since_X_months"]
    ] = 0

    # Set Competition_Since_X_months to 0 when there are zero months
    df.loc[df["Competition_Since_X_months"] <= 0, "Competition_Since_X_months"] = 0

    # drop the columns we no longer need
    df.drop(
        columns=["CompetitionOpenSinceYear", "CompetitionOpenSinceMonth"], inplace=True
    )

    return df

def clean_data(df):
    df = df.dropna()
    df = pd.merge(df, store, on='Store')
    df = df[df['Open']==1]
    df = df[df['Sales']>0]
    df = df[df['CompetitionDistance']<2000]
    df = competition_since(df)
    df = df[df['Competition_Since_X_months']<60]
    return df