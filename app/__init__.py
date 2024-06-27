#!/usr/bin/env python3
# -*-coding: utf8 -*-
"""About Me"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def About_me():
    list = ["first_name: Amber", "last_name: Patton", "Hobby: Playing drums poorly"]
    bullet_list = "".join(
        "<li>%s</li>" % list for list in list
    )
    return "<ul>%s</ul>" % bullet_list 