from app.domain import db
from app.domain.user import User


def get_users():
    return User.query.all()


def create_user(name, password, user_role):
    user = User()
    user.name = name
    user.password = password
    user.role = user_role
    db.session.add(user)
    db.session.commit()
    return user


def change_password(user_id, new_password):
    user = User.query.get(user_id)
    user.password = new_password
    user.is_first_login = 1
    db.session.commit()
    return user


def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return user
