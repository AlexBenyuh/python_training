# -*- coding: utf-8 -*-
from model.credentials import Credentials

def test_success_login_mk(app):
    app.cas.wrong_password(Credentials(login="380961451058", password="MK2prod_20"))


