from assistant.rules import reply

def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_reply_partial_office_name_training():
    ans = reply("where is training?")
    assert "Training Office" in ans
    assert "room" in ans


def test_reply_partial_office_name_helpdesk():
    ans = reply("when does the helpdesk open?")
    assert "IT Helpdesk" in ans
    assert "open" in ans
