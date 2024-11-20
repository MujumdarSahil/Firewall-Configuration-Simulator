import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from app.firewall import Firewall
import os

class FirewallSimulatorApp:
    def __init__(self):
        self.firewall = Firewall()

        # Set up the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Firewall Configuration Simulator")
        self.root.geometry("800x600")

        # Load the wallpaper image
        self.set_background()

        # Add UI components
        self.setup_ui()

    def set_background(self):
        # Load and display the wallpaper
        image_path = os.path.join(os.path.dirname(__file__), "../assets/wallpaper.png")
        image = Image.open(image_path)
        bg_image = ImageTk.PhotoImage(image.resize((800, 600)))
        bg_label = tk.Label(self.root, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def setup_ui(self):
        # Add buttons, input fields, etc.
        ttk.Label(self.root, text="Firewall Rules", background="#ffffff").pack(pady=10)

        self.rule_list = tk.Listbox(self.root, height=10)
        self.rule_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        control_frame = tk.Frame(self.root)
        control_frame.pack()

        add_btn = ttk.Button(control_frame, text="Add Rule", command=self.add_rule)
        add_btn.pack(side=tk.LEFT, padx=5)

        del_btn = ttk.Button(control_frame, text="Delete Rule", command=self.delete_rule)
        del_btn.pack(side=tk.LEFT, padx=5)

    def add_rule(self):
        rule = "ALLOW ALL"
        self.firewall.add_rule(rule)
        self.refresh_rules()

    def delete_rule(self):
        selected = self.rule_list.curselection()
        if selected:
            self.firewall.delete_rule(selected[0])
            self.refresh_rules()

    def refresh_rules(self):
        self.rule_list.delete(0, tk.END)
        for rule in self.firewall.get_rules():
            self.rule_list.insert(tk.END, rule)

    def run(self):
        self.root.mainloop()
