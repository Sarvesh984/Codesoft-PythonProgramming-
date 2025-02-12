import tkinter as tk
from tkinter import messagebox
import random
import datetime

class QuoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Daily Quote")
        self.quotes = [
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
            "You miss 100% of the shots you don't take. - Wayne Gretzky"
        ]
        self.favorite_quotes = []
        self.current_quote = self.get_daily_quote()
        self.create_widgets()

    def get_daily_quote(self):
        today = datetime.date.today()
        return self.quotes[today.day % len(self.quotes)]

    def create_widgets(self):
        self.quote_label = tk.Label(self.root, text=self.current_quote, wraplength=400)
        self.quote_label.pack(padx=20, pady=20)
        self.share_button = tk.Button(self.root, text="Share Quote", command=self.share_quote)
        self.share_button.pack(pady=10)
        self.favorite_button = tk.Button(self.root, text="Add to Favorites", command=self.add_to_favorites)
        self.favorite_button.pack(pady=10)
        self.view_favorites_button = tk.Button(self.root, text="View Favorites", command=self.view_favorites)
        self.view_favorites_button.pack(pady=10)
        self.refresh_button = tk.Button(self.root, text="Refresh Quote", command=self.refresh_quote)
        self.refresh_button.pack(pady=10)

    def share_quote(self):
        import pyperclip
        pyperclip.copy(self.current_quote)
        messagebox.showinfo("Quote Shared", "Quote copied to clipboard.")

    def add_to_favorites(self):
        if self.current_quote not in self.favorite_quotes:
            self.favorite_quotes.append(self.current_quote)
            messagebox.showinfo("Quote Added", "Quote added to favorites.")
        else:
            messagebox.showinfo("Quote Already Added", "Quote is already in favorites.")

    def view_favorites(self):
        favorite_quotes_window = tk.Toplevel(self.root)
        favorite_quotes_window.title("Favorite Quotes")
        favorite_quotes_label = tk.Label(favorite_quotes_window, text="Favorite Quotes:")
        favorite_quotes_label.pack()
        for quote in self.favorite_quotes:
            quote_label = tk.Label(favorite_quotes_window, text=quote)
            quote_label.pack()

    def refresh_quote(self):
        self.current_quote = self.get_daily_quote()
        self.quote_label['text'] = self.current_quote

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QuoteApp()
    app.run()
