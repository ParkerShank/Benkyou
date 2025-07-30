import tkinter as tk
import json as js
from tkinter import ttk, messagebox
import random
class benkyou:
    def __init__(self, file):
        self.root = tk.Tk()
        self.root.title("Benkyou")
        self.root.geometry("600x400")
        self.root.configure(bg="#3d374a")
        
        # Container for all frames
        self.container = tk.Frame(self.root, bg="#3d374a")
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Dictionary to store all frames
        self.frames = {}
        self.mainColor = "#082E3F"
        self.buttonColor = "#C9EAF8"
        self.file = file
        self.cards = js.load(self.file)
        if  "count" in self.cards:
            self.count = self.cards["count"]
            self.numbers = [x for x in range(1,self.count)] # Puts all the numbers into a list
            for x in self.numbers:
                self.makeCard(self.cards["Question " + str(x)][0], self.cards["Question " + str(x)][1], x)

        else:
            self.count = 1
        self.lI = 0
        self.randomCard = []
        self.button_press = False
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
        # This is the make card frame
        makeCardFrame = tk.Frame(self.container, bg = self.mainColor, bd = 2)
        makeCardFrame.pack(fill = "both", expand=True)
        tk.Label(makeCardFrame, text="Please make a card", font=("American Typewriter", 20), bg = self.buttonColor).pack(pady=5, anchor="w")
        self.frames["MakeCardFrame"] = makeCardFrame
        self.entryquestion = tk.Entry(makeCardFrame, font=("American Typewriter", 14), bg="#D79ECD")
        self.entryquestion.pack(fill="x", padx=10, pady=5)
        self.entryanwser = tk.Entry(makeCardFrame, font=("American Typewriter", 14), bg="#D79ECD")
        self.entryanwser.pack(fill="x", padx=10, pady=5)
        
        # Buttons for the home page
        homeButtons = tk.Frame(homeFrame, bg="#3d374a")
        homeButtons.pack(pady=10)
        tk.Button(homeButtons, text="add Card", command=lambda: self.displayFrame("MakeCardFrame"), bg="#D79ECD", font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=10)
        #tk.Button(homeButtons, text="Make new set", command=self.make_new_set,bg = self.buttonColor,font= ("American Typewriter", 14)).pack(side=tk.LEFT,padx=10)
        tk.Button(homeButtons, text = "Study Cards", command=self.study_cards, bg = self.buttonColor,font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=10)
        # Buttons for the make card page
        cardMaker = tk.Entry(makeCardFrame, bg=self.buttonColor)
        cardMaker.pack(pady=10)
        

        tk.Button(cardMaker,text="Submit", command=self.submit_data, bg="#D79ECD", font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=5)
        tk.Button(cardMaker,text="Back Home", command=self.updateCards,bg= self.buttonColor, font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=10)

        self.frames["HomePage"] = homeFrame

        setPage = tk.Frame(self.container, bg="#FFFFFF", bd =2)
        setPage.pack(fill="both", expand=True)
        setButtons = tk.Frame(setPage,bg="#05F630", bd= 2)
        setButtons.pack(pady=50)
        tk.Button(setButtons, text="Back Home", command=lambda: self.displayFrame("HomePage"), bg= "#FBAAA0", font=("American Typewriter", 14)).pack(side=tk.RIGHT, padx= 20)
        self.frames["SetPage"] = setPage


    #def make_new_set(self):
    #   self.count = 1
    def study_cards(self):
        self.lI = 0
        self.randomCard.clear()
        numbers = [x for x in range(1,self.count)] # Puts all the numbers into a list
        
        temp = 0
        for x in range(self.count - 1):
            temp = random.choice(numbers)
            self.randomCard.append("Question " + str(temp))
            numbers.remove(temp)
        self.randomCard.append("HomePage")
        self.displayFrame(self.randomCard[self.lI])
    def updateCards(self):
        self.cards["count"] = self.count
        self.file.seek(0)
        js.dump(self.cards, file, indent=4)
        
        self.count = 1
        self.displayFrame("HomePage")
        return
    def makeCard(self, ques, answer, x):
        """Creates a card-like frame with a title and content"""
        card = tk.Frame(self.container, bg="#D79ECD", bd=2, relief="groove")
        card.pack(fill="x", pady=5)
        
        title_label = tk.Label(card, text=ques, font=("American Typewriter", 16), bg="#D79ECD")
        title_label.pack(anchor="w", padx=10, pady=5)
        
        content_label = tk.Label(card, text=answer, font=("American Typewriter", 12), bg="#D79ECD")
        content_label.pack(anchor="w", padx=10, pady=5)
        tk.Button(card, text="next", command= self.incr_lI, bg= "#FBAAA0", font=("American Typewriter", 14)).pack(anchor='s', padx= 20)
        self.frames["Question " + str(x)] = card
        print(card)
    def incr_lI(self):
        self.lI += 1
        self.displayFrame(self.randomCard[self.lI])
    def submit_data(self):
        answer = self.entryanwser.get().strip()
        question = self.entryquestion.get().strip()
        print(answer, question)
        if not answer or not question:
            messagebox.showerror("Error", "Please enter a name!")
            return
        self.cards["Question " + str(self.count)] = (question, answer)
        self.count += 1
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
file = open("test.json", 'r+')
app = benkyou(file)
app.root.mainloop()
