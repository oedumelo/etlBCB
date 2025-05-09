import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)

    conn.close()
    return


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return


def salvarMySQL(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
    return
