from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result14():
    if request.method == "POST":
        a = request.form.get("a")
        b = request.form.get("b")
        c = request.form.get("c")


        return render_template("result14.html", a=a, b=b, c=c)

    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
