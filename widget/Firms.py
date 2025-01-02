import tkinter as tk
from tkinter import ttk

class Firms:
    def __init__(self, parent):
        self.parent = parent

    def render(self):
        """Render the Firms view into the parent widget."""
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Firms", font=("Arial", 24)).pack(pady=20)

