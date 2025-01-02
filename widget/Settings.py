import tkinter as tk
from tkinter import ttk

class Settings:
    def __init__(self, parent):
        self.parent = parent

    def render(self):
        """Render the settings into the parent widget."""
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Settings", font=("Arial", 24)).pack(pady=20)

        tk.Label(self.parent, text="Option 1:").pack(anchor="w", padx=20)
        ttk.Entry(self.parent).pack(fill="x", padx=20, pady=5)

        tk.Label(self.parent, text="Option 2:").pack(anchor="w", padx=20)
        ttk.Entry(self.parent).pack(fill="x", padx=20, pady=5)