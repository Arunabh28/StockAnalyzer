import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from AnalyzeTwo13F import AnalyzeTwo13F
from ChangeInData import ChangeInData
import os  # Correct the redundant import of os

class Analyze13FUI:
    def __init__(self, root):
        self.root = root
        self.root.title("13F Filing Comparison Tool")

        # Variables to hold file paths
        self.file1_path = ""
        self.file2_path = ""

        # Create the UI components
        self.create_widgets()

    def create_widgets(self):
        # Previous 13F Filing label and file picker
        self.label_file1 = tk.Label(self.root, text="Previous 13F Filing:")
        self.label_file1.grid(row=0, column=0, padx=10, pady=10)

        self.entry_file1 = tk.Entry(self.root, width=50)
        self.entry_file1.grid(row=0, column=1, padx=10, pady=10)

        self.browse_button1 = tk.Button(self.root, text="Browse...", command=self.browse_file1)
        self.browse_button1.grid(row=0, column=2, padx=10, pady=10)

        # Latest 13F Filing label and file picker
        self.label_file2 = tk.Label(self.root, text="Latest 13F Filing:")
        self.label_file2.grid(row=1, column=0, padx=10, pady=10)

        self.entry_file2 = tk.Entry(self.root, width=50)
        self.entry_file2.grid(row=1, column=1, padx=10, pady=10)

        self.browse_button2 = tk.Button(self.root, text="Browse...", command=self.browse_file2)
        self.browse_button2.grid(row=1, column=2, padx=10, pady=10)

        # Compare button
        self.compare_button = tk.Button(self.root, text="Compare", command=self.compare_files, state=tk.DISABLED)
        self.compare_button.grid(row=2, column=1, padx=10, pady=20)

        # Results display area (using scrolledtext to allow multiline results)
        self.results_text = scrolledtext.ScrolledText(self.root, width=80, height=20, wrap=tk.WORD)
        self.results_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_file1(self):
        """Opens file dialog to select the previous 13F XML file."""
        file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        if file_path:
            self.file1_path = file_path
            self.entry_file1.delete(0, tk.END)
            self.entry_file1.insert(0, self.file1_path)
            self.check_files_selected()

    def browse_file2(self):
        """Opens file dialog to select the latest 13F XML file."""
        file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        if file_path:
            self.file2_path = file_path
            self.entry_file2.delete(0, tk.END)
            self.entry_file2.insert(0, self.file2_path)
            self.check_files_selected()

    def check_files_selected(self):
        """Enables the compare button if both files are selected and exist."""
        if self.file1_path and self.file2_path:
            if os.path.exists(self.file1_path) and os.path.exists(self.file2_path):
                self.compare_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("File Error", "One or both files do not exist.")
                self.compare_button.config(state=tk.DISABLED)

    def compare_files(self):
        """Compares the selected 13F XML files and displays the results."""
        if not self.file1_path or not self.file2_path:
            messagebox.showerror("File Error", "Both files must be selected.")
            return

        try:
            # Create the AnalyzeTwo13F object
            analyzer = AnalyzeTwo13F(self.file1_path, self.file2_path)

            # Clear previous results
            self.results_text.delete(1.0, tk.END)

            # New issuers added
            new_issuers = analyzer.new_issuers_added()
            self.results_text.insert(tk.END, "New Issuers Added in XML 2:\n")
            if new_issuers:
                for issuer in new_issuers:
                    self.results_text.insert(tk.END, f"{issuer}\n")
            else:
                self.results_text.insert(tk.END, "No new issuers.\n")
            
            # Issuers removed
            removed_issuers = analyzer.issuers_removed()
            self.results_text.insert(tk.END, "\nIssuers Removed in XML 2:\n")
            if removed_issuers:
                for issuer in removed_issuers:
                    self.results_text.insert(tk.END, f"{issuer}\n")
            else:
                self.results_text.insert(tk.END, "No issuers removed.\n")

            # Top N issuers with increased shares
            increased_shares = analyzer.top_n_issuers_increased_shares(5)
            self.results_text.insert(tk.END, "\nTop 5 Issuers with Increased Shares:\n")
            if increased_shares:
                for change in increased_shares:
                    self.results_text.insert(tk.END, f"{change.Issuer}: {change.Quantity:,} ({change.Change_Type})\n")
            else:
                self.results_text.insert(tk.END, "No issuers with increased shares.\n")

            # Top N issuers with decreased shares
            decreased_shares = analyzer.top_n_issuers_decreased_shares(5)
            self.results_text.insert(tk.END, "\nTop 5 Issuers with Decreased Shares:\n")
            if decreased_shares:
                for change in decreased_shares:
                    self.results_text.insert(tk.END, f"{change.Issuer}: {change.Quantity:,} ({change.Change_Type})\n")
            else:
                self.results_text.insert(tk.END, "No issuers with decreased shares.\n")

            # Top N issuers with market value change
            positive_changes, negative_changes = analyzer.top_n_issuers_market_value_changed(5)
            self.results_text.insert(tk.END, "\nTop 5 Issuers with Positive Market Value Change:\n")
            if positive_changes:
                for change in positive_changes:
                    self.results_text.insert(tk.END, f"{change.Issuer}: ${change.Quantity:,.2f} ({change.Change_Type})\n")
            else:
                self.results_text.insert(tk.END, "No positive market value changes.\n")

            self.results_text.insert(tk.END, "\nTop 5 Issuers with Negative Market Value Change:\n")
            if negative_changes:
                for change in negative_changes:
                    self.results_text.insert(tk.END, f"{change.Issuer}: {change.Quantity:,.2f} ({change.Change_Type})\n")
            else:
                self.results_text.insert(tk.END, "No negative market value changes.\n")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during comparison: {e}")
            print(e)

# Main code to launch the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = Analyze13FUI(root)
    root.mainloop()
