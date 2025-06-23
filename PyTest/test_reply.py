import datetime

import pytest
from reply import Reply


def test_init():
    body = "Hello, World!"
    user = "user1"
    created = datetime.datetime.now()

    reply = Reply(body, user, created)

    assert reply.body == body
    assert reply.user == user
    assert reply.created == created


def test_repr():
    body = "Hello, World!"
    user = "user1"
    created = datetime.datetime(2023, 1, 1, 0, 0, 0)

    reply = Reply(body, user, created)
    expected_repr = f"<Reply from '{user}' on '2023-01-01 00:00'>"

    assert repr(reply) == expected_repr


def test_repr_without_date():
    body = "Hello, World!"
    user = "user1"
    created = "2021-02-07 12:00"

    reply = Reply(body, user, created)

    with pytest.raises(AttributeError):
        assert repr(reply) == f"<Reply from '{user}' on '2021-02-07 12:00'>"


def test_eq_same_values():
    body = "Hello, World!"
    user = "user1"
    created = datetime.datetime.now()

    reply1 = Reply(body, user, created)
    reply2 = Reply(body, user, created)

    assert reply1 == reply2


def test_eq_different_values():
    body1 = "Hello, World!"
    user1 = "user1"
    created1 = datetime.datetime.now()

    body2 = "Goodbye, World!"
    user2 = "user2"
    created2 = created1 + datetime.timedelta(minutes=1)

    reply1 = Reply(body1, user1, created1)
    reply2 = Reply(body2, user2, created2)

    assert reply1 != reply2


def test_eq_different_types():
    body = "Hello, World!"
    user = "user1"
    created = datetime.datetime.now()

    reply = Reply(body, user, created)
    non_reply = "Not a reply object"

    assert reply != non_reply