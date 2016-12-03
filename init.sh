#!/bin/bash
pip install virtualenv
virtualenv -p /usr/bin/python3 venv
activate(){
	source venv/bin/activate
}
pip install -r requirements.txt
echo "Run sample code with python3 wiki_cat.py"
