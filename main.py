import tkinter as tk
from tkinter import filedialog, messagebox


class YSPTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Y# Text Editor")

        self.text_area = tk.Text(root, wrap="word", font=("Consolas", 12))
        self.text_area.pack(fill="both", expand=True)

        self.current_file = None

        # Menubar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("YSP Text Editor - New File")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("YSP Files", "*.ysp"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.current_file = file_path
                self.root.title(f"YSP Text Editor - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self):
        if self.current_file:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("YSP Files", "*.ysp")]
        )
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                self.current_file = file_path
                self.root.title(f"YSP Text Editor - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    editor = YSPTextEditor(root)
    root.geometry("700x500")
    root.mainloop()
