import tkinter as tk
from datetime import datetime
import os
import socket
import subprocess  # Dodajemy import modułu subprocess

class JJJournalApp:
    def __init__(self, root):
        self.root = root
        root.title('Jazzed Journal by AK4CZ')

        # Tworzenie pola tekstowego do wprowadzania notatki
        self.note_text = tk.Text(root)
        self.note_text.pack()

        # Tworzenie przycisku do zapisywania notatki
        self.save_button = tk.Button(root, text='Zapisz', command=self.save_note)
        self.save_button.pack()

        # Tworzenie przycisku do otwierania folderu z notatkami
        self.open_notes_button = tk.Button(root, text='Otwórz notatki', command=self.open_notes_folder)
        self.open_notes_button.pack()

    def save_note(self):
        note_text = self.note_text.get("1.0", tk.END).strip()
        if note_text:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            computer_name = socket.gethostname()

            filename = f"notes/{computer_name}_{timestamp}_JJ.txt"

            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as file:
                file.write(note_text)

            self.note_text.delete("1.0", tk.END)

    def open_notes_folder(self):
        folder_path = os.path.abspath("notes")
        if os.path.exists(folder_path):
            subprocess.Popen(['explorer', folder_path])  # Otwieramy folder notatek w eksploratorze plików

def main():
    root = tk.Tk()
    app = JJJournalApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
