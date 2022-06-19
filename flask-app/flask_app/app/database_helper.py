from .models import db


def get_all_data(model):
    return model.query.all()


def add_data(model, **kwargs):
    new_row = model(**kwargs)
    db.session.add(new_row)
    db.session.commit()
