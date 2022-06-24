from .models import db


def get_all_data(model):
    return model.query.all()


def add_data(model, **kwargs):
    new_row = model(**kwargs)
    db.session.add(new_row)
    db.session.commit()


def get_instance_or_add(model, **kwargs):
    """
    Returns an exisiting instance or
    creates a new instance & returns it
    """
    with db.session.begin():
        instance = db.session.query(model).filter_by(**kwargs).one_or_none()
        if not instance:
            new_row = model(**kwargs)
            db.session.add(new_row)
            db.session.commit()
    instance = db.session.query(model).filter_by(**kwargs).one_or_none()
    return instance
