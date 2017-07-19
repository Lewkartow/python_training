__author__ = 'Алексей'
from model.group import Group

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Modified group name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="Modified group header"))
    app.session.logout()

def test_modify_group_footer_and_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Modified name both", footer="Modified group footer both"))
    app.session.logout()