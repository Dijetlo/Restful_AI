#!/usr/bin/env python3
import http.server
'''
   REQUIRES: Python 3.6    UNTESTED ON: PYTHON 3.5
   Reason: Interpolitive strings used throughout.
   - Designed for minimal in memory footprint
   - Maximizes extensibility 
   - Uses only modules from the python 3.6 STL:
       Simplifies implementation - no 'Requirements.txt' to fullfill in secure environments.
       No external module versioning issues to track.
   Installation: 
   - Move this file and the accompanying lcs_responses.py into the same directory.
   - Run this file. Requires elevated permissions for socket access

'''
class API_Endpoint(http.server.BaseHTTPRequestHandler):
    
    def do_HEAD():
        pass

    def do_GET(self):
        pass

    def do_POST(self):
        import cgi
        
        self.ctype, self.pdict = cgi.parse_header(self.headers.get('content-type'))
        self.post_str = self.rfile.read((int(self.headers.get('Content-Length')))).decode('utf-8')    
        
        if self.path.endswith('/api/v1/lcs'):
            import json, lcs_responses as answer

            self.con_type = "application/json"
            if len(self.post_str) == 0:
                answer.no_data(self)
                print('No Data Recieved')
                return
            
            try:
                self.post_dict = json.loads(self.post_str)
            except json.decoder.JSONDecodeError as malformed_json:
                self.post_dict = {}
                answer.malformed_json(self)
                print(malformed_json)
                return
        
            if self.ctype != self.con_type:
                answer.bad_format(self)
                print(f'{self.ctype} recieved. BAD FORMAT')
                return

            self.vals = set()
            [self.vals.add(i['value']) for i in self.post_dict['setOfStrings']]
            self.lv = len(self.vals) 
            if self.lv != len(self.post_dict['setOfStrings']):
                answer.dupes(self)
                return
            
        answer.ok(self,[str(i) for i in self.vals])
        return

def main(serv_on):
    try:
        server = http.server.HTTPServer((serv_on), API_Endpoint)
        print(f"API_Endpoint is running @ {serv_on[0]} on port {serv_on[1]}")
        server.serve_forever()

    except KeyboardInterrupt as breakEndpoint:
        print('\n\tShutdown Has Been Called,\n\tAPI_Endpoint Server Out')
    server.socket.close()

if __name__=='__main__':
    
    main(('127.0.0.1', 7777))
