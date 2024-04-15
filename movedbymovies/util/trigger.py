# flake8:noqa
from typing import Any
from datetime import date


class Trigger:
    @classmethod
    def make_log(cls, motivation: str, username: str, deleted_user: str, db):
        db.execute(
            'INSERT INTO log_deletes (delete_date, username, motivation, deleted_username) VALUES (?,?,?,?)',
            (date.today(), username, motivation, deleted_user)
        )
        db.commit()
