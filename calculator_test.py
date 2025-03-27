from pytest import MonkeyPatch
import calculator
import io

def test_normal_numbers(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('3\n2'))
    calculator.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Zahl 1 ein: Gebe Zahl 2 ein: "
        "3.0 + 2.0 = 5.0\n"
        "3.0 - 2.0 = 1.0\n"
        "3.0 * 2.0 = 6.0\n"
        "3.0 / 2.0 = 1.5"
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()
    print("Captured output:", repr(output))
    assert output == expected_output

def test_floating_numbers(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('2.5\n-0.5'))
    calculator.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Zahl 1 ein: Gebe Zahl 2 ein: "
        "2.5 + -0.5 = 2.0\n"
        "2.5 - -0.5 = 3.0\n"
        "2.5 * -0.5 = -1.25\n"
        "2.5 / -0.5 = -5.0"
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()
    print("Captured output:", repr(output))
    assert output == expected_output

def test_division_by_zero(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('3\n0'))
    try:
        calculator.main()
    except ZeroDivisionError:
        assert True
    else:
        assert False, "Expected ZeroDivisionError but none was raised"

def test_negative_numbers(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('-3\n-2'))
    calculator.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Zahl 1 ein: Gebe Zahl 2 ein: "
        "-3.0 + -2.0 = -5.0\n"
        "-3.0 - -2.0 = -1.0\n"
        "-3.0 * -2.0 = 6.0\n"
        "-3.0 / -2.0 = 1.5"
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()

    assert output == expected_output

def test_large_numbers(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1000000\n2000000'))
    calculator.main()
    captured = capsys.readouterr()
    expected_output = (
        "Gebe Zahl 1 ein: Gebe Zahl 2 ein: "
        "1000000.0 + 2000000.0 = 3000000.0\n"
        "1000000.0 - 2000000.0 = -1000000.0\n"
        "1000000.0 * 2000000.0 = 2000000000000.0\n"
        "1000000.0 / 2000000.0 = 0.5"
    )
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()

    assert output == expected_output
