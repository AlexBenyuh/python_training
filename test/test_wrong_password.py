# -*- coding: utf-8 -*-
from model.credentials import Credentials

def test_success_login_mk(app):
    app.cas.wrong_password(Credentials(login="380960000000", password="1"))


