import threading

from sqlalchemy import Column, String

from DCManeger.modules.sql import BASE, SESSION


class dcChats(BASE):
    __tablename__ = "dc_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


dcChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_dc(chat_id):
    try:
        chat = SESSION.query(dcChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_dc(chat_id):
    with INSERTION_LOCK:
        dcchat = SESSION.query(dcChats).get(str(chat_id))
        if not dcchat:
            dcchat = dcChats(str(chat_id))
        SESSION.add(dcchat)
        SESSION.commit()


def rem_dc(chat_id):
    with INSERTION_LOCK:
        dcchat = SESSION.query(dcChats).get(str(chat_id))
        if dcchat:
            SESSION.delete(dcchat)
        SESSION.commit()
