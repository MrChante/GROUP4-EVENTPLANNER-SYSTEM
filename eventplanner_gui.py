import json
import os
import tkinter as tk
from tkinter import messagebox, ttk


class EventPlannerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Event Planner System - Login")
        self.root.geometry("400x500")  # Start with a compact size for the login card
        self.root.resizable(False, False)

        # UI Color Palette matching the ComProg project reference
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

        # Hardcoded Credentials matching your system style
        self.credentials = {"username": "group4", "password": "12345"}

        self.database = "events.json"
        self.selected_event_id = None
        self.stat_labels = {}

        self.setup_style()
        
        # Build the initial Login View
        self.build_login_interface()

    # --- UI STYLING ---

    def setup_style(self):
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

    # --- LOGIN INTERFACE BUILD ---

    def build_login_interface(self):
        # Master container for centering elements
        self.login_container = ttk.Frame(self.root, padding=30)
        self.login_container.pack(fill="both", expand=True)

        # App Brand Header
        ttk.Label(self.login_container, text="SYSTEM LOGIN", style="Title.TLabel").pack(anchor="center", pady=(20, 4))

        # Credentials Box Panel
        login_card = ttk.Frame(self.login_container, padding=20, style="Panel.TFrame")
        login_card.pack(fill="both", expand=True)

        ttk.Label(login_card, text="Username", style="Panel.TLabel").pack(anchor="w", pady=(5, 4))
        self.username_entry = ttk.Entry(login_card)
        self.username_entry.pack(fill="x", pady=(0, 15))
        self.username_entry.focus()

        ttk.Label(login_card, text="Password", style="Panel.TLabel").pack(anchor="w", pady=(5, 4))
        self.password_entry = ttk.Entry(login_card, show="*") # Obfuscates input string characters
        self.password_entry.pack(fill="x", pady=(0, 25))

        # Enter key shortcut handler
        self.password_entry.bind("<Return>", lambda event: self.authenticate_user())

        # Action Execution Button
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
            # Clear out the verification container architecture
            self.login_container.destroy()
            
            # Transition window configuration sizes smoothly for dashboard
            self.root.geometry("980x620")
            self.root.resizable(True, True)
            self.root.minsize(900, 560)
            self.root.title("Event Planner System")
            
            # Initialize primary working dashboards
            self.build_layout()
            self.refresh_all()
        else:
            messagebox.showerror("Access Denied", "Invalid administrative identification parameters.")
            self.password_entry.delete(0, tk.END)

    # --- MAIN SYSTEM LAYOUT (Only shown after login) ---

    def build_layout(self):
        header_frame = ttk.Frame(self.root, padding=(18, 16, 18, 8))
        header_frame.pack(fill="x")

        title_area = ttk.Frame(header_frame)
        title_area.pack(side="left", fill="x", expand=True)
        ttk.Label(title_area, text="Event Planner System", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            title_area,
            text="MEMBER: DAVE KEVIN CABAB, JOHN PAUL CASCARA, JUSTIN PAUL GUASIL, GERRY ESPERAS, LORENZ TUBIS, KYLE LESTER NAVAL",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(3, 0))

        # Dashboard Summary Mini-cards
        self.summary_frame = ttk.Frame(self.root, padding=(18, 2, 18, 14))
        self.summary_frame.pack(fill="x")
        self.create_stat_card("total_events", "Total Events Scheduled", "0")
        self.create_stat_card("unique_venues", "Unique Venues Booked", "0")

        # Tabbed Window Area
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=18, pady=(0, 18))

        self.crud_tab = ttk.Frame(self.tabs)
        self.view_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.crud_tab, text="Event Planner Form")
        self.tabs.add(self.view_tab, text="All Events Calendar View")

        self.build_crud_tab()
        self.build_view_tab()

    def create_stat_card(self, key, label, value):
        card = tk.Frame(self.summary_frame, bg=self.colors["surface"], highlightbackground=self.colors["border"], highlightthickness=1)
        card.pack(side="left", fill="x", expand=True, padx=(0, 10))
        accent = tk.Frame(card, bg=self.colors["accent_bright"], height=3)
        accent.pack(fill="x")
        body = tk.Frame(card, bg=self.colors["surface"])
        body.pack(fill="x", padx=14, pady=10)
        tk.Label(body, text=label.upper(), bg=self.colors["surface"], fg=self.colors["muted"], font=("Arial", 8, "bold")).pack(anchor="w")
        value_label = tk.Label(body, text=value, bg=self.colors["surface"], fg=self.colors["text"], font=("Arial", 15, "bold"))
        value_label.pack(anchor="w", pady=(4, 0))
        self.stat_labels[key] = value_label

    def build_crud_tab(self):
        form = ttk.Frame(self.crud_tab, padding=16, style="Panel.TFrame")
        form.pack(fill="x", pady=(10, 0))

        ttk.Label(form, text="Event ID", style="Panel.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(form, text="Event Name", style="Panel.TLabel").grid(row=0, column=1, sticky="w", padx=(12, 0))
        ttk.Label(form, text="Event Date", style="Panel.TLabel").grid(row=0, column=2, sticky="w", padx=(12, 0))
        ttk.Label(form, text="Venue Location", style="Panel.TLabel").grid(row=2, column=0, sticky="w", pady=(10, 0))
        ttk.Label(form, text="Organizer Name", style="Panel.TLabel").grid(row=2, column=1, sticky="w", padx=(12, 0), pady=(10, 0))

        self.id_entry = ttk.Entry(form, width=15)
        self.name_entry = ttk.Entry(form, width=30)
        self.date_entry = ttk.Entry(form, width=20)
        self.venue_entry = ttk.Entry(form, width=30)
        self.organizer_entry = ttk.Entry(form, width=30)

        self.id_entry.grid(row=1, column=0, sticky="ew", pady=(4, 0))
        self.name_entry.grid(row=1, column=1, sticky="ew", padx=(12, 0), pady=(4, 0))
        self.date_entry.grid(row=1, column=2, sticky="ew", padx=(12, 0), pady=(4, 0))
        self.venue_entry.grid(row=3, column=0, sticky="ew", pady=(4, 0))
        self.organizer_entry.grid(row=3, column=1, columnspan=2, sticky="ew", padx=(12, 0), pady=(4, 0))

        buttons = ttk.Frame(form, style="Panel.TFrame")
        buttons.grid(row=4, column=0, columnspan=3, sticky="w", pady=(16, 0))
        ttk.Button(buttons, text="Create Event", style="Primary.TButton", command=self.create_event).pack(side="left")
        ttk.Button(buttons, text="Update Event", command=self.update_event).pack(side="left", padx=6)
        ttk.Button(buttons, text="Delete Event", command=self.delete_event).pack(side="left")
        ttk.Button(buttons, text="Clear", command=self.clear_form).pack(side="left", padx=6)

        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=2)
        form.columnconfigure(2, weight=1)

        search_frame = ttk.Frame(self.crud_tab, padding=(14, 12, 14, 6))
        search_frame.pack(fill="x")
        ttk.Label(search_frame, text="Select an event from the list below to edit/delete:").pack(side="left")

        columns = ("id", "name", "date", "venue", "organizer")
        self.events_tree = ttk.Treeview(self.crud_tab, columns=columns, show="headings", selectmode="browse")
        self.setup_treeview_headers(self.events_tree)
        self.events_tree.pack(fill="both", expand=True, padx=14, pady=(0, 14))
        self.events_tree.bind("<<TreeviewSelect>>", self.on_event_select)

    def build_view_tab(self):
        records_frame = ttk.Frame(self.view_tab, padding=14)
        records_frame.pack(fill="both", expand=True)

        columns = ("id", "name", "date", "venue", "organizer")
        self.view_only_tree = ttk.Treeview(records_frame, columns=columns, show="headings", selectmode="none")
        self.setup_treeview_headers(self.view_only_tree)
        self.view_only_tree.pack(fill="both", expand=True)

    def setup_treeview_headers(self, tree):
        tree.heading("id", text="Event ID")
        tree.heading("name", text="Event Name")
        tree.heading("date", text="Scheduled Date")
        tree.heading("venue", text="Venue Location")
        tree.heading("organizer", text="Main Organizer")

        tree.column("id", width=80, anchor="center")
        tree.column("name", width=240)
        tree.column("date", width=140, anchor="center")
        tree.column("venue", width=220)
        tree.column("organizer", width=180)

        tree.tag_configure("odd", background=self.colors["surface"])
        tree.tag_configure("even", background=self.colors["surface_alt"])

    # --- DATA & DATABASE METHODS ---

    def load_events(self):
        try:
            if os.path.exists(self.database):
                with open(self.database, "r") as file:
                    return json.load(file)
            return []
        except json.JSONDecodeError:
            messagebox.showerror("Error", "JSON file is empty or corrupted.")
            return []

    def save_events(self, events):
        try:
            with open(self.database, "w") as file:
                json.dump(events, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Error saving database: {e}")

    def refresh_all(self):
        events = self.load_events()
        self.populate_treeview(self.events_tree, events)
        self.populate_treeview(self.view_only_tree, events)
        self.refresh_stats(events)

    def populate_treeview(self, tree, events):
        tree.delete(*tree.get_children())
        for index, event in enumerate(events):
            tree.insert(
                "",
                "end",
                iid=str(event["Event ID"]),
                tags=("even" if index % 2 == 0 else "odd",),
                values=(event["Event ID"], event["Event Name"], event["Date"], event["Venue"], event["Organizer"]),
            )

    def refresh_stats(self, events):
        self.stat_labels["total_events"].configure(text=str(len(events)))
        self.stat_labels["unique_venues"].configure(text=str(len(set(e["Venue"] for e in events if e["Venue"]))))

    def on_event_select(self, _event=None):
        selected = self.events_tree.selection()
        if not selected: return
        self.selected_event_id = selected[0]
        events = self.load_events()
        event = next((e for e in events if str(e["Event ID"]) == self.selected_event_id), None)

        if event:
            self.id_entry.configure(state="normal")
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, str(event["Event ID"]))
            self.id_entry.configure(state="disabled")

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, event["Event Name"])
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, event["Date"])
            self.venue_entry.delete(0, tk.END)
            self.venue_entry.insert(0, event["Venue"])
            self.organizer_entry.delete(0, tk.END)
            self.organizer_entry.insert(0, event["Organizer"])

    def get_form_values(self):
        fields = (self.id_entry.get().strip(), self.name_entry.get().strip(), self.date_entry.get().strip(), self.venue_entry.get().strip(), self.organizer_entry.get().strip())
        if any(not f for f in fields):
            raise ValueError("All interface structural fields are required.")
        return fields

    def create_event(self):
        try:
            event_id, name, date, venue, organizer = self.get_form_values()
        except ValueError as e:
            messagebox.showwarning("Incomplete Data", str(e))
            return

        events = self.load_events()
        if any(str(e["Event ID"]) == str(event_id) for e in events):
            messagebox.showerror("Duplicate Error", f"An event matching ID '{event_id}' already exists.")
            return

        events.append({"Event ID": event_id, "Event Name": name, "Date": date, "Venue": venue, "Organizer": organizer})
        self.save_events(events)
        self.clear_form()
        self.refresh_all()
        messagebox.showinfo("Success", "Event logged successfully.")

    def update_event(self):
        if self.selected_event_id is None: return
        try:
            _, name, date, venue, organizer = self.get_form_values()
        except ValueError as e:
            messagebox.showwarning("Incomplete Data", str(e))
            return

        events = self.load_events()
        for event in events:
            if str(event["Event ID"]) == str(self.selected_event_id):
                event["Event Name"] = name
                event["Date"] = date
                event["Venue"] = venue
                event["Organizer"] = organizer
                break
        self.save_events(events)
        self.clear_form()
        self.refresh_all()
        messagebox.showinfo("Success", "Event data successfully altered.")

    def delete_event(self):
        if self.selected_event_id is None: return
        events = self.load_events()
        event = next((e for e in events if str(e["Event ID"]) == str(self.selected_event_id)), None)

        if event and messagebox.askyesno("Confirm Action", f"Delete event data: {event['Event Name']}?"):
            events = [e for e in events if str(e["Event ID"]) != str(self.selected_event_id)]
            self.save_events(events)
            self.clear_form()
            self.refresh_all()

    def clear_form(self):
        self.selected_event_id = None
        self.events_tree.selection_remove(self.events_tree.selection())
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.venue_entry.delete(0, tk.END)
        self.organizer_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = EventPlannerGUI(root)
    root.mainloop()
