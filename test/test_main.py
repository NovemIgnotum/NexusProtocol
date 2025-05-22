def test_true_is_true():
    assert True == True

def test_hello_world(capsys):
    print("Hello, le monde")
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"