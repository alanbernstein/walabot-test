# API
- http://api.walabot.com/_pythonapi.html
- get the API python file and put it in the right place, e.g. C:\Python27\Lib\site-packages\WalabotAPI.py
- I got a unicode error trying to use it, so copy the (probably out of date) version from this repo, or copy the change I made - line 29 (last line of Init()): "s/libPath/str(libPath)"

# examples
- run wall-scanner.py, switch the `profile` setting if desired
- run the official examples