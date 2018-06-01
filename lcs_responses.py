#!/usr/bin/env python3

def ok(self, vals):
    from difflib import SequenceMatcher

    current_set =  ''
    if vals:
        tvals=[]
        for i in vals:
            while ' ' in i:
                split_val = list(i.split(" "))
                [tvals.append(s) for s in split_val]
                vals.remove(i)
                break
        [vals.append(e) for e in tvals]
    print(f' Initial value set: {vals}')
    champ = vals.pop(len(vals)-1)

    while len(vals):
        challenger = vals.pop(len(vals)-1)
        print(challenger,vals)
        seq = SequenceMatcher(None, champ, challenger)
        hits = seq.find_longest_match(0, len(champ), 0, len(challenger))
        if (hits.size!=0):
            current_set = (champ[hits.a: hits.a + hits.size])
        else:
            current_set = 'No matching substrings across set'
            break
        if len(vals) == 0:
            break
    self.send_response(200)
    self.send_header('content-type', 'application/json')
    self.end_headers()
    output = ""
    output += "<html><head><title>API Endpoint Server</title></head>"
    output += "<h1>Longest Chain in Set</h1>"
    output += "--------------------------"
    output += f"<h2>{current_set}</h2></html>"
    self.wfile.write(bytes(output, "utf-8"))

def bad_format(self):
    self.send_response(400)
    self.send_header('content-type', 'application/json')
    self.end_headers()
    output = ""
    output += "<html><head><title>API Endpoint Server</title></head>"
    output += f"<body><h1>ERROR 400: REQUEST NOT IN {self.con_type} FORMAT</h1>"
    output += f"<h2>These ReSTful Endpoints Use {self.con_type}</h2>"
    output += "<h2>You, on the other hand, do no such thing.</h2>"
    output += f"<p>You sent {self.ctype} and it left us wondering...\n"
    output += f"\t\tWhy you hatin\' on {self.con_type} dog?</p>"
    output += "</body></html>"
    self.wfile.write(bytes(output, "utf-8"))

def malformed_json(self):
    self.send_response(400)
    self.send_header('content-type', 'application/json')
    self.end_headers()
    output = ""
    output += "<html><head><title>API Endpoint Server'</title></head>"
    output += f"<body><h1>ERROR 400: HOSED UP {self.con_type}:</h1>"
    output += "<h2>Who told you this was acceptable? </h2>"
    output += "<h2>STOP TRYING TO BREAK THE INTERNET</h2>"
    self.wfile.write(bytes(output, "utf-8"))


def no_data(self):
    self.send_response(204)
    self.send_header('content-type', 'application/json')
    self.end_headers()
    output = ""
    output += "<html><head><title>API Endpoint Server</title></head>"
    output += "<body><h1>RESPONSE: 204 EMPTY REQUEST FULLFILLED</h1>"
    output += "<h2>Attention: YOU ARE FIRING BLANKS</h2>"
    output += "<h2>You sent no data whatsoever, none, nada, zip, bolo</h2></body></html>"
    self.wfile.write(bytes(output, "utf-8"))

def dupes(self,):    
    self.send_response(200)
    self.send_header('content-type', 'application/json')
    self.end_headers()
    output = ""
    output += "<html><head><title>API Endpoint Server</title></head>"
    output += "<h1>RESPONSE 200: YOU GOT DUPES<h1>"
    output += "<h2>Duplicate values in your dictionary, man...<h1>"
    output += "<h3> You know that aint right...</h3></html>"
    self.wfile.write(bytes(output, "utf-8"))
    return
