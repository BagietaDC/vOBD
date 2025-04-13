import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog, ttk
import obd
import threading
from datetime import datetime
import time
import os
import random

class OBDGuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("vOBD")
        self.root.configure(bg="#6b92d1")
        self.connection = None
        self.monitoring = False
        self.use_emulator = False
        self.param_labels = {}

        self.params_to_monitor = [
            obd.commands.RPM,
            obd.commands.SPEED,
            obd.commands.COOLANT_TEMP,
            obd.commands.MAF,
            obd.commands.THROTTLE_POS,
            obd.commands.ENGINE_LOAD,
            obd.commands.FUEL_PRESSURE,
            obd.commands.INTAKE_PRESSURE,
            obd.commands.RUN_TIME,
            obd.commands.FUEL_LEVEL
        ]

        self.param_units = {
            "RPM": "obr/min",
            "SPEED": "km/h",
            "COOLANT_TEMP": "°C",
            "MAF": "g/s",
            "THROTTLE_POS": "%",
            "ENGINE_LOAD": "%",
            "FUEL_PRESSURE": "kPa",
            "INTAKE_PRESSURE": "kPa",
            "RUN_TIME": "s",
            "FUEL_LEVEL": "%",
        }

        self.create_widgets()
        self.setup_menu()

    def create_widgets(self):
        btn_frame = tk.Frame(self.root, bg="#6b92d1")
        btn_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

        self.connect_btn = tk.Button(btn_frame, text="Connect with interface", command=self.connect, width=20, bg="#6a9ed9", font=("Arial", 10, "bold"))
        self.connect_btn.pack(pady=5, fill=tk.X)

        self.dtc_btn = tk.Button(btn_frame, text="Read DTC", command=self.read_dtc, state=tk.DISABLED, width=20, bg="#6a9ed9")
        self.dtc_btn.pack(pady=5, fill=tk.X)

        self.freeze_btn = tk.Button(btn_frame, text="Read Freeze Frames", command=self.read_freeze_frames, state=tk.DISABLED, width=20, bg="#6a9ed9")
        self.freeze_btn.pack(pady=5, fill=tk.X)

        self.clear_btn = tk.Button(btn_frame, text="Delete DTC", command=self.clear_dtc, state=tk.DISABLED, width=20, bg="#6a9ed9")
        self.clear_btn.pack(pady=5, fill=tk.X)

        self.live_params_btn = tk.Button(btn_frame, text="Monitor parameters", command=self.monitor_params, state=tk.DISABLED, width=20, bg="#6a9ed9")
        self.live_params_btn.pack(pady=5, fill=tk.X)

        self.save_log_btn = tk.Button(btn_frame, text="Save log", command=self.save_log, width=20, bg="#6a9ed9")
        self.save_log_btn.pack(pady=5, fill=tk.X)

        self.exit_btn = tk.Button(btn_frame, text="Exit", command=self.on_exit, width=20, bg="#f4b5ae", font=("Arial", 10, "bold"))
        self.exit_btn.pack(pady=5, fill=tk.X)

        self.output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=30, bg="#edf0f5", font=("Arial", 10))
        self.output.tag_config("green", foreground="green")
        self.output.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.param_tree = ttk.Treeview(self.root, columns=("param", "value"), show="headings", height=30)
        self.param_tree.heading("param", text="Parameter")
        self.param_tree.heading("value", text="Value")
        self.param_tree.column("param", width=150)
        self.param_tree.column("value", anchor="center", width=150)
        self.param_tree.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.status_var = tk.StringVar()
        self.status_var.set("NOT CONNECTED")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, bd=0, relief=tk.SUNKEN, anchor="center", bg="#6b92d1", font=("Arial", 10, "bold"))
        self.status_bar.grid(row=2, column=0, columnspan=4, sticky="we", pady=5)

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save log", command=self.save_log)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Choose parameters", command=self.select_parameters)
        tools_menu.add_checkbutton(label="Emulator mode", command=self.toggle_emulator)
        menubar.add_cascade(label="Advanced", menu=tools_menu)

        self.root.config(menu=menubar)

    def toggle_emulator(self):
        self.use_emulator = not self.use_emulator
        self.log(f"Emulator mode {'ON' if self.use_emulator else 'OFF'}")

    def log(self, message, tag=None):
        timestamp = datetime.now().strftime("%H:%M:%S")
        full_message = f"[{timestamp}] {message}\n"
        self.output.insert(tk.END, full_message, tag)
        if "błąd" in message.lower():
            self.output.insert(tk.END, "\n")
        self.output.see(tk.END)
        self.status_var.set(message[:50] + "..." if len(message) > 50 else message)

    def connect(self):
        self.log("Connecting with interface...")
        try:
            if not self.use_emulator:
                self.connection = obd.OBD()
            else:
                self.connection = None

            if self.use_emulator or (self.connection and self.connection.is_connected()):
                self.log("Connected (EMULATION)" if self.use_emulator else f"Connected with {self.connection.port_name()}", tag="green")

                self.dtc_btn.config(state=tk.NORMAL)
                self.freeze_btn.config(state=tk.NORMAL)
                self.clear_btn.config(state=tk.NORMAL)
                self.live_params_btn.config(state=tk.NORMAL)
                self.connect_btn.config(state=tk.DISABLED)
            else:
                self.log("Couldn't connect with interface...")

        except Exception as e:
            self.log(f"Connection ERROR: {str(e)}")
            messagebox.showerror("ERROR!", f"Connection ERROR: {str(e)}")

    def monitor_params(self):
        if not self.monitoring:
            self.monitoring = True
            self.live_params_btn.config(text="Stop monitoring")
            self.run_in_thread(self._monitor_params)
        else:
            self.monitoring = False
            self.live_params_btn.config(text="Monitor parameters")

    def _monitor_params(self):
        self.param_tree.delete(*self.param_tree.get_children())
        for cmd in self.params_to_monitor:
            self.param_tree.insert("", "end", iid=cmd.name, values=(cmd.name, "--"))

        self.log("Started monitoring parameters...")

        while self.monitoring:
            for cmd in self.params_to_monitor:
                if self.use_emulator:
                    value = f"{random.randint(0, 100)}"
                elif self.connection and self.connection.is_connected():
                    response = self.connection.query(cmd)
                    value = str(response.value) if not response.is_null() else "NO DATA!"
                else:
                    value = "Connection ERROR"

                unit = self.param_units.get(cmd.name, "")
                self.param_tree.set(cmd.name, column="value", value=f"{value} {unit}")
            time.sleep(1)

    def read_dtc(self):
        self.run_in_thread(self._read_dtc)

    def _read_dtc(self):
        self.log("Reading DTC...")
        if self.use_emulator:
            self.log("(EMULATION) Found DTC: P0420, P0300")
            return
        response = self.connection.query(obd.commands.GET_DTC)
        if response and not response.is_null():
            for code in response.value:
                self.log(f"- {code}")

    def read_freeze_frames(self):
        self.run_in_thread(self._read_freeze)

    def _read_freeze(self):
        self.log("Reading Freeze Frames...")
        self.log("(EMULATION) Found Freeze Frames: RPM=3000, SPEED=90")

    def clear_dtc(self):
        self.run_in_thread(self._clear_dtc)

    def _clear_dtc(self):
        self.log("Deleting DTC...")
        if self.use_emulator:
            self.log("(EMULATION) DTC has been deleted!")
            return
        self.connection.query(obd.commands.CLEAR_DTC)
        self.log("DTC has been deleted!")

    def save_log(self):
        logs_dir = "Logs"
        os.makedirs(logs_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = filedialog.asksaveasfilename(
            initialdir=logs_dir,
            defaultextension=".txt",
            initialfile=f"log_{timestamp}.txt",
            filetypes=[("Pliki tekstowe", "*.txt")]
        )
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(self.output.get("1.0", tk.END))
            self.log("Log saved!")

    def select_parameters(self):
        param_window = tk.Toplevel(self.root)
        param_window.title("Choose parameters")

        all_commands = sorted([cmd for cmd in obd.commands.__dict__.values()
                               if isinstance(cmd, obd.OBDCommand)], key=lambda x: x.name)
        self.param_vars = {cmd.name: tk.BooleanVar(value=cmd in self.params_to_monitor)
                           for cmd in all_commands}

        canvas = tk.Canvas(param_window)
        scrollbar = tk.Scrollbar(param_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for cmd in all_commands:
            cb = tk.Checkbutton(scrollable_frame, text=cmd.name, variable=self.param_vars[cmd.name])
            cb.pack(anchor="w")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def select_all():
            for var in self.param_vars.values():
                var.set(True)

        def deselect_all():
            for var in self.param_vars.values():
                var.set(False)

        tk.Button(param_window, text="Check all", command=select_all).pack(pady=(10, 0))
        tk.Button(param_window, text="Uncheck all", command=deselect_all).pack(pady=5)

        def save():
            self.params_to_monitor = [cmd for cmd in all_commands if self.param_vars[cmd.name].get()]
            self.log(f"Selected {len(self.params_to_monitor)} parameters")
            param_window.destroy()

        tk.Button(param_window, text="Save", command=save).pack(pady=(10, 10))

    def run_in_thread(self, target):
        thread = threading.Thread(target=target)
        thread.daemon = True
        thread.start()

    def on_exit(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = OBDGuiApp(root)
    root.mainloop()
