__author__ = 'Алексей'


def test_delete_first_group(app):
    app.session.logout()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()