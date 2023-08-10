import tkinter as tk
from tkinter import messagebox

class FileSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File System")

        self.file_content = ""

        self.create_ui()
        
    def create_ui(self):
        self.label = tk.Label(self.root, text="File System App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.filename_label = tk.Label(self.root, text="Enter filename:")
        self.filename_label.pack()

        self.filename_entry = tk.Entry(self.root)   
        self.filename_entry.pack()

        self.create_button = tk.Button(self.root, text="Create File", command=self.create_file)
        self.create_button.pack()

        self.write_label = tk.Label(self.root, text="Enter text to write:")
        self.write_label.pack()

        self.text_entry = tk.Text(self.root, height=5, width=40)
        self.text_entry.pack()

        self.write_button = tk.Button(self.root, text="Write to File", command=self.write_to_file)
        self.write_button.pack()

        self.read_button = tk.Button(self.root, text="Read File", command=self.read_file)
        self.read_button.pack()

    def create_file(self):
        filename = self.filename_entry.get()
        if not filename:
            messagebox.showerror("Error", "Please enter a filename.")
            return

        if self.file_content:
            self.file_content += "\n"

        self.file_content += f"--- File: {filename} ---\n"

        messagebox.showinfo("Success", f"File '{filename}' created.")

    def write_to_file(self):
        text = self.text_entry.get("1.0", tk.END)
        self.file_content += text
        self.text_entry.delete("1.0", tk.END)

        messagebox.showinfo("Success", "Text written to file.")

    def read_file(self):
        filename = self.filename_entry.get()
        if not filename:
            messagebox.showerror("Error", "Please enter a filename.")
            return

        messagebox.showinfo("File Content", self.file_content)

def main():
    root = tk.Tk()
    app = FileSystemApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
