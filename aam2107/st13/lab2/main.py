from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from .config import Config
from .Spisok import Spisok

app = Flask(__name__)
app.config.from_object(Config)


class Form(FlaskForm):
    text = SelectField('input', choices=[1, 2, 3, 4, 5, 6, 7])
    submit = SubmitField('send')


class FormAdding(FlaskForm):
    selector = SelectField('input', choices=['Student', 'Starosta'])
    submit = SubmitField('send')


class FormStudent(FlaskForm):
    name = StringField('name')
    group = StringField('group')
    submit = SubmitField('send')


class FormStarosta(FlaskForm):
    name = StringField('name')
    group = StringField('group')
    doppole = StringField('doppole')
    submit = SubmitField('send')


class FormOnDelete(FlaskForm):
    selector = IntegerField('input')
    submit = SubmitField('send')


obj = Spisok()
textdata = ""
changeindex = 0


@app.route('/2/Starosta', methods=['POST', 'GET'])
def index2Star():
    form = FormStarosta()
    if form.validate_on_submit():
        obj.functions[2](1, changeindex, form.name.data, form.group.data, form.doppole.data)
        return redirect('/')
    return render_template("1Star.html", form=form)


@app.route('/2/Student', methods=['POST', 'GET'])
def index2Stud():
    form = FormStudent()
    if form.validate_on_submit():
        obj.functions[2](1, changeindex, form.name.data, form.group.data)
        return redirect('/')
    return render_template("1Stud.html", form=form)


@app.route('/2', methods=['POST', 'GET'])
def index2():
    form = FormOnDelete()
    if form.validate_on_submit():
        global changeindex
        changeindex = form.selector.data
        if obj.functions[9](changeindex) == 1:
            return redirect("/2/Student")
        else:
            return redirect("/2/Starosta")
    return render_template("1.html", form=form)


@app.route('/3', methods=['POST', 'GET'])
def index3():
    form = FormOnDelete()
    if form.validate_on_submit():
        obj.functions[3](form.selector.data)
        return redirect('/')
    return render_template("1.html", form=form)


@app.route('/1/Starosta', methods=['POST', 'GET'])
def index1star():
    form = FormStarosta()
    if form.validate_on_submit():
        obj.functions[1](2, form.name.data, form.group.data, form.doppole.data)
        return redirect('/')
    return render_template("1Star.html", form=form)


@app.route('/1/Student', methods=['POST', 'GET'])
def index1stud():
    form = FormStudent()
    if form.validate_on_submit():
        obj.functions[1](1, form.name.data, form.group.data)
        return redirect('/')
    return render_template("1Stud.html", form=form)


@app.route('/1', methods=['POST', 'GET'])
def index1():
    form = FormAdding()
    if form.validate_on_submit():
        if form.selector.data == "Student":
            return redirect('/1/Student')
        else:
            return redirect('/1/Starosta')
    return render_template("1.html", form=form)


@app.route('/', methods=['POST', 'GET'])
def index():
    global obj
    global textdata
    form = Form()
    if form.validate_on_submit():
        switch = int(form.text.data)
        if switch == 1:
            return redirect('/1')
        elif switch == 2:
            return redirect('/2')
        elif switch == 3:
            if obj.functions[8]() != 0:
                return redirect('/3')
            else:
                textdata = "List is empty"
                return redirect('/')
        elif switch == 4:
            textdata = obj.functions[switch]()
            return redirect('/')
        elif (switch <= 7) or (switch >= 5):
            textdata = obj.functions[switch]()
            return redirect('/')
    return render_template("base.html", text=textdata, form=form)


def main():
    app.run(debug=False)


if __name__ == "__main__":
    main()
