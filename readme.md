- get the api and put it in the right place,
  e.g. C:\Python27\Lib\site-packages\WalabotAPI.py
- modify the file if necessary
  I saw a unicode error, so fixed it by modifying line 29 (last line of Init()): "s/libPath/str(libPath)"
- run wall-scanner.py, switch the `profile` setting if desired
- run the official examples