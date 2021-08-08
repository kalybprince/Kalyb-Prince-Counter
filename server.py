from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    return render_template("index.html")

@app.route('/count', methods=['POST'])
def counter():
    if request.form['button'] == 'refresh':
        pass
    elif request.form['button'] == 'addtwo':
        session['count'] += 1
    elif request.form['button'] == 'reset':
        return redirect('/destroy_session')
    
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    del session['count']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
