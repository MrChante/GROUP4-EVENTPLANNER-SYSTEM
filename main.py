import tkinter as tk
from tkinter import ttk

# Import our custom feature modules
from dashboard_view import DashboardView
from database_manager import DatabaseManager
from login_view import LoginView


class MainApplication:

    def __init__(self, root):
        self.root = root

        # Configuration Styling Maps
        self.colors = {
            "bg": "#0B0D10",
            "surface": "#171A21",
            "surface_alt": "#20242E",
            "surface_soft": "#262B36",
            "accent": "#587100",
            "accent_bright": "#749400",
            "text": "#F5F7FB",
            "muted": "#A7AFBE",
            "border": "#303642",
            "danger": "#B0003A",
        }

        # Initialize the shared file handler service module
        self.db_manager = DatabaseManager("events.json")

        self.setup_global_styles()

        # Start the app lifecycle inside the login screen view state
        self.login_screen = LoginView(self.root, self.colors, on_success_callback=self.show_dashboard)

    def setup_global_styles(self):
        self.root.configure(bg=self.colors["bg"])
        style = ttk.Style()
        style.theme_use("clam")
        
        style.configure("TFrame", background=self.colors["bg"])
        style.configure("Panel.TFrame", background=self.colors["surface"])
        style.configure("TNotebook", background=self.colors["bg"], borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background=self.colors["surface_alt"],
            foreground=self.colors["muted"],
            padding=(18, 11),
            borderwidth=0,
            font=("Arial", 10, "bold"),
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", self.colors["surface_soft"]), ("active", self.colors["surface"])],
            foreground=[("selected", self.colors["text"]), ("active", self.colors["text"])],
        )
        style.configure(
            "Treeview",
            background=self.colors["surface"],
            fieldbackground=self.colors["surface"],
            foreground=self.colors["text"],
            bordercolor=self.colors["border"],
            lightcolor=self.colors["border"],
            darkcolor=self.colors["border"],
            rowheight=30,
            font=("Arial", 10),
        )
        style.map("Treeview", background=[("selected", self.colors["accent"])], foreground=[("selected", self.colors["text"])])
        style.configure(
            "Treeview.Heading",
            background=self.colors["surface_soft"],
            foreground=self.colors["text"],
            relief="flat",
            font=("Arial", 10, "bold"),
        )
        style.configure(
            "Primary.TButton",
            background=self.colors["accent_bright"],
            foreground=self.colors["text"],
            borderwidth=0,
            focusthickness=0,
            padding=(14, 8),
            font=("Arial", 10, "bold"),
        )
        style.map("Primary.TButton", background=[("active", self.colors["accent"])])
        style.configure(
            "TButton",
            background=self.colors["surface_soft"],
            foreground=self.colors["text"],
            borderwidth=0,
            focusthickness=0,
            padding=(12, 7),
            font=("Arial", 10),
        )
        style.map("TButton", background=[("active", self.colors["border"])])
        style.configure("TLabel", background=self.colors["bg"], foreground=self.colors["muted"], font=("Arial", 10))
        style.configure("Panel.TLabel", background=self.colors["surface"], foreground=self.colors["muted"], font=("Arial", 10))
        style.configure("Title.TLabel", background=self.colors["bg"], foreground=self.colors["text"], font=("Arial", 22, "bold"))
        style.configure("Subtitle.TLabel", background=self.colors["bg"], foreground=self.colors["muted"], font=("Arial", 10))
        style.configure(
            "TEntry",
            fieldbackground=self.colors["surface_alt"],
            foreground=self.colors["text"],
            insertcolor=self.colors["text"],
            bordercolor=self.colors["border"],
            lightcolor=self.colors["border"],
            darkcolor=self.colors["border"],
            padding=7,
        )

    def show_dashboard(self):
        """Callback event fired automatically once authorization completes."""
        self.dashboard = DashboardView(self.root, self.colors, self.db_manager)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()