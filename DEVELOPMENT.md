# Prerequisites
* install pipx
* install cookiecutter from pipx
* install poetry from pipx

# Building the initial project
```sh
cookiecutter https://github.com/tbennett6421/pythoncookie
```

# Initializing poetry
```sh
poetry add python-barcode
poetry add python-barcode[images]
git add poetry.lock
```

# Running the tool with poetry
```sh
poetry run genbarcode
poetry run genbarcode -h
poetry run genbarcode -d "9400123456789999876500"   # USPS sample
poetry run genbarcode -d "1Z9999999999999999"       # UPS sample
poetry run genbarcode -d "123456789012"             # Fedex sample
```

# Building wheels
```sh
poetry build
```

# Publishing wheel to remote
```sh
# Configure Test-PyPi
poetry config repositories.testpypi https://test.pypi.org/legacy/
# Push to Test-PyPi
poetry publish -r testpypi

# test-pypi doesn't have the same packages as pypi, so
# you should have an env that resembles your build env
python -m venv env/
./env/bin/activate
pip install -r requirements.txt
pipx install PKG_NAME

# ensure it works
cat unit-tests.txt

# Publish to prod-pypi
poetry publish
```
