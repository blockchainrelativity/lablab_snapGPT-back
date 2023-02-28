import sys
import gc
import time
import threading
import multiprocessing


def check_daemonic_threads():
    for t in threading.enumerate():
        if t.daemon and t.is_alive():
            t.join()

def join_active_children():
    for p in multiprocessing.active_children():
        p.join()

def gc_collect_exit(s):
    gc.collect()
    sys.exit(s)

def sleeep(t):
    time.sleep(t)
    