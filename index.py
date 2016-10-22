from flask import Flask, render_template, url_for, abort
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('base.html'), 200

@app.route('/Playstation4/')
def root_Playstation4():
  return render_template('Playstation4.html'), 200

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

