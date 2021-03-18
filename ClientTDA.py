import traceback
import httpx
from tda.auth import easy_client
from tda.auth import client_from_login_flow
from config import client_id, redirect_url, my_account_id
from selenium import webdriver
import pandas as pd


try: # Tries to initialize tda client
    client = easy_client(
        api_key=client_id,
        redirect_uri=redirect_url,
        token_path='resources/token.txt',
        webdriver_func=webdriver.Chrome())

except Exception as exc: # Gets new token if previous token is expired
    client = client_from_login_flow(webdriver.Chrome, api_key=client_id,
                           redirect_url=redirect_url,
                           token_path='resources/token.txt',
                           redirect_wait_time_seconds=0.1,
                           max_waits=3000,
                           asyncio=False,
                           token_write_func=None)
    traceback.print_exc(exc)

stream_client = StreamClient(client, account_id=int(my_account_id))


def get_option_chain(symbol):
    r = client.get_option_chain(symbol=symbol)
    assert r.status_code == httpx.codes.OK, r.raise_for_status()

    return pd.DataFrame(r.json())


def get_quotes(quoteList):
    return pd.DataFrame(client.get_quotes(quoteList).json())


def get_quote(symbol):
    return pd.DataFrame(client.get_quote(symbol).json())