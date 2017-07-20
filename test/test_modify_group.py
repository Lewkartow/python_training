__author__ = 'Алексей'
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Need someone group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Modified group name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

"""
def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Modified group header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer_and_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="Modified two fields", footer="Modified group footer both"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""