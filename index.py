from flask import Flask, render_template, url_for, abort
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('base.html'), 200

#@app.route('/Playstation-4')
#def root_Playstation-4():
   # return render_template('Playstation-4.html')

@app.route('/img')
def img():
  start = '<img src="'
  url = url_for('static', filename='uncharted4.jpg')
  end = '">'
  return start+url+end, 200

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

