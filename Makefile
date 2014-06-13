test:
	python test_fork.py

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lines:
	find . -name "*.py"|xargs cat|wc -l
