# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.credentials import Credentials


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_cas2(app):
    app.login(Credentials(login="380961451058", password="MK2prod_2016"))
    app.hello_mk()
    app.logout()

