#!/usr/bin/python
# encoding: utf-8

from __future__ import unicode_literals

import os
import sys
import sqlite3
from sqlite3 import Error

from workflow import Workflow3, ICON_INFO, ICON_WARNING, ICON_ERROR

DB = r"/Users/kevinfunderburg/Library/Application Support/Keyboard Maestro/Keyboard Maestro Variables.sqlite"
KM_VAR_ICON = "/System/Volumes/Data/Applications/Keyboard Maestro.app/Contents/Resources/Variable.icns"


# noinspection PyProtectedMember
def main(wf):

    sql = "SELECT name, value FROM variables WHERE value IS NOT '%Delete%';"

    # create a database connection
    conn = create_connection(DB)
    with conn:
        log.info("query: " + sql)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            name = row[0]
            value = row[1]
            l = len(value)
            if l < 100:
                sub = value
            else:
                sub = 'show in window'

            it = wf.add_item(uid=value,
                             title=name,
                             subtitle=sub,
                             arg=value,
                             autocomplete=name,
                             valid=True,
                             icon=KM_VAR_ICON,
                             icontype="filepath",
                             quicklookurl=value)
            it.add_modifier('cmd', subtitle="placeholder", arg=value, valid=True)

    if len(wf._items) == 0:
        wf.add_item('No variables with this name found', icon=ICON_WARNING)

    wf.send_feedback()


def add(x):
    return x + 5


def count_lines(txt):
    assert isinstance(txt, str)
    return txt.find('\n')


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))
