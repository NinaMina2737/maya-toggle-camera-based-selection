#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import maya.cmds as cmds


def toggle_camera_based_selection():
    """
    Toggles the camera-based selection in Maya.
    """
    if cmds.selectPref(q=True, useDepth=True):
        cmds.selectPref(useDepth=False)
    else:
        cmds.selectPref(useDepth=True)


def execute():
    """
    Executes the script.
    """
    toggle_camera_based_selection()


if __name__ == "__main__":
    execute()
