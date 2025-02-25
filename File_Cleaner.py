import os
import shutil
import time
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from icecream import ic

class FileCleaner:
    def __init__(self):
        self.path = ""
        self.sub_folders = []
        self.index = 1.0

    def in_path(self, path_input_ind):
        self.path = path_input_ind.get()
        ic(self.path)

    def make_sub_folders(self, disp_text, progressing):
        disp_text.configure(state="normal")
        sub_folder = ["text folder", "image folder", "video folder", "audio folder", "compressed folder",
                      "document folder",
                      "python folder", "Java folder", "others folder"]
        for i in sub_folder:
            self.sub_folders.append(os.path.join(self.path, i))
        ic(self.sub_folders)
        for i in self.sub_folders:
            if not os.path.exists(i):
                os.makedirs(i, exist_ok=True)
                disp_text.insert(self.index, f"{i} has been created\n")
                self.index += 1
                progressing["value"] += 1
                time.sleep(0.1)
            else:
                disp_text.insert(self.index, f"{i} already exists\n")
                self.index += 1
                progressing["value"] += 1
                time.sleep(0.1)
        disp_text.configure(state="disabled")
        ic(disp_text.get(1.0, END))

    def sort_to_folders(self, disp_text, progressing):
        disp_text.configure(state="normal")
        files = os.listdir(self.path)
        for file in files:
            file_path = os.path.join(self.path, file)
            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1]
                if extension in [".txt", ".csv", ".csvw"]:
                    shutil.move(file_path, self.sub_folders[0])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[0]}\n")
                    progressing["value"] += 1
                elif extension in [".jpg", ".png", ".jpeg", ".gif", ".bmp", ".webp"]:
                    shutil.move(file_path, self.sub_folders[1])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[1]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                elif extension in [".mp4", ".avi", ".mkv", ".wmv", ".mov", ".flv"]:
                    shutil.move(file_path, self.sub_folders[2])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[2]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                elif extension in [".mp3", ".wav", ".m4a", ".flac", "wma", ".aac"]:
                    shutil.move(file_path, self.sub_folders[3])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[3]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                elif extension in [".zip", ".rar", ".7z"]:
                    shutil.move(file_path, self.sub_folders[4])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[4]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                elif extension in [".doc", ".docx", ".pdf"]:
                    shutil.move(file_path, self.sub_folders[5])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[5]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                elif extension in [".py", ".ipynb", ".pyw"]:
                    shutil.move(file_path, self.sub_folders[6])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[6]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                elif extension in [".java", ".class", ".jar"]:
                    shutil.move(file_path, self.sub_folders[7])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[7]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
                else:
                    shutil.move(file_path, self.sub_folders[8])
                    disp_text.insert(self.index, f"{file_path} has been moved to {self.sub_folders[8]}\n")
                    progressing["value"] += 1
                    time.sleep(0.1)
        disp_text.get(1.0, END)
        disp_text.configure(state="disabled")


def open_file(path_input_ind):
    file = filedialog.askdirectory()
    if file:
        file_path = os.path.abspath(file.title())
        path_input_ind.insert(0, file_path)


def progress_bar(path_input_ind, disp_text, progressing):
    start = FileCleaner()
    start.in_path(path_input_ind)
    start.make_sub_folders(disp_text, progressing)
    start.sort_to_folders(disp_text, progressing)


root = Tk()
root.geometry("800x600")

style = Style()
style.configure('frame.TFrame', background='#ffffff')

frame = Frame(root, style="frame.TFrame", width=800, height=600)
frame.place(x=0, y=0)

directory = Label(frame, text="File Cleaner")
directory.place(x=0, y=0)

root.update()

path_input = Entry(frame)
path_input.place(x=directory.winfo_width(), y=0)

root.update()

browse = Button(frame, text="Browse", command=lambda: open_file(path_input))
browse.place(x=directory.winfo_width() + path_input.winfo_width(), y=0)

root.update()

progress = Progressbar(frame, orient=HORIZONTAL, length=300, mode='determinate')
progress.place(x=0, y=100)

root.update()

disp_output = Text(frame, height=10, width=120, state="disabled")
disp_output.configure(relief=FLAT)

submit = Button(frame, text="Submit", command=lambda: progress_bar(path_input, disp_output, progress))
submit.place(x=directory.winfo_width(), y=directory.winfo_height() + 5)

root.update()

disp_output.place(x=0, y=submit.winfo_height() + 100)

root.update()

root.mainloop()
