# Introduction
Downloading heros' img from [https://pvp.qq.com/](https://pvp.qq.com/) based on Muti-thread.
# Install
```bash
pip install -r requirements.txt
```
# Usage
```
git clone https://github.com/XavierJiezou/python-crawl-learning.git
cd python-crawl-learning
python app_3.py
```
# Build
```bash
pipenv install
pipenv shell
pip install -r requirements.txt
pip install pyinstaller
pyinstaller -F -i favicon.ico app_3.py
pipenv --rm
```