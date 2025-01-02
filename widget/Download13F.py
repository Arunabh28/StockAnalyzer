import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import zipfile
import io

class Download13F:
    def __init__(self, parent):
        self.parent = parent

    def render(self):
        """Render the Download 13F view into the parent widget."""
        for widget in self.parent.winfo_children():
            widget.destroy()

        container = tk.Frame(self.parent)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="Download 13F Data", font=("Arial", 24)).pack(pady=20)
        tk.Label(container, text="Open the SEC site and download the zip file.", font=("Arial", 16)).pack(pady=20)

        # Button to navigate to the SEC website
        btn_navigate = tk.Button(container, text="Navigate", command=self.navigate)
        btn_navigate.pack(padx=10, pady=10)

        # Button to upload file
        btn_upload = tk.Button(container, text="Upload Zip File", command=self.upload_file)
        btn_upload.pack(padx=10, pady=10)

    def navigate(self):
        """Opens the SEC website in the default web browser."""
        import webbrowser
        webbrowser.open_new("https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets")

    def upload_file(self):
        """Open a file dialog to upload a zip file."""
        file_path = filedialog.askopenfilename(title="Select a Zip File", filetypes=[("Zip files", "*.zip")])
        
        if file_path:
            self.extract_file(file_path)

    def extract_file(self, file_path):
        """Extract the INFOTABLE.tsv from the uploaded zip file in memory."""
        try:
            # Open the zip file in memory
            with open(file_path, 'rb') as f:
                zip_data = io.BytesIO(f.read())
            
            with zipfile.ZipFile(zip_data, 'r') as zip_ref:
                # Check if INFOTABLE.tsv exists in the zip file
                if "INFOTABLE.tsv" in zip_ref.namelist():
                    with zip_ref.open("INFOTABLE.tsv") as file:
                        tsv_data = file.read().decode('utf-8')
                        # Process or display the TSV data
                        messagebox.showinfo("File Extracted", "INFOTABLE.tsv has been successfully extracted.")
                        print(tsv_data)  # You can do further processing with the TSV data here
                else:
                    messagebox.showerror("Error", "INFOTABLE.tsv not found in the zip file.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract the zip file: {e}")
