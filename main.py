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
        tk.Label(homeFrame, text="Welcome to Benkyou", font=("American Typewriter", 20), bg="#D79ECD").pack(pady=5, anchor="w")


        self.entryanwser = tk.Entry(homeFrame, font=("American Typewriter", 14), bg="#D79ECD")
        self.entryanwser.pack(fill="x", padx=10, pady=5)

        self.entryquestion = tk.Entry(homeFrame, font=("American Typewriter", 14), bg="#D79ECD")
        self.entryquestion.pack(fill="x", padx=10, pady=5)

        homeButtons = tk.Frame(homeFrame, bg="#3d374a")
        homeButtons.pack(pady=10)

        #tk.Button(homeButtons,text="Submit", command=self.submit_data, bg="#D79ECD", font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=5)
        tk.Button(homeButtons, text="View Sets", command=lambda: self.displayFrame("SetPage"), bg="#D79ECD", font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=10)
        self.frames["HomePage"] = homeFrame

        setPage = tk.Frame(self.container, bg="#FFFFFF", bd =2)
        setPage.pack(fill="both", expand=True)

        self.frames["SetPage"] = setPage




    def makeCard(self, parent, title, content):
        """Creates a card-like frame with a title and content"""
        card = tk.Frame(parent, bg="#D79ECD", bd=2, relief="groove")
        card.pack(fill="x", pady=5)
        
        title_label = tk.Label(card, text=title, font=("American Typewriter", 16), bg="#D79ECD")
        title_label.pack(anchor="w", padx=10, pady=5)
        
        content_label = tk.Label(card, text=content, font=("American Typewriter", 12), bg="#D79ECD")
        content_label.pack(anchor="w", padx=10, pady=5)
        
        return card
    
    def submit_data(self):
        """Example function for data entry page"""
        answer = self.entryanwser.get().strip()
        question = self.entryquestion.get().strip()
        print(answer, question)
        if not answer:
            messagebox.showerror("Error", "Please enter a name!")
            return
        
        self.clear_form()
        return answer, question  

    def clear_form(self):
        """Clear the form fields"""
        self.entryanwser.delete(0, tk.END)
        self.entryquestion.delete(0, tk.END)
    
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