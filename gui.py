import tkinter as tk
import pandas as pd
from recommendation_system import data

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.data = data

    def create_widgets(self):

        self.search = tk.Entry(self, text='Input your movie here')
        self.search.pack(side='top')

        self.search_button = tk.Button(self, text='Search')
        self.search_button['command'] = self.search_movie
        self.search_button.pack(side='right')

        self.movies = tk.Label(self, text='No movie found')
        self.movies.pack(side='bottom')

    def search_movie(self):
        print(self.data[self.data.title == 'Avatar'].title.iloc[0])
        return self.data[self.data.title == 'Avatar'].title.iloc[0]

    def changetext():
        self.movies.config(text=self.search_movie())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
