import requests
import pandas as pd

def requestApiBcb(data: str) -> pd.DataFrame:
    """
    Funcao para extrair os dados dos meios de pagamentos trimestrais do Banco Central

    Parametros:
    data - string - aaaat (Exemplo: 20191)

    Saída:
    DataFrame - Estrutura de dados do pandas
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    
    req = requests.get(url)
    dados = req.json()
    
    df = pd.json_normalize(dados['value'])
    df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])
    return df

dadosBcb = requestApiBcb('20241')
print (dadosBcb.info())
