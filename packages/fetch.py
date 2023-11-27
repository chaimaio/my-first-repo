from pandas import DataFrame
from yfinance import download


def fetch(ticker, start_date=None, end_date=None, data_frequency=None) -> DataFrame:
    ticker: DataFrame = download(
        ticker,
        start_date,
        end_date,
        interval=data_frequency
    )

    return ticker
