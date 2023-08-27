from src.decorating.main import validate_types
import pytest

@validate_types(str)
def something(string: str):
    print(string)

def test_validate_types():
    something("This should work")
    assert True # If the previous function fails, this line shouldn't be executed

@pytest.mark.parametrize(
        "value",
        (
            13,
            True,
            list("yeah"),
            15.2
        )
)
def test_validate_types_failing(value):
    with pytest.raises(TypeError):
        something(value)


# more tests by Bito
@pytest.mark.parametrize("arg_types, args, kwargs, expected_result", [
    ((int, str), (10, "hello"), {}, None),
    ((int, str), ("10", "hello"), {}, TypeError),
    ((int,), (10,), {}, None),
    ((int,), ("10",), {}, TypeError),
    ((str,), ("hello",), {}, None),
    ((str,), (10,), {}, TypeError),
])
def test_validate_types_bito(arg_types, args, kwargs, expected_result):
    @validate_types(*arg_types)
    def dummy_function(*args, **kwargs):
        pass
    
    if expected_result is None:
        assert dummy_function(*args, **kwargs) is None
    else:
        with pytest.raises(expected_result):
            dummy_function(*args, **kwargs)