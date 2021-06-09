import aqt
from aqt import mw
from aqt.deckbrowser import DeckBrowser
from anki.hooks import wrap
import anki
from anki import *
import time
import threading
import os
from subprocess import Popen
import os
import subprocess
from aqt import gui_hooks

#toaster = ToastNotifier()

def get_due():
    while True:
        new, lrn, due = 0, 0, 0
        for tree in mw.col.sched.deckDueTree():
            new += tree[4]
            lrn += tree[3]
            due += tree[2]
        global value
        global inicial
        value = new + lrn + due
        time.sleep(1)

def disable_Enable_Wifi():
    if value > 0:
        subprocess.call('netsh wlan disconnect', shell=True)
#        toaster.show_toast("Sample Notification","Anki time.")
    else:
        subprocess.call('netsh wlan connect THOR', shell=True)
#        toaster.show_toast("Sample Notification","No anki left for today.")

def ColdTurkey(self, _old):
    ret = _old(self)
    threading.Thread(target=get_due).start()
    time.sleep(1)
    threading.Thread(target=disable_Enable_Wifi).start()
    value, inicial = None, None
    if value != inicial:
        disable_Enable_Wifi()
    inicial = value
    return ret

def initializeViews():
    DeckBrowser._renderStats = wrap(
        DeckBrowser._renderStats, ColdTurkey, "around")

initializeViews()
#gui_hooks.reviewer_did_answer_card.append(ColdTurkey)