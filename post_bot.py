import pyautogui
import time
import tkinter as tk
from tkinter import ttk, scrolledtext
import threading

class BotGUI:
    def __init__(self, master):
        self.master = master
        master.title("AdsPower Bot")
        master.geometry("400x300")

        self.is_running = False

        self.start_button = ttk.Button(master, text="Start", command=self.start_bot)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(master, text="Stop", command=self.stop_bot, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(master, width=50, height=10)
        self.log_area.pack(pady=10)

    def start_bot(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.run_bot, daemon=True).start()

    def stop_bot(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def run_bot(self):
        if self.is_running:
            self.click_open_button()
            self.open_sandbox_alpha()
        self.stop_bot()  # Автоматично зупиняємо бота після виконання дій

    def log(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)  # Прокручуємо до останнього повідомлення

    def click_open_button(self):
        time.sleep(1)
        try:
            open_button = pyautogui.locateOnScreen('open_button.png', confidence=0.9)
            if open_button:
                pyautogui.click(pyautogui.center(open_button))
                self.log("Кнопка 'Open' успішно натиснута")
            else:
                self.log("Кнопка 'Open' не знайдена")
        except Exception as e:
            self.log(f"Виникла помилка: {e}")

    def open_sandbox_alpha(self):
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'tab')
        self.log("Змінено вкладку за допомогою комбінації Ctrl + Tab")

if __name__ == "__main__":
    root = tk.Tk()
    gui = BotGUI(root)
    root.mainloop()
