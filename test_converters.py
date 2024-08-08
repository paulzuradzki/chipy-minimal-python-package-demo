from converters import celsius_to_fahrenheit, fahrenheit_to_celsius
import pytest
import hypothesis.strategies as st


@pytest.mark.parametrize(
    "celsius, fahrenheit",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
        (20, 68),
    ],
)
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    # Act
    result = celsius_to_fahrenheit(celsius)
    expected = fahrenheit

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "fahrenheit, celsius",
    [
        (32, 0),
        (212, 100),
        (-40, -40),
        (98.6, 37),
        (68, 20),
    ],
)
def test_fahrenheit_to_celsius(fahrenheit, celsius):
    # Act
    result = fahrenheit_to_celsius(fahrenheit)
    expected = celsius

    # Assert
    assert result == expected


from hypothesis import given, strategies as st


@given(
    celsius=st.one_of(
        st.floats(min_value=-500, max_value
                  =500),
        st.integers(min_value=-500, max_value=500),
    ),
)
def test_roundtrip(celsius):
    """Check converting from Celsius to Fahrenheit and back to Celsius.
    
    We should end up with original value. E.g., "decode(encode(x)) == x".
    """
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(celsius)) == pytest.approx(
        celsius
    )
