from flask import Flask, render_template

app =  Flask(__name__)

@app.route('/')
def home1():
    # return "Homepage here!"
    return render_template("home1.html")
@app.route('/about/')
def about():
    # return "About content goes here!"
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)
