import tkinter as tk
from tkinter import ttk

class Analysis:
    def __init__(self, parent):
        self.parent = parent

    def render(self):
        """Render the analysis view into the parent widget."""
        for widget in self.parent.winfo_children():
            widget.destroy()

        tk.Label(self.parent, text="Analysis", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.parent, text="Run Analysis", command=lambda: print("Analysis started!")).pack(pady=10)
