__author__ = 'Алексей'
import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list(1)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert  contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphonephone == clear(contact_from_edit_page.workphonephone)
    assert contact_from_home_page.mobilephonephone == clear(contact_from_edit_page.mobilephonephone)
    assert contact_from_home_page.seconderyphone == clear(contact_from_edit_page.seconderyphone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert  contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphonephone == contact_from_edit_page.workphonephone
    assert contact_from_view_page.mobilephonephone == contact_from_edit_page.mobilephonephone
    assert contact_from_view_page.seconderyphone == contact_from_edit_page.seconderyphone


def clear(s):
    return re.sub("[ () -]", "", s)