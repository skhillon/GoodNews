ps -ef | grep 'app.py' | grep -v grep | awk '{print $2}' | xargs kill -9
#ps aux | grep app.py | awk '{print $2}' | kill
