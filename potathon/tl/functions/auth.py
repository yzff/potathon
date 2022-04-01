"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeCodeSettings, TypeDataJSON, TypeInputCheckPasswordSRP



class AcceptLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe894ad4d
    SUBCLASS_OF_ID = 0xc913c01a

    def __init__(self, token: bytes):
        """
        :returns Authorization: Instance of Authorization.
        """
        self.token = token

    def to_dict(self):
        return {
            '_': 'AcceptLoginTokenRequest',
            'token': self.token
        }

    def _bytes(self):
        return b''.join((
            b'M\xad\x94\xe8',
            self.serialize_bytes(self.token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _token = reader.tgread_bytes()
        return cls(token=_token)


class BindTempAuthKeyRequest(TLRequest):
    CONSTRUCTOR_ID = 0xcdd42a05
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, perm_auth_key_id: int, nonce: int, expires_at: Optional[datetime], encrypted_message: bytes):
        """
        :returns Bool: This type has no constructors.
        """
        self.perm_auth_key_id = perm_auth_key_id
        self.nonce = nonce
        self.expires_at = expires_at
        self.encrypted_message = encrypted_message

    def to_dict(self):
        return {
            '_': 'BindTempAuthKeyRequest',
            'perm_auth_key_id': self.perm_auth_key_id,
            'nonce': self.nonce,
            'expires_at': self.expires_at,
            'encrypted_message': self.encrypted_message
        }

    def _bytes(self):
        return b''.join((
            b'\x05*\xd4\xcd',
            struct.pack('<q', self.perm_auth_key_id),
            struct.pack('<q', self.nonce),
            self.serialize_datetime(self.expires_at),
            self.serialize_bytes(self.encrypted_message),
        ))

    @classmethod
    def from_reader(cls, reader):
        _perm_auth_key_id = reader.read_long()
        _nonce = reader.read_long()
        _expires_at = reader.tgread_date()
        _encrypted_message = reader.tgread_bytes()
        return cls(perm_auth_key_id=_perm_auth_key_id, nonce=_nonce, expires_at=_expires_at, encrypted_message=_encrypted_message)


class CancelCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1f040578
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, phone_number: str, phone_code_hash: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            '_': 'CancelCodeRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash
        }

    def _bytes(self):
        return b''.join((
            b'x\x05\x04\x1f',
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash)


class CheckPasswordRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd18b4d16
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, password: 'TypeInputCheckPasswordSRP'):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.password = password

    def to_dict(self):
        return {
            '_': 'CheckPasswordRequest',
            'password': self.password.to_dict() if isinstance(self.password, TLObject) else self.password
        }

    def _bytes(self):
        return b''.join((
            b'\x16M\x8b\xd1',
            self.password._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _password = reader.tgread_object()
        return cls(password=_password)


class CheckPhoneRequest(TLRequest):
    CONSTRUCTOR_ID = 0x6fe51dfb
    SUBCLASS_OF_ID = 0x81920c9d

    def __init__(self, phone_number: str):
        """
        :returns auth.checkedPhone: Instance of CheckedPhone.
        """
        self.phone_number = phone_number

    def to_dict(self):
        return {
            '_': 'CheckPhoneRequest',
            'phone_number': self.phone_number
        }

    def _bytes(self):
        return b''.join((
            b'\xfb\x1d\xe5o',
            self.serialize_bytes(self.phone_number),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        return cls(phone_number=_phone_number)


class DropTempAuthKeysRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8e48a188
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, except_auth_keys: List[int]):
        """
        :returns Bool: This type has no constructors.
        """
        self.except_auth_keys = except_auth_keys

    def to_dict(self):
        return {
            '_': 'DropTempAuthKeysRequest',
            'except_auth_keys': [] if self.except_auth_keys is None else self.except_auth_keys[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x88\xa1H\x8e',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.except_auth_keys)),b''.join(struct.pack('<q', x) for x in self.except_auth_keys),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _except_auth_keys = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _except_auth_keys.append(_x)

        return cls(except_auth_keys=_except_auth_keys)


class ExportAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe5bfffcd
    SUBCLASS_OF_ID = 0x5fd1ec51

    def __init__(self, dc_id: int):
        """
        :returns auth.ExportedAuthorization: Instance of ExportedAuthorization.
        """
        self.dc_id = dc_id

    def to_dict(self):
        return {
            '_': 'ExportAuthorizationRequest',
            'dc_id': self.dc_id
        }

    def _bytes(self):
        return b''.join((
            b'\xcd\xff\xbf\xe5',
            struct.pack('<i', self.dc_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _dc_id = reader.read_int()
        return cls(dc_id=_dc_id)


class ExportLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb1b41517
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, api_id: int, api_hash: str, except_ids: List[int]):
        """
        :returns auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.except_ids = except_ids

    def to_dict(self):
        return {
            '_': 'ExportLoginTokenRequest',
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'except_ids': [] if self.except_ids is None else self.except_ids[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x17\x15\xb4\xb1',
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.except_ids)),b''.join(struct.pack('<i', x) for x in self.except_ids),
        ))

    @classmethod
    def from_reader(cls, reader):
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        reader.read_int()
        _except_ids = []
        for _ in range(reader.read_int()):
            _x = reader.read_int()
            _except_ids.append(_x)

        return cls(api_id=_api_id, api_hash=_api_hash, except_ids=_except_ids)


class ImportAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe3ef9613
    SUBCLASS_OF_ID = 0xb9e04e39

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int, bytes: bytes):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.id = id
        self.bytes = bytes

    def to_dict(self):
        return {
            '_': 'ImportAuthorizationRequest',
            'id': self.id,
            'bytes': self.bytes
        }

    def _bytes(self):
        return b''.join((
            b'\x13\x96\xef\xe3',
            struct.pack('<i', self.id),
            self.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.read_int()
        _bytes = reader.tgread_bytes()
        return cls(id=_id, bytes=_bytes)


class ImportBotAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0x67a3ff2c
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.flags = flags
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_auth_token = bot_auth_token

    def to_dict(self):
        return {
            '_': 'ImportBotAuthorizationRequest',
            'flags': self.flags,
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'bot_auth_token': self.bot_auth_token
        }

    def _bytes(self):
        return b''.join((
            b',\xff\xa3g',
            struct.pack('<i', self.flags),
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            self.serialize_bytes(self.bot_auth_token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _flags = reader.read_int()
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        _bot_auth_token = reader.tgread_string()
        return cls(flags=_flags, api_id=_api_id, api_hash=_api_hash, bot_auth_token=_bot_auth_token)


class ImportLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID = 0x95ac5ce4
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, token: bytes):
        """
        :returns auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.token = token

    def to_dict(self):
        return {
            '_': 'ImportLoginTokenRequest',
            'token': self.token
        }

    def _bytes(self):
        return b''.join((
            b'\xe4\\\xac\x95',
            self.serialize_bytes(self.token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _token = reader.tgread_bytes()
        return cls(token=_token)


class LogOutRequest(TLRequest):
    CONSTRUCTOR_ID = 0x5717da40
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'LogOutRequest'
        }

    def _bytes(self):
        return b''.join((
            b'@\xda\x17W',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class RecoverPasswordRequest(TLRequest):
    CONSTRUCTOR_ID = 0x4ea56e92
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, code: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.code = code

    def to_dict(self):
        return {
            '_': 'RecoverPasswordRequest',
            'code': self.code
        }

    def _bytes(self):
        return b''.join((
            b'\x92n\xa5N',
            self.serialize_bytes(self.code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _code = reader.tgread_string()
        return cls(code=_code)


class RequestPasswordRecoveryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd897bc66
    SUBCLASS_OF_ID = 0xfa72d43a

    def to_dict(self):
        return {
            '_': 'RequestPasswordRecoveryRequest'
        }

    def _bytes(self):
        return b''.join((
            b'f\xbc\x97\xd8',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class ResendCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3ef1a9bf
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number: str, phone_code_hash: str):
        """
        :returns auth.SentCode: Instance of either SentCode, SentCodeCaptcha.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            '_': 'ResendCodeRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash
        }

    def _bytes(self):
        return b''.join((
            b'\xbf\xa9\xf1>',
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash)


class ResendCodeCaptchaRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf9421a18
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number: str, phone_code_hash: str, captcha_token: Optional[str]=None, captcha_answer: Optional['TypeDataJSON']=None):
        """
        :returns auth.SentCode: Instance of either SentCode, SentCodeCaptcha.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.captcha_token = captcha_token
        self.captcha_answer = captcha_answer

    def to_dict(self):
        return {
            '_': 'ResendCodeCaptchaRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'captcha_token': self.captcha_token,
            'captcha_answer': self.captcha_answer.to_dict() if isinstance(self.captcha_answer, TLObject) else self.captcha_answer
        }

    def _bytes(self):
        assert ((self.captcha_token or self.captcha_token is not None) and (self.captcha_answer or self.captcha_answer is not None)) or ((self.captcha_token is None or self.captcha_token is False) and (self.captcha_answer is None or self.captcha_answer is False)), 'captcha_token, captcha_answer parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\x18\x1aB\xf9',
            struct.pack('<I', (0 if self.captcha_token is None or self.captcha_token is False else 1) | (0 if self.captcha_answer is None or self.captcha_answer is False else 1)),
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
            b'' if self.captcha_token is None or self.captcha_token is False else (self.serialize_bytes(self.captcha_token)),
            b'' if self.captcha_answer is None or self.captcha_answer is False else (self.captcha_answer._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        if flags & 1:
            _captcha_token = reader.tgread_string()
        else:
            _captcha_token = None
        if flags & 1:
            _captcha_answer = reader.tgread_object()
        else:
            _captcha_answer = None
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash, captcha_token=_captcha_token, captcha_answer=_captcha_answer)


class ResetAuthorizationsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9fab0d1a
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'ResetAuthorizationsRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\x1a\r\xab\x9f',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class SendCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa677244f
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number: str, api_id: int, api_hash: str, settings: 'TypeCodeSettings'):
        """
        :returns auth.SentCode: Instance of either SentCode, SentCodeCaptcha.
        """
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.settings = settings

    def to_dict(self):
        return {
            '_': 'SendCodeRequest',
            'phone_number': self.phone_number,
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'settings': self.settings.to_dict() if isinstance(self.settings, TLObject) else self.settings
        }

    def _bytes(self):
        return b''.join((
            b'O$w\xa6',
            self.serialize_bytes(self.phone_number),
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            self.settings._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        _settings = reader.tgread_object()
        return cls(phone_number=_phone_number, api_id=_api_id, api_hash=_api_hash, settings=_settings)


class SendCodeCaptchaRequest(TLRequest):
    CONSTRUCTOR_ID = 0x7780ee94
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number: str, api_id: int, api_hash: str, allow_flashcall: Optional[bool]=None, current_number: Optional[bool]=None, captcha_token: Optional[str]=None, captcha_answer: Optional['TypeDataJSON']=None):
        """
        :returns auth.SentCode: Instance of either SentCode, SentCodeCaptcha.
        """
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.allow_flashcall = allow_flashcall
        self.current_number = current_number
        self.captcha_token = captcha_token
        self.captcha_answer = captcha_answer

    def to_dict(self):
        return {
            '_': 'SendCodeCaptchaRequest',
            'phone_number': self.phone_number,
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'allow_flashcall': self.allow_flashcall,
            'current_number': self.current_number,
            'captcha_token': self.captcha_token,
            'captcha_answer': self.captcha_answer.to_dict() if isinstance(self.captcha_answer, TLObject) else self.captcha_answer
        }

    def _bytes(self):
        assert ((self.allow_flashcall or self.allow_flashcall is not None) and (self.current_number or self.current_number is not None)) or ((self.allow_flashcall is None or self.allow_flashcall is False) and (self.current_number is None or self.current_number is False)), 'allow_flashcall, current_number parameters must all be False-y (like None) or all me True-y'
        assert ((self.captcha_token or self.captcha_token is not None) and (self.captcha_answer or self.captcha_answer is not None)) or ((self.captcha_token is None or self.captcha_token is False) and (self.captcha_answer is None or self.captcha_answer is False)), 'captcha_token, captcha_answer parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\x94\xee\x80w',
            struct.pack('<I', (0 if self.allow_flashcall is None or self.allow_flashcall is False else 1) | (0 if self.current_number is None or self.current_number is False else 1) | (0 if self.captcha_token is None or self.captcha_token is False else 2) | (0 if self.captcha_answer is None or self.captcha_answer is False else 2)),
            self.serialize_bytes(self.phone_number),
            b'' if self.current_number is None or self.current_number is False else (b'\xb5ur\x99' if self.current_number else b'7\x97y\xbc'),
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            b'' if self.captcha_token is None or self.captcha_token is False else (self.serialize_bytes(self.captcha_token)),
            b'' if self.captcha_answer is None or self.captcha_answer is False else (self.captcha_answer._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _allow_flashcall = bool(flags & 1)
        _phone_number = reader.tgread_string()
        if flags & 1:
            _current_number = reader.tgread_bool()
        else:
            _current_number = None
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        if flags & 2:
            _captcha_token = reader.tgread_string()
        else:
            _captcha_token = None
        if flags & 2:
            _captcha_answer = reader.tgread_object()
        else:
            _captcha_answer = None
        return cls(phone_number=_phone_number, api_id=_api_id, api_hash=_api_hash, allow_flashcall=_allow_flashcall, current_number=_current_number, captcha_token=_captcha_token, captcha_answer=_captcha_answer)


class SignInRequest(TLRequest):
    CONSTRUCTOR_ID = 0xbcd51581
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, phone_number: str, phone_code_hash: str, phone_code: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def to_dict(self):
        return {
            '_': 'SignInRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'phone_code': self.phone_code
        }

    def _bytes(self):
        return b''.join((
            b'\x81\x15\xd5\xbc',
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
            self.serialize_bytes(self.phone_code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        _phone_code = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash, phone_code=_phone_code)


class SignUpRequest(TLRequest):
    CONSTRUCTOR_ID = 0x80eee427
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            '_': 'SignUpRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def _bytes(self):
        return b''.join((
            b"'\xe4\xee\x80",
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
            self.serialize_bytes(self.first_name),
            self.serialize_bytes(self.last_name),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        _first_name = reader.tgread_string()
        _last_name = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash, first_name=_first_name, last_name=_last_name)

