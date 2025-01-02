import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, parent):
        self.parent = parent

    def render(self):
        """Render the dashboard into the parent widget."""
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Welcome to the Dashboard!", font=("Arial", 24)).pack(pady=20)
