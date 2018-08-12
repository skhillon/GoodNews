#!/bin/bash
python3 Backend/app.py &
echo wait 15 seconds for backend
sleep 15
open -a "Google Chrome" Frontend/noReact/index.html
