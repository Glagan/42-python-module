pip install --upgrade pip 
pip install --upgrade setuptools
pip install --upgrade wheel
python setup.py sdist bdist_wheel
pip install ./dist/my_minipack-1.0.0.tar.gz
