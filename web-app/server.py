from flask import Flask, request

app = Flask(__name__)

visitors = {}

def get_hit_count(remote_ip):
    if remote_ip in visitors:
        visitors[remote_ip] = visitors[remote_ip] + 1
    else:
        visitors[remote_ip] = 1
    hits = visitors[remote_ip]
    return hits

@app.route('/')
def hello():
    hits = get_hit_count(str(request.remote_addr))
    ip_res = "User Address: " + request.remote_addr
    hit_count = "\nHits: " + str(hits)
    return ip_res+hit_count

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)