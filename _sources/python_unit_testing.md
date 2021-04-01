# Pytest

Using `Vscode` and `pytest`.

Two files:
1. `filename.py` - where the program is written
2. `test_filename.py` - where the tests are written
    * `test_` prefix lets vscode know that the test are here, this also applies to the functions 

## Program file: `filename.py`

```python
def returnInputPlusFive(numberInput):
    return numberInput + 5


def returnInputPlusTwo(numberInput):
    return numberInput + 2


class SomeClass:
    def returnInputPlusTen(self, numberInput):
        return numberInput + 10

```

## Test file: `test_filename.py`
The `class` method test initiates the test class object then runs the test

```python
import filename


def test_returnInputPlusFive():
    assert filename.returnInputPlusFive(3) == 8


def test_returnInputPlusTwo():
    assert filename.returnInputPlusTwo(3) == 5


def test_returnInputPlusTen():
    newObj = filename.SomeClass()
    assert newObj.returnInputPlusTen(10) == 20
```
