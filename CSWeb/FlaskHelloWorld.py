from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("lucas.html")

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    with open('submissions.txt', 'a') as f:
        f.write(f"{fname} {lname}\n")
    if fname.lower() == 'audieezy':
        return render_template("easter.html")
    return render_template("welcome.html", fname=fname, lname=lname)

@app.route('/car', methods=['POST'])
def car():
    choice = request.form['cars']
    with open('car_choices.csv', 'a') as f:
        f.write(f"{choice}\n")
    return render_template("car.html", car=choice)

if __name__ == '__main__':
    app.run(debug=True)