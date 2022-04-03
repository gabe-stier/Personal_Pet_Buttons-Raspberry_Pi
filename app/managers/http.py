from typing import Literal, Union
from requests import get, post, put
from hashlib import sha3_512
from app.managers.encryption import EncryptionManager
from json import dumps

class HttpManager:
    fqdn = ''
    port = ''
    password = ''
    methods = Literal['get','post','put']
    def __init__(self, url, port, key_signature, salt) -> None:
        self.fqdn = url
        self.port = port
        self.password = key_signature
        self.salt = salt

    def send_request(self, msg:dict, req_type:methods, uri:str):
        if req_type == "get":
            return True
        elif req_type == 'post':
            return True
        elif req_type == "put":
            return True
        else:
            url = f'{self.fqdn}/error'
            error_message = {
                "message": msg,
                "error": "Invalid request_type",
                "uri": uri,
                "request_type": req_type
            }
            encrypted_message = EncryptionManager.encrypt(dumps(error_message), self.password, self.salt).decode()
            post(url, data=encrypted_message, verify=False)
        return False