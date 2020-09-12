# -*- coding: utf-8 -*-
from model.credentials import Credentials


def test_success_login_mk(app):
    app.session.login(Credentials(login="38096000000", password="xxx"))
    app.mk.hello_mk()
    app.mk.merge_from_mk()
    app.session.logout()
