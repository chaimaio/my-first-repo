from datetime import date

import streamlit as st

from pandas import DataFrame

from packages import fetch

st.write(st.session_state)

data_frequency_options: dict = {
    "1d": "每天",
    "1wk": "每週",
    "1mo": "每月"
}


def format_func(option) -> None:
    return data_frequency_options[option]


def form_callback() -> None:
    pass


with st.form(key="my_form"):
    ticker_input: str = st.text_input("股票代號", key="ticker")
    is_taiwan: bool = st.toggle("台灣地區股票", key="is_taiwan")

    start_date_input: date = st.date_input("開始日期", key="start_date")
    end_date_input: date = st.date_input("結束日期", key="end_date")

    data_frequency_input: str = st.selectbox("資料頻率",
                                             options=list(data_frequency_options.keys()),
                                             format_func=format_func,
                                             key="data_frequency")

    submit_button: bool = st.form_submit_button(label="確定", on_click=form_callback)
