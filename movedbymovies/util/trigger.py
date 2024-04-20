from datetime import date
from typing import Any


class Trigger:
    @classmethod
    def delete(cls, admin_id: int, motivation: str, db: Any):

        db.execute(
            """INSERT INTO logs
            (type_operation, admin_id, motivation, delete_date)
            VALUES (?,?,?,?,?)""",
            ('Delete', admin_id, motivation, date.today())
        )
        db.commit()

    @classmethod
    def movie_registered(cls, admin_id: int, db: Any):
        db.execute(
            """INSERT INTO logs
            (type_operation, admin_id,
            motivation, delete_date)
            VALUES (?,?,?,?,?)""",
            ('Movie registered', admin_id, 'movie added', date.today())
        )
        db.commit()
