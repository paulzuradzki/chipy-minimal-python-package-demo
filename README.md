### Description

Scripts for converting temperature.

### Example usage

```python
from converters import celsius_to_fahrenheit, fahrenheit_to_celsius

celsius = 0
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
celsius_again = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {celsius_again}°C")
```

### Setup

Right now there are only dev dependencies (testing).

```bash
python3 -m venv .venv
source .venv/bin/activate
(.venv) python -m pip install --upgrade pip
(.venv) python -m pip install -r requirements.txt

# Installing from git
    # URL takes format: git+ssh://git@github.com/<user>/<repo>.git@<branch>#egg=<package_name>
    # change to HTTPS if you use password-based authentication with your GitHub account
(.venv) python -m pip install git+ssh://git@github.com/paulzuradzki/chipy-minimal-python-package-demo.git@main#egg=converters

```

### Testing

Testing and code quality.
```
pytest -vv
mypy converters.py --strict
```

# Creating Source or Binary Distribution

```bash
# source distribution (has Python source code)
$ python setup.py sdist
$ python -m pip install dist/converters-0.0.1.tar.gz 
```