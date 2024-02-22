install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
    python -m unittest discover tests


lint:
    pylint my_module.py

clean:
    rm -rf __pycache__
