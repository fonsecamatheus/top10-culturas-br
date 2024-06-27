from typing import Any, Dict, List

import requests as rq


class HttpRequester:
    def __init__(self) -> None:
        self.url = 'https://apisidra.ibge.gov.br/values/t/5457/n1/all/n3/all/u/y/v/214,216,8331/p/all/c782/40099,40102,40106,40119,40122,40124,40127,40136,40139,40151'

    def http_response(self) -> List[Dict[str, Any]]:
        try:
            response = rq.get(self.url)
            response.raise_for_status()
            return response.json()
        except rq.exceptions.RequestException:
            print('Erro ocorreu na requisição')
        except rq.exceptions.ConnectionError:
            print('Erro ocorreu na rede/servidor')
        except rq.exceptions.Timeout:
            print('Erro ocorreu pois a rede/servidor estão instáveis')
        except Exception as e:
            print(f'Erro inesperado: {e}')
            return {}
