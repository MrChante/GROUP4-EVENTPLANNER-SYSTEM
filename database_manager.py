import json
import os
from tkinter import messagebox


class DatabaseManager:

    def __init__(self, filename="events.json"):
        self.database = filename

    def load_events(self):
        """Applies file handling to retrieve records from the JSON database."""
        try:
            if os.path.exists(self.database):
                with open(self.database, "r") as file:
                    return json.load(file)
            return []
        except json.JSONDecodeError:
            messagebox.showerror("Error", "JSON database file is empty or corrupted.")
            return []

    def save_events(self, events):
        """Saves current memory data collections securely back to the file storage."""
        try:
            with open(self.database, "w") as file:
                json.dump(events, file, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Error saving database alterations: {e}")