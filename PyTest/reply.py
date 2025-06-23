import datetime


class Reply:
    def __init__(self, body: str, user: str, created: datetime.datetime) -> None:
        self.body = body
        self.user = user
        self.created = created
    
    def __repr__(self) -> str:
        return f"<Reply from '{self.user}' on '{self.created.strftime('%Y-%m-%d %H:%M')}'>"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Reply):
            return False
        return (
            self.body == __value.body and
            self.user == __value.user and
            self.created == __value.created
        )