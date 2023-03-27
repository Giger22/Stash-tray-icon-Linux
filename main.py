import pystray
import re
import subprocess
import signal
import sys
import time
import multiprocessing
import webbrowser
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
stop_threads = False
stash_flag = False
started_before = False
manager = multiprocessing.Manager()
final_list = manager.list()
final_list.append(1)
final_list.append(1)
port = 9999

def pyquit():
    global stop_threads
    stop_threads = True
    if shell() != -1:
        result = subprocess.run(["ps", "-aux"], stdout=subprocess.PIPE)
        result = result.stdout.decode("utf-8")
        newlines = re.finditer("\n", result)
        stash_pos =result.find("stash-linux")

        for i, x in enumerate(newlines):
            end = x.end()
            if int(end) > int(stash_pos):
                start = i
                break
            prev = x.end()

        ProcessID = ""
        for i in range(int(prev), int(stash_pos + 11)):
            ProcessID += result[i]

        stash_pos =result.find("stash-linux")
        ProcessID = re.search("\w+[\s]+(\d+)", ProcessID)
        ProcessID = str(ProcessID.group(1))
        subprocess.run(["kill", ProcessID])

    procs[-1].terminate()
    sys.exit()

def startup_stop():
    if shell() != -1:
        result = subprocess.run(["ps", "-aux"], stdout=subprocess.PIPE)
        result = result.stdout.decode("utf-8")
        newlines = re.finditer("\n", result)
        stash_pos =result.find("stash-linux")

    for i, x in enumerate(newlines):
        end = x.end()
        if int(end) > int(stash_pos):
            start = i
            break
        prev = x.end()

    ProcessID = ""
    for i in range(int(prev), int(stash_pos + 11)):
        ProcessID += result[i]

    stash_pos =result.find("stash-linux")
    ProcessID = re.search("\w+[\s]+(\d+)", ProcessID)
    ProcessID = str(ProcessID.group(1))
    subprocess.run(["kill", ProcessID])
def shell():
    global started_before
    result = subprocess.run(["ps", "-aux"], stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")
    result = result.find("stash-linux")
    if result != -1:
        started_before = True
    return result

def stash_start(final_list):
        global started_before, port
        started_before = False
        try:
            subproc =subprocess.Popen(["stash-linux", "--port", port]) #FIXME when pressing ctrl+c tray icon stays and process does not exit
        except KeyboardInterrupt(): 
        
            subproc.kill()
            pyquit()

        default_browser = webbrowser.get()
        default_browser_name = default_browser.name
        default_browser_basename = default_browser.basename
        localhost = "http://localhost:" + str(port)
        # if default_browser_basename == "chrome" or "chromium" or "librewolf" or "firefox":
        #     subprocess.run([default_browser_basename, "--new-window", localhost])
        # elif default_browser_basename == "konqueror" or "brave":
        #     subprocess.run([default_browser_basename, localhost])
        # else:
        subprocess.run([default_browser_basename, localhost])

        while True:
            if final_list[0] == 0:
                print("STOP")
                subproc.kill()
                break

def thread_stash():
    procs.append(multiprocessing.Process(target=stash_start, args=([final_list]), name=final_list[1]))
    final_list[1] = str(1 + int(final_list[1]))
    final_list[0] = 1
    procs[-1].start()
    global stash_flag
    stash_flag = True

def thread_stash_stop():
    global stop_threads, stash_flag, started_before
    global final_list
    if started_before == True:
        startup_stop()
    try:
        stash_flag = False
        time.sleep(0.25)

        final_list[0] = 0 
        time.sleep(0.25)

        procs[-1].kill()
        time.sleep(0.25)
    except IndexError:
        pass


procs = []
proc = multiprocessing.Process(target=stash_start, args=([final_list]), name=final_list[1])#args=(lambda: stop_threads, ))

p = subprocess.Popen(["whoami"], stdout=subprocess.PIPE)
user_name, err = p.communicate()
user_name = str(user_name)
user_name = re.sub(r"[b'\\n\t\s]*", "", user_name)


with open("/home/{user_name}/Applications/Stash/config.txt".format(user_name=user_name), "r", ) as c:
    config_list = c.readlines()

config = config_list[0]
port = config_list[1]

config = re.sub(r"[\n\t\s]*", "", config)
config = re.sub(r"(Icon:)", "", config)

port = re.sub(r"[\n\t\s]*", "", port)
port = re.sub(r"(Port:)", "", port)

if shell() != -1:
    image = Image.open(config)
    stash_flag = True
else:
    stash_flag = False
    image = Image.open(config)

thread_stash()

icon = pystray.Icon(name="IP Check",
                    title="Stash Linux",
                    icon=image, menu=menu(
        menu.SEPARATOR,
        item("Start Stash", thread_stash, checked=lambda item:stash_flag),
        item("Stop Stash", thread_stash_stop, checked=lambda item: not stash_flag),
        item("Quit", pyquit)
    ))
icon.run()
