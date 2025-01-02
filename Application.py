import tkinter as tk
from tkinter import ttk
from widget.Dashboard import Dashboard
from widget.Analysis import Analysis
from widget.Download13F import Download13F
from widget.Firms import Firms
from widget.Settings import Settings


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Analyzer")
        self.geometry("800x600")

        # Create main container frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Create menu
        self.create_menu()

        # Initialize widgets
        self.dashboard = Dashboard(self.main_frame)
        self.settings = Settings(self.main_frame)
        self.analysis = Analysis(self.main_frame)
        self.download_13f = Download13F(self.main_frame)
        self.firms = Firms(self.main_frame)

        # Display the initial dashboard
        self.show_dashboard()

    def create_menu(self):
        # Create a menu bar
        menu_bar = tk.Menu(self)

        # Add Dashboard menu directly
        menu_bar.add_command(label="Dashboard", command=self.show_dashboard)


        # Add Settings menu
        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Settings", command=self.show_settings)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)

        # Add SEC 13F menu
        sec_menu = tk.Menu(menu_bar, tearoff=0)
        sec_menu.add_command(label="Download 13F", command=self.show_download_13f)
        sec_menu.add_command(label="Firms", command =self.show_firms)
        menu_bar.add_cascade(label="SEC 13F", menu=sec_menu)

        # Add Analysis menu
        analysis_menu = tk.Menu(menu_bar, tearoff=0)
        analysis_menu.add_command(label="Analysis", command=self.show_analysis)
        menu_bar.add_cascade(label="Analysis", menu=analysis_menu)

        # Configure the menu bar
        self.config(menu=menu_bar)

    def show_dashboard(self):
        """Display the Dashboard."""
        self.dashboard.render()

    def show_settings(self):
        """Display the Settings."""
        self.settings.render()

    def show_analysis(self):
        """Display the Analysis."""
        self.analysis.render()

    def show_download_13f(self):
        """Display the Download 13F."""
        self.download_13f.render()

    def show_firms(self):
        """Display the Firms."""
        self.firms.render()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
