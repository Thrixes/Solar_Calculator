from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('practice.html')               # Links HTML to Python/Flask

@app.route('/success/<int:score>')
def success(score):                                       # Seperate HTML file
    res =''
    if score >= 49:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', result = res)   # Links HTML to Python/Flask
    
@app.route('/fail/<int:score>')
def fail(score):                                          # Seperate HTML file
    return "The failing score is 49%, your score is: " + str(score) + "%"

# Result checker
@app.route('/results/<int:marks>')
def results(marks):
    if marks < 49:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score = marks))

#'/submit' is the URL for the page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["C"])
        data_science = float(request.form["datascience"])
        total_score = (science + maths + c + data_science)/4
    res = ''
    if total_score >=49:
        res = 'success'
    else:
        res = "fail"
    return redirect(url_for(res, score = total_score))
    

if __name__ == '__main__':
    app.run(debug = True)
