import subprocess

subprocess.call('set FLASK_APP=root/flashcard.py', shell=True)
subprocess.call('export FLASK_APP=root/flashcard.py', shell=True)
subprocess.call('flask run', shell=True)
