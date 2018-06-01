# webserver36
Python 3.6 web server:
- Requirement: Currently tested on python3.6 only. Use of interpolitive strings restricts earlier versions.
- Simple web server currently implemented with a "longest common substring " gizmo attached at /lcs
- Set to use localhost on port 7777 (localhost:7777//api/v1/lcs)

## Installation
There are no dependencies outside the python3.6 Standard Template Library asociated with this web server. 
Batteries included.
Currently this is a single use implementation for the lcs functionality so the file "lcs_responses.py" from this git is also required. The two files, webserver36.py and lcs_responses.py must live in the same directory.

- Downloade webser36.py and lcs_responses.py to the execution directory of your choosing
- Mark them as executable based on the operating system you are using

Execution String: /path/to/your/python3.6/binaries webserver36.py

### Longest Common String -
header: application/json -

body:
{ "setOfStrings" : [{“value" : "string1"}, {“value" : "string2”}, {“value" : "String 3 yeah, this works too”}] }

location: /api/v1/lcs

Top leve dictionary must have key 'setOfStrings' sub key must be string "value".
Broken subkey values - i.e. { "value" : "Erp, Derpa, Derp"} get split on the white space and tossed in the word chipper along with the rest.
