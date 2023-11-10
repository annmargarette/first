from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contacts():
    return render_template('contacts.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)






@app.route('/areaOfcirle', methods=['GET', 'POST'])
def Area():
    result = None
    if request.method == 'POST':
        input_integer = int(request.form.get('inputInteger', ''))
        result = 3.14 * (input_integer**2)
    return render_template('areaofacircle.html', result=result)
    
@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def AreaT():
    result = None
    if request.method == 'POST':
        input_base = int(request.form.get('inputBase', ''))
        input_height = int(request.form.get('inputHeight', ''))
        result = (input_base*input_height)/2
    return render_template('areaofatriangle.html', result=result)
    

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

if __name__ == "__main__":
    app.run(debug=True)
