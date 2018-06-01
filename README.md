# webserver36
Python 3.6 web server:
- Requirement: Currently tested on python3.6 only. Use of interpolitive strings restricts earlier versions.
- Simple web server currently implemented with a "longest common substring " gizmo attached at /lcs
- Set to use localhost on port 7777 (localhost:7777//api/v1/lcs)

## Installation
There are no dependencies outside the python3.6 Standard Template Library asociated with this web server. 
Batteries included.
Currently this is a single use implementation for the lcs functionality so the file "lcs_responses.py" from this git is also required. The two files, webserver36.py and lcs_responses must live in the same directory.

- Downloade webser36.py and lcs_resonses.py to the executoin directory of your choosing
- Mark them as executable based on the operating system you are using
###  --> /path/to/your/python3.6/binaries webserver36.py

### Longest Common String -
header: application/json
body
{ "setOfStrings" : [{“value" : "string1"}, {“value" : "string2”}, {“value" : "String 3 yeah, this works too”}] }
location: /api/v1/lcs

Dictionary key must be string value "value", other than that you feed it anything you can type. Broken val i.e. "Erp, Derpa, Derp" are righteous voodoo as far as this gizmo is concerned. 
