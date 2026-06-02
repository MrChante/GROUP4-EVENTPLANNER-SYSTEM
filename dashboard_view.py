import tkinter as tk
from tkinter import messagebox, ttk


class DashboardView:

    def __init__(self, root, colors, db_manager):
        self.root = root
        self.colors = colors
        self.db = db_manager
        self.selected_event_id = None
        self.stat_labels = {}

        # Reconfigure window constraints to match dashboard scale requirements
        self.root.geometry("980x620")
        self.root.resizable(True, True)
        self.root.minsize(900, 560)
        self.root.title("Event Planner System")

        self.build_layout()
        self.refresh_all()

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

        # Metric Panels Setup
        self.summary_frame = ttk.Frame(self.root, padding=(18, 2, 18, 14))
        self.summary_frame.pack(fill="x")
        self.create_stat_card("total_events", "Total Events Scheduled", "0")
        self.create_stat_card("unique_venues", "Unique Venues Booked", "0")

        # Layout Navigation Management Tabs
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

    def refresh_all(self):
        events = self.db.load_events()
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
        events = self.db.load_events()
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

        events = self.db.load_events()
        if any(str(e["Event ID"]) == str(event_id) for e in events):
            messagebox.showerror("Duplicate Error", f"An event matching ID '{event_id}' already exists.")
            return

        events.append({"Event ID": event_id, "Event Name": name, "Date": date, "Venue": venue, "Organizer": organizer})
        self.db.save_events(events)
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

        events = self.db.load_events()
        for event in events:
            if str(event["Event ID"]) == str(self.selected_event_id):
                event["Event Name"] = name
                event["Date"] = date
                event["Venue"] = venue
                event["Organizer"] = organizer
                break
        self.db.save_events(events)
        self.clear_form()
        self.refresh_all()
        messagebox.showinfo("Success", "Event data successfully altered.")

    def delete_event(self):
        if self.selected_event_id is None: return
        events = self.db.load_events()
        event = next((e for e in events if str(e["Event ID"]) == str(self.selected_event_id)), None)

        if event and messagebox.askyesno("Confirm Action", f"Delete event data: {event['Event Name']}?"):
            events = [e for e in events if str(e["Event ID"]) != str(self.selected_event_id)]
            self.db.save_events(events)
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