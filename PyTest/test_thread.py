import datetime

import pytest
from reply import Reply
from thread import Thread


@pytest.fixture
def thread():
    """This fixture returns a Thread object"""
    title = "Hello, World!"
    user = "user1"
    replies = [
        Reply("Hello, World!", "user1", datetime.datetime(2023, 1, 1, 0, 0, 0)),
        Reply("Goodbye, World!", "user2", datetime.datetime(2023, 1, 2, 0, 0, 0)),
    ]
    return Thread(title, user, replies)


def test_init():
    title = "Hello, World!"
    user = "user1"
    replies = [
        Reply("Hello, World!", "user1", datetime.datetime(2023, 1, 1, 0, 0, 0)),
        Reply("Goodbye, World!", "user2", datetime.datetime(2023, 1, 2, 0, 0, 0)),
    ]

    thread = Thread(title, user, replies)

    assert thread.title == "Hello, World!"
    assert thread.user == "user1"
    assert thread.replies == replies


def test_repr(thread):
    assert repr(thread) == "<Thread 'Hello, World!' by 'user1'>"


def test_reply(thread):
    new_reply = Reply("Hello, World!", "user1", datetime.datetime(2023, 1, 3, 0, 0, 0))

    thread.reply(new_reply)

    assert new_reply in thread.replies


def test_reply_more_recent(thread):
    new_reply = Reply("Hello, World!", "user1", datetime.datetime(2023, 1, 1, 0, 0, 0))

    with pytest.raises(ValueError):
        thread.reply(new_reply)