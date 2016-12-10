from flask import Flask,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route("/school")
def school():
    return redirect("http://techkids.vn/")

@app.route('/bmi/<int:h>/<int:w>')
def bmi(w,h):
    BMI=(float(w))/((float(h)/100)**2)

    ketqua=""
    if BMI<16:
        ketqua="Severely underweight"
    elif BMI<18.5:
        ketqua="Underweight"
    elif BMI<25:
        ketqua="Normal"
    elif BMI<30:
        ketqua="Overweight"
    else:
        ketqua="Obese"
    return "So Bmi la{0} ket qua la {1}".format(BMI,ketqua)


if __name__ == '__main__':
    app.run()
