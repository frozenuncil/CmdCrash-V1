import customtkinter as ctk
from PIL import Image
import os
import platform
import psutil
import subprocess
from datetime import datetime

from overlay.bsod_overlay import trigger_svchost_kill
from overlay.cmd_spammer import spam_cmd_windows
from utils.task_utils import show_fake_alert
from overlay.warning_tab import get_warning_text

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("CMD Crash V1")
app.geometry("720x520")
app.resizable(False, False)

status_text = ctk.StringVar(value="Ready")

tabs = ctk.CTkTabview(app, width=680, height=440, corner_radius=10)
tabs.pack(pady=20)

tabs.add("Home")
tabs.add("Tools")
tabs.add("Warning")
tabs.add("System")

import sys

home = tabs.tab("Home")
logo_file = "assets/logo.png"

home = tabs.tab("Home")

if os.path.exists(logo_file):
    ...


if os.path.exists(logo_file):
    img = ctk.CTkImage(light_image=Image.open(logo_file), size=(100, 100))
    ctk.CTkLabel(home, image=img, text="").pack(pady=(20, 5))
else:
    ctk.CTkLabel(home, text="CMD Crash V1", font=("Arial", 24, "bold")).pack(pady=20)

ctk.CTkLabel(home, text="CMD Crash Toolkit", font=("Arial", 18)).pack(pady=(5, 20))

home_btn_cfg = {"width": 220, "height": 38, "corner_radius": 6, "font": ("Arial", 13)}

def restart_app():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def open_folder():
    folder = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(f'explorer "{folder}"')

def check_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    log_status("Running as Admin" if is_admin else "NOT running as Admin")

ctk.CTkButton(home, text="🔄 Restart Application", command=restart_app, **home_btn_cfg).pack(pady=10)
ctk.CTkButton(home, text="📁 Open Installation Folder", command=open_folder, **home_btn_cfg).pack(pady=10)
ctk.CTkButton(home, text="🔍 Check Admin Rights", command=check_admin, **home_btn_cfg).pack(pady=10)



tools = tabs.tab("Tools")

def log_status(msg):
    timestamp = datetime.now().strftime('%H:%M:%S')
    status_text.set(f"[{timestamp}] {msg}")

btn_cfg = {"width": 260, "height": 42, "corner_radius": 6, "font": ("Arial", 14)}

ctk.CTkLabel(tools, text="Available Actions", font=("Arial", 16, "bold")).pack(pady=(20, 10))

ctk.CTkButton(tools, text="Trigger BSOD (VM only)", command=lambda: [trigger_svchost_kill(), log_status("BSOD triggered")], **btn_cfg).pack(pady=10)
ctk.CTkButton(tools, text="Spam CMD Windows", command=lambda: [spam_cmd_windows(), log_status("CMD spam started")], **btn_cfg).pack(pady=10)
ctk.CTkButton(tools, text="Fake System Alert", command=lambda: [show_fake_alert(), log_status("Fake alert shown")], **btn_cfg).pack(pady=10)


warning = tabs.tab("Warning")

ctk.CTkLabel(warning, text="⚠ WARNING", font=("Arial", 18, "bold"), text_color="orange").pack(pady=(20, 10))

warn_box = ctk.CTkTextbox(warning, width=620, height=280, font=("Consolas", 13), wrap="word")
warn_box.insert("0.0", get_warning_text())
warn_box.configure(state="disabled", text_color="red", fg_color="#181818", border_width=0)
warn_box.pack(pady=10)


system = tabs.tab("System")

def get_sysinfo():
    mem = psutil.virtual_memory().total / (1024**3)
    return f"""
OS: {platform.system()} {platform.release()}
CPU: {platform.processor()}
RAM: {mem:.2f} GB
Python: {platform.python_version()}
    """.strip()

def open_taskmgr():
    subprocess.Popen("taskmgr")

ctk.CTkLabel(system, text="System Info", font=("Arial", 16, "bold")).pack(pady=10)

sys_box = ctk.CTkTextbox(system, width=600, height=180, font=("Consolas", 13))
sys_box.insert("0.0", get_sysinfo())
sys_box.configure(state="disabled", text_color="lightgreen", fg_color="#101010", border_width=0)
sys_box.pack(pady=10)

ctk.CTkButton(system, text="Open Task Manager", command=open_taskmgr, **btn_cfg).pack(pady=10)


ctk.CTkLabel(app, textvariable=status_text, font=("Consolas", 12), text_color="gray").pack(pady=(0, 10))

app.mainloop()



