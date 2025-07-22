import tkinter as tk
from tkinter import ttk, messagebox

class benkyou:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Benkyou")
        self.root.geometry("600x400")
        self.root.configure(bg="#3d374a")
        
        # Container for all frames
        self.container = tk.Frame(self.root, bg="#3d374a")
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Dictionary to store all frames
        self.frames = {}
        
        # Create all frames
        self.makeFrames()
        
        # Show the first frame
        self.displayFrame("HomePage")
    def makeFrames(self):
        """This function creates different frames so they can be showed later"""
        # We will start with making the Home Page Frame
        homeFrame = tk.Frame(self.container, bg="#3d374a", bd =2)
        homeFrame.pack(fill="both", expand=True)
        # Now we will add the content to this page
        tk.Label(homeFrame, text="Welcome to Benkyou", font=("American Typewriter", 20), bg="#D79ECD").pack(pady=5)

        self.frames["HomePage"] = homeFrame

    def displayFrame(self, frameName):
        """Hide all frames and show the needed frame"""
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        
        # Show the requested frame
        frame = self.frames[frameName]
        frame.pack(fill="both", expand=True)
        
        print(f"Frame: {frameName}")  # For debugging
app = benkyou()
app.root.mainloop()