import main


def test_while_1(capsys, monkeypatch):
    inputs = iter([7])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == '5040\n'


def test_while_2(capsys, monkeypatch):
    inputs = iter([0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_while()
    captured = capsys.readouterr()
    assert captured.out == '1\n'


def test_for_1(capsys, monkeypatch):
    inputs = iter([5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_for()
    captured = capsys.readouterr()
    assert captured.out == '120\n'


def test_while_1(capsys, monkeypatch):
    inputs = iter([0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main_for()
    captured = capsys.readouterr()
    assert captured.out == '1\n'
