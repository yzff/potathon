"""
This module contains the class used to communicate with Telegram's servers
in plain text, when no authorization key has been created yet.
"""
import struct
import logging

from .mtprotostate import MTProtoState
from ..errors import InvalidBufferError
from ..extensions import BinaryReader


class MTProtoPlainSender:
    """
    MTProto Mobile Protocol plain sender
    (https://core.telegram.org/mtproto/description#unencrypted-messages)
    """
    def __init__(self, connection, *, loggers):
        """
        Initializes the MTProto plain sender.

        :param connection: the Connection to be used.
        """
        self._state = MTProtoState(auth_key=None, loggers=loggers)
        self._connection = connection

    async def send(self, request):
        """
        Sends and receives the result for the given request.
        """
        body = bytes(request)
        msg_id = self._state._get_new_msg_id()
        logging.info("send msg len: %d", len(body))
        data = struct.pack('<qqi', 0, msg_id, len(body)) + body
        logging.info(data)
        await self._connection.send(data)

        logging.info("recv...")
        body = await self._connection.recv()
        logging.info("recv data len: %d", len(body))
        if len(body) < 8:
            raise InvalidBufferError(body)

        logging.info(body)
        with BinaryReader(body) as reader:
            auth_key_id = reader.read_long()
            assert auth_key_id == 0, 'Bad auth_key_id'

            msg_id = reader.read_long()
            assert msg_id != 0,  'Bad msg_id'
            # ^ We should make sure that the read ``msg_id`` is greater
            # than our own ``msg_id``. However, under some circumstances
            # (bad system clock/working behind proxies) this seems to not
            # be the case, which would cause endless assertion errors.

            length = reader.read_int()
            assert length > 0,  'Bad length'
            # We could read length bytes and use those in a new reader to read
            # the next TLObject without including the padding, but since the
            # reader isn't used for anything else after this, it's unnecessary.
            return reader.tgread_object()
