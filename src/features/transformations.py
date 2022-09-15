import pandas as pd

from src.utils.time import robust_hour_of_iso_date




def hour_of_day(df: pd.DataFrame) -> pd.DataFrame:
    df["event_hour"] = df["event_timestamp"].apply(robust_hour_of_iso_date)
    return df

