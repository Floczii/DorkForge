from flask import Flask, render_template, request

app = Flask(__name__)

#basic : intitle, inurl, filetype, site, intext
#advanced : related, cache, link, daterange
#operators : "", +, -, OR
def forge(form):

  requests = ["intext","inurl","intitle","filetype","site"]

  inputs = [form['intext'],form['inurl'],form['intitle'],form['filetype'],form['site']]

  res = ""
  i = 0
  for s in inputs:
    if s != "":
      print(s)
      res += "{}:\"{}\" ".format(requests[i],inputs[i])
    i += 1
  
  
  return res

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/',methods = ['POST'])
def resultat():
  form = request.form
  dork = forge(form)
  return render_template("index.html", dork=dork)

if __name__ == "__main__":
    app.run()