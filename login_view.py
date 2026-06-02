import tkinter as tk
from tkinter import messagebox, ttk


class LoginView:

    def __init__(self, root, colors, on_success_callback):
        self.root = root
        self.colors = colors
        self.on_success = on_success_callback

        # Initial geometry setup optimized for a compact card login
        self.root.title("Event Planner System - Login")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.credentials = {"username": "group4", "password": "12345"}
        self.build_login_interface()

    def build_login_interface(self):
        self.login_container = ttk.Frame(self.root, padding=30)
        self.login_container.pack(fill="both", expand=True)

        ttk.Label(self.login_container, text="SYSTEM LOGIN", style="Title.TLabel").pack(anchor="center", pady=(20, 4))

        login_card = ttk.Frame(self.login_container, padding=20, style="Panel.TFrame")
        login_card.pack(fill="both", expand=True)

        ttk.Label(login_card, text="Username", style="Panel.TLabel").pack(anchor="w", pady=(5, 4))
        self.username_entry = ttk.Entry(login_card)
        self.username_entry.pack(fill="x", pady=(0, 15))
        self.username_entry.focus()

        ttk.Label(login_card, text="Password", style="Panel.TLabel").pack(anchor="w", pady=(5, 4))
        self.password_entry = ttk.Entry(login_card, show="*")
        self.password_entry.pack(fill="x", pady=(0, 25))

        # Enter key shortcut action binding
        self.password_entry.bind("<Return>", lambda event: self.authenticate_user())

        ttk.Button(
            login_card,
            text="LOG IN",
            style="Primary.TButton",
            command=self.authenticate_user
        ).pack(fill="x", ipady=4)

    def authenticate_user(self):
        user_input = self.username_entry.get().strip()
        pass_input = self.password_entry.get()

        if user_input == self.credentials["username"] and pass_input == self.credentials["password"]:
            self.login_container.destroy()
            self.on_success()  # Triggers the main dashboard swap inside main.py
        else:
            messagebox.showerror("Access Denied", "Invalid Username And Password!")
            self.password_entry.delete(0, tk.END)