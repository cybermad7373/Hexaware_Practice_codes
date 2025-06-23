from reply import Reply


class Thread:
    def __init__(self, title: str, user: str, replies: list[Reply] = None) -> None:
        self.title = title
        self.user = user
        self.replies = replies or []
    
    def __repr__(self) -> str:
        return f"<Thread '{self.title}' by '{self.user}'>"
    
    def reply(self, reply: Reply) -> None:
        if reply.created < self.replies[-1].created:
            raise ValueError("New reply is older than the last reply")
        self.replies.append(reply)