from flask import Blueprint, redirect, render_template, request, url_for
from app.domain import db
from app.domain.task import Task


bp_index = Blueprint(__name__, __name__)


@bp_index.route("/")
def home():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@bp_index.route("/create-task", methods=["POST"])
def create():
    new_task = Task(title=request.form["title"], text=request.form["text"])
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("view.index.home"))


@bp_index.route("/done/<id>")
def done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not (task.done)
    db.session.commit()
    return redirect(url_for("view.index.home"))


@bp_index.route("/delete/<id>")
def delete(id):
    Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("view.index.home"))
