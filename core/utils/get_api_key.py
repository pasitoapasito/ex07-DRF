import os
from typing import Tuple, List

from config.settings import env, ImproperlyConfigured


class GetApiKey:
    def get_api_key_n_check_error() -> Tuple[List[str], str]:
        NUM = 1
        KEYS = []

        while True:
            try:
                KEYS.append(env(f'KEY{NUM}'))
                NUM += 1
            except ImproperlyConfigured as e:
                break

        if not KEYS:
            return None, '외부 API의 요청 KEY가 필요합니다.'

        return KEYS, None
