import json
from typing import Dict
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
from .utils import byte_to_str


class Tools(object):

    # 字符串转json
    @staticmethod
    def str_to_json(content):
        return json.loads(content)

    # 解密支付结果数据，详见(https://pay.weixin.qq.com/wiki/doc/apiv3/apis/chapter3_5_5.shtml)
    # 通过商户公钥加密，用商户私钥解密
    # api_v3_key: 公钥
    # nonce: 加密使用的随机串初始化向量
    # ciphertext：Base64编码后的密文
    # associated_data：附加数据包（可能为空）
    @staticmethod
    def decrypt_data(api_v3_key: str, nonce: str, ciphertext: str, associated_data: str) -> Dict:
        key_bytes = str.encode(api_v3_key)
        nonce_bytes = str.encode(nonce)
        ad_bytes = str.encode(associated_data)
        data = base64.b64decode(ciphertext)

        aesgcm = AESGCM(key_bytes)
        result_bytes = aesgcm.decrypt(nonce_bytes, data, ad_bytes)
        return Tools.str_to_json(byte_to_str(result_bytes))
