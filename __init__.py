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
from aqt.reviewer import Reviewer
from typing import Callable

#toaster = ToastNotifier()

def get_due():
    global end
    end = 1
    while True:
        new, lrn, due = 0, 0, 0
        for tree in mw.col.sched.deckDueTree():
            new += tree[4]
            lrn += tree[3]
            due += tree[2]
        global value
        global inicial
        value = new + lrn + due
        if value > 0: 
            subprocess.call('netsh wlan disconnect', shell=True)
        #        toaster.show_toast("Sample Notification","Anki time.")
        else:
            if end == 1:
                subprocess.call('netsh wlan connect THOR', shell=True)
                end = 0
        #        toaster.show_toast("Sample Notification","No anki left for today.")
        time.sleep(1)
        x = 0

def func():
    if x == 1:
        threading.Thread(target=get_due).start()

def When_user_answers(reviewer: Reviewer, ease: int, _old: Callable):
    x = 1

def start(self, _old: Callable):
    func()
    return _old(self)

def initializeViews():
    DeckBrowser._renderStats = wrap(
        DeckBrowser._renderStats, start, "around")

x = 1
initializeViews()
gui_hooks.reviewer_did_answer_card.append(When_user_answers)
