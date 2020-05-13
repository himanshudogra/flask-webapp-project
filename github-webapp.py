from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)

@app.route('/github', methods=['POST'])
def api_gh_msg():
    if request.headers['Content-Type'] == 'application/json':
        my_info = json.dumps(request.json)
        print (my_info)
        

if __name__ == '__main__':
    app.run(debug=True)