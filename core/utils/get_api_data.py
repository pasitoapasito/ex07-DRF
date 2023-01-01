import requests
from typing import Tuple, List, Dict

from config.settings import URL


class GetRequestData:
    def get_request_data_n_check_error(keys: List[str]) -> Tuple[Dict[str, str], str]:
        result = {}
        for num, key in enumerate(keys):
            data = {
                'key': key,
                'action': 'balance',
            }

            res = requests.post(URL, data=data)
            if res.status_code == 500:
                return None, '외부 API로부터 데이터를 가져올 수 없습니다.'
            if res.status_code == 422:
                return None, '외부 API에 요청하는 데이터 형식이 올바르지 않습니다.'

            data = res.json()
            if 'balance' in data:
                result[f'key{num+1}'] = data['balance']

        return result, None
