# Restful AI --- The AI stands for Automated Infrastructure, not the other thing...
## webserver36
Python 3.6 web server:
- Requirement: Python3.6 only - no modules external to the python 3.6 STL
* Currently tested on python3.6 only. Use of interpolitive strings restricts earlier versions.
- Simple web server currently implemented with a "longest common substring " gizmo attached at /lcs
- Set to use localhost on port 7777 (localhost:7777//api/v1/lcs)

### Installation
There are no dependencies outside the python3.6 Standard Template Library asociated with this web server. 
Batteries included.
Currently this is a single use implementation for the lcs functionality so the file "lcs_responses.py" from this git is also required. The two files, webserver36.py and lcs_responses.py must live in the same directory.

- Downloade webser36.py and lcs_responses.py to the execution directory of your choosing
- Mark them as executable based on the operating system you are using

Execution String: /path/to/your/python3.6/binaries webserver36.py

### Goals:
- Micro service Dev/Ops tool that retains idempotency and is aplicable to the widest number of use cases. See wiki

