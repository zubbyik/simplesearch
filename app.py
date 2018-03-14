from json import JSONEncoder
import unicodedata
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle
from flask import Flask, redirect, request, render_template, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['DEBUG'] = True
SECRET_KEY = '1234567890'

class Base:
    def __init__(self, form):
        self.form = {}


class ProductSearchForm(Form):
    product = StringField('Product')
    advanced_filter = StringField('Advanced Filter')
    submit_button = SubmitField('Submit Request')


@app.route('/', methods=['GET', 'POST'])
def cseacher():
    base = Base({})
    print(request.method)
    base.form = ProductSearchForm(csrf_enabled=False)
    if base.form.validate_on_submit():
        print("validated")
        print(base.form.product.data)
        return redirect(url_for('results', form=base.form))
    return render_template('form.html', form=base.form)


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        return {'_python_object': pickle.dumps(obj)}


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


base = Base({})
rsearch = dumps(base.form, cls=PythonObjectEncoder)
result = loads(rsearch, object_hook=as_python_object)


@app.route('/results')
def results():
    message = request.args['_python_object']
    rsearch2 = request.args[result]
    return render_template('results.html', message=message, rsearch2=rsearch2)


# @app.route('/')
# def index():
#     return "Hello Flask"
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)
