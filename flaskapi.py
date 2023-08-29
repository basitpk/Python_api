import flask
 
app = flask.Flask(__name__, static_folder="dbfiles")
# app.config["DEBUG"] = True
# app.config["SERVER_NAME"]="0.0.0.0:4443"
 
@app.route('/', methods=["GET"])
def home():
    return "<h1>Download Gzip and a text file from remote server.</p>"
 
@app.route('/myfile', methods=["GET", "POST"])
def getbotnet():
    return flask.send_from_directory(directory="dbfiles", path="Myfile.gz", as_attachment=True)
 
@app.route('/abcd', methods=["GET", "POST"])
def getgeoip():
    return flask.send_from_directory(directory="dbfiles", path="abcd.gz", as_attachment=True)
    
@app.route('/botip', methods=["GET", "POST"])
def getdeag():
    return flask.send_from_directory(directory="dbfiles", path="bottIp.txt", as_attachment=True)    
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000',ssl_context='adhoc')
