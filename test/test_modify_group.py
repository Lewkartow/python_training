__author__ = 'Алексей'
from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Need someone group"))
    app.group.modify_first_group(Group(name="Modified group name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Modified group header"))


def test_modify_group_footer_and_name(app):
    app.group.modify_first_group(Group(name="Modified two fields", footer="Modified group footer both"))
