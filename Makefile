TARGET: requirements.txt wiki_cat.py
	@echo "First time install only"
	pip install virtualenv
	virtualenv -p /usr/bin/python3 venv
	@echo "Activate virtual environment with source venv/bin/activate command"
	
activate:
	( \
		source ./venv/bin/activate; \
		pip install -r requirements.txt; \
	)
	
uninstall:
	rm -R venv/
