from flask import Flask, render_template, request
from forms import *
from regular_expression import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='regex expression')


@app.route('/about/')
def about():
    return render_template('about.html', title='regex expression')


@app.route('/regex/', methods=['GET', 'POST'])
def regex():
    flags_checkers = FlagsForm()
    str_form = StringForm()
    matches = RegularExpression()
    if request.method == 'POST':
        form_name = request.form['form-name']
        if form_name == 'debug':
            flags = request.form.getlist('flag')
            flags_checkers.checker(flags, request.form.getlist('function'))
            str_form.regex_string = request.form['regex']
            str_form.test_string = request.form['test_string']
            str_form.subs_string = request.form['replace-string']
        else:
            flags_checkers.checker([form_name])
            str_form.regex_string, str_form.test_string = FlagExampleForm().get_regex_and_str(form_name)
        matches.find_matches(flags_checkers, '\'', str_form.regex_string, str_form.test_string, str_form.subs_string)
    return render_template('regex.html', title='regex expression', regex=regex, flags_checkers=flags_checkers,
                           str_form=str_form, matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
