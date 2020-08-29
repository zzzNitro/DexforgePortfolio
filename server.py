from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def pablo_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_contact', methods=['POST', 'GET'])
def submit_contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/gracias.html')
    else:
        return 'Hubo un problema, intenta de nuevo.'
