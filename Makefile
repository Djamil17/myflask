.ONESHELL: # Applies to every targets in the file!

PYTHON_VERSION := $(shell python3 -c "import sys;print('{}.{}'.format(*sys.version_info[:2]))")

# name
.venv:
	python3 -m venv .venv
	. .venv/bin/activate; pip install -e .[dev,test]

venv: .venv

# setup
test: .venv
	. .venv/bin/activate; python3 -m floor_checks dlakhdar-hamina@researchdata.us dlakhdar-hamina@researchdata.us

lambda_function.zip: .venv src/*.py
	. .venv/bin/activate; pip install --target lambda_function .
	cd lambda_function; zip -r ../lambda_function.zip .

package: lambda_function.zip

deploy: lambda_function.zip
	tofu init
	tofu validate
	tofu plan
	tofu apply

clean:
	rm -rf .venv
