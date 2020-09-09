#!/usr/bin/python
# encoding: utf-8

from __future__ import unicode_literals

import os
import argparse
import plistlib
import sys
import sqlite3
from sqlite3 import Error

from workflow import Workflow3, ICON_INFO, ICON_WARNING, ICON_ERROR

KM_APP_SUPPORT = os.path.expanduser("~/Library/Application Support/Keyboard Maestro/")
KM_APP_RESOURCES = "/System/Volumes/Data/Applications/Keyboard Maestro.app/Contents/Resources/"

VARS_DB = KM_APP_SUPPORT + "Keyboard Maestro Variables.sqlite"
CLIPS_PLIST = KM_APP_SUPPORT + "Keyboard Maestro Clipboards.plist"
ICON_KM_VAR = KM_APP_RESOURCES + "Variable.icns"
ICON_KM_CLIP = KM_APP_RESOURCES + "ClipboardIcon.icns"

wf = None
log = None


# noinspection PyProtectedMember
def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', dest='vars', nargs='?', default=None)
    parser.add_argument('-c', dest='clips', nargs='?', default=None)
    parser.add_argument('query', nargs='?', default=None)
    args = parser.parse_args(wf.args)

    if args.vars:
        sql = "SELECT name, value FROM variables WHERE value IS NOT '%Delete%';"

        # create a database connection
        conn = create_connection(VARS_DB)
        with conn:
            log.info("query: " + sql)
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
                value = row[1]
                if len(value) < 100:
                    sub = value
                else:
                    sub = 'show in window'

                it = wf.add_item(uid=value,
                                 title=name,
                                 subtitle=sub,
                                 arg=[name,value],
                                 autocomplete=name,
                                 valid=True,
                                 icon=ICON_KM_VAR,
                                 icontype="filepath",
                                 quicklookurl=value)
                it.add_modifier('cmd', subtitle="placeholder", arg=value, valid=True)

    elif args.clips:
        clips_pl = plistlib.readPlist(CLIPS_PLIST)
        for clip in clips_pl:
            name = clip['Name']
            uid = clip['UID']
            it = wf.add_item(uid=uid,
                             title=name,
                             subtitle='view in window',
                             arg=[name, uid],
                             autocomplete=name,
                             valid=True,
                             icon=ICON_KM_CLIP,
                             icontype="filepath",
                             quicklookurl=ICON_KM_CLIP)

    if len(wf._items) == 0:
        wf.add_item('No items found', icon=ICON_WARNING)

    wf.send_feedback()


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
