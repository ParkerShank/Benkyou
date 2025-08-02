import tkinter as tk
import json as js
from tkinter import ttk, messagebox
import random
class benkyou:
    def __init__(self, file):
        self.bgColor= "#011627"
        self.bgSecondary ="#FF3366"
        self.root = tk.Tk()
        self.root.title("Benkyou")
        self.root.geometry("600x400")
        self.root.configure(bg=self.bgColor)
        
        # Container for all frames
        self.container = tk.Frame(self.root, bg=self.bgColor)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        self.menuContainer = tk.Frame(self.root, bg=self.bgColor)
        # Dictionary to store all frames
        self.frames = {}
        # colors
        self.mainColor = "#082E3F"
        self.buttonColor = self.bgSecondary
        self.file = file # The file we read and write to
        # holds dictionary representation of all the flash card information
        self.set_names = self.safe_load_json()
        # used when making buttons for the set page
        self.listOfSetsPrinted = []
        # holds text information for cards in a single set
        self.cards = {}
        # Lets us know what set we're in for printing out the flash cards
        self.currentSet = ""
        # holds the number of questions in a set
        self.count = 1
        # Used when incrementing through the flash cards
        self.lI = 0
        # Helps increment through the flash cards in a random order
        self.randomCard = []
        # Create all frames
        self.makeFrames()
        
        # Show the first frame
        self.displayFrame("HomePage")

    def safe_load_json(self):
        self.file.seek(0)
        content = self.file.read().strip()
        if not content:
            self.file.seek(0)
            self.file.write("{}")  # write empty dict if file is empty
            self.file.flush()
            self.file.seek(0)
            return {}
        self.file.seek(0)
        return js.load(self.file)

    def makeFrames(self):
        """This function creates different frames so they can be showed later"""
        # We will start with making the Home Page Frame
        homeFrame = tk.Frame(self.container, bg=self.bgColor, bd =2)
        homeFrame.pack(fill="both", expand=True)
        # Now we will add the content to this page
        tk.Label(homeFrame, text="Welcome to Benkyou", font=("American Typewriter", 35), bg=self.bgColor, fg=self.bgSecondary).pack(pady=5, anchor="n")
        tk.Label(homeFrame, text="Flashcard and set maker", font=("American Typewriter", 14), bg=self.bgColor, fg=self.bgSecondary).pack(pady=5, anchor="n")

        # Buttons for the home page
        homeButtons = tk.Frame(homeFrame, bg=self.bgColor)
        homeButtons.pack(pady=40)
        tk.Button(homeButtons, text="View Sets", command=lambda: self.displayFrame("SetPage"), bg=self.buttonColor, font=("American Typewriter", 14)).pack(anchor='s',side=tk.RIGHT, padx=20)
        tk.Button(homeButtons, text="Exit", command=self.root.destroy, bg=self.buttonColor, font=("American Typewriter", 14)).pack(anchor='s',side=tk.RIGHT, padx= 20)
        #tk.Button(homeButtons, text="Settings", command=lambda: self.displayFrame("SettingsPage"), bg=self.buttonColor, font=("American Typewriter", 14)).pack(anchor="s",side=tk.LEFT, padx=40)
        #tk.Button(homeButtons, text="add Card", command=lambda: self.displayFrame("MakeCardFrame"), bg="#D79ECD", font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=10)
        #tk.Button(homeButtons, text="Make new set", command=self.make_new_set,bg = self.buttonColor,font= ("American Typewriter", 14)).pack(side=tk.LEFT,padx=10)
        self.frames["HomePage"] = homeFrame

        # set page
        self.setPage = tk.Frame(self.container, bg=self.bgColor, bd =2)
        self.setPage.pack(fill="both", expand=True)
        # set page buttons
        setButtons = tk.Frame(self.setPage, bg=self.bgColor)
        setButtons.pack(anchor="n",pady=10)
        tk.Button(setButtons, text="Create Set", command=lambda: self.displayFrame("CreateSetPage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.RIGHT, padx=10)
        tk.Button(setButtons, text="Back to Home", command=lambda: self.displayFrame("HomePage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.LEFT, pady=10)
        self.init_sets() # initializes the frames for cards that already exist


        self.frames["SetPage"] = self.setPage

        # This is the make card frame
        makeCardFrame = tk.Frame(self.container, bg = self.mainColor, bd = 2)
        makeCardFrame.pack(fill = "both", expand=True)
        tk.Label(makeCardFrame, text="Please make a card", font=("American Typewriter", 20), bg = self.mainColor, fg = self.bgSecondary).pack(pady=5, anchor="w")
        self.frames["MakeCardFrame"] = makeCardFrame
        self.entryquestion = tk.Entry(makeCardFrame, font=("American Typewriter", 14), bg=self.bgSecondary)
        self.entryquestion.pack(fill="x", padx=10, pady=5)
        self.entryanwser = tk.Entry(makeCardFrame, font=("American Typewriter", 14), bg=self.bgSecondary)
        self.entryanwser.pack(fill="x", padx=10, pady=5)
        # Buttons for the make card page
        cardMaker = tk.Entry(makeCardFrame, bg=self.buttonColor)
        cardMaker.pack(pady=10)
        

        tk.Button(cardMaker, text="Submit", command=self.submit_data, bg=self.bgSecondary, font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=5)
        tk.Button(cardMaker, text="Back Home", command=self.updateCards,bg= self.buttonColor, font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=10)
        self.frames["MakeCardFrame"] = makeCardFrame

        # makes a new set page for each set
        createSetPage = tk.Frame(self.container, bg="#BFB1C1", bd =2)
        createSetPage.pack(fill="both",padx=10,pady=10, expand=True)

        tk.Label(createSetPage, text="Create a Set", font=("Arial", 20), bg="#BFB1C1", fg=self.bgColor).pack(pady=5, anchor="center")
        tk.Label(createSetPage, text="Enter the name of the set", font=("Arial", 14), bg="#BFB1C1", fg=self.bgColor).pack(pady=5, anchor="center")

        self.entrySetName = tk.Entry(createSetPage, font=("American Typewriter", 14), bg=self.buttonColor)
        self.entrySetName.pack(fill="x", padx=10, pady=5)
            
        creatSetButtons = tk.Frame(createSetPage, bg=self.bgSecondary)
        creatSetButtons.pack(pady=10)
        tk.Button(creatSetButtons, text="Create Set", command=lambda: self.createSet(self.entrySetName.get()), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

        self.frames["CreateSetPage"] = createSetPage

        #setPage = tk.Frame(self.container, bg="#FFFFFF", bd =2)
        #setPage.pack(fill="both", expand=True)
        #setButtons = tk.Frame(setPage,bg="#05F630", bd= 2)
        #setButtons.pack(pady=50)
        #tk.Button(setButtons, text="Back Home", command=lambda: self.displayFrame("HomePage"), bg= "#FBAAA0", font=("American Typewriter", 14)).pack(side=tk.RIGHT, padx= 20)
        #self.frames["SetPage"] = setPage


    #def make_new_set(self):
    #   self.count = 1
    # initializes all the set frames that already exist
    def init_sets(self): # initializes all the set pages for already existing sets
        for setName in self.set_names:
            if setName != "default":
                print(f"Creating set: {setName}")
                makeSetFrame = tk.Frame(self.container, bg=self.bgColor, bd=2)
                makeSetFrame.pack(fill="both", expand=True, padx=40, pady=40)
                # makes labels and buttons
                tk.Label(makeSetFrame, text=f"Set: {setName}", font=("Arial", 20), bg=self.bgColor, fg=self.buttonColor).pack(pady=5, anchor="center")
                makeSetButtons = tk.Frame(makeSetFrame, bg=self.bgColor)
                makeSetButtons.pack(anchor="nw", pady=(10,0))
                tk.Button(makeSetButtons, text="add Card", command=lambda: self.displayFrame("MakeCardFrame"), bg=self.bgSecondary, font=("American Typewriter", 14)).pack(anchor='n', side=tk.LEFT, padx=10)
                tk.Button(makeSetButtons, text = "Study Cards", command=self.study_cards, bg = self.buttonColor,font=("American Typewriter", 14)).pack(anchor='n', side=tk.LEFT, padx=10)

                # button to go back
                makebackButtons = tk.Frame(makeSetFrame, bg=self.bgColor)
                makebackButtons.pack(side=tk.BOTTOM,fill="x", pady=10)
                tk.Button(makebackButtons, text="Sets", command=lambda: self.displayFrame("SetPage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.BOTTOM, padx=10)
                self.frames[setName] = makeSetFrame
                print(f"Set '{setName}' created successfully.")
        self.displaySet() # displays the set buttons on the main set page
    def createSet(self, name): # Creates new set pages and buttons
        # gets name
        setName = name.strip()
        if setName in self.set_names:
            messagebox.showerror("Error", "Set already exists")
            return
        print(f"Creating set: {setName}")
        makeSetFrame = tk.Frame(self.container, bg=self.bgColor, bd=2)
        makeSetFrame.pack(fill="both", expand=True, padx=40, pady=40)
        # makes labels and buttons
        tk.Label(makeSetFrame, text=f"Set: {setName}", font=("Arial", 20), bg=self.bgColor, fg=self.buttonColor).pack(pady=5, anchor="center")
        makeSetButtons = tk.Frame(makeSetFrame, bg=self.bgColor)
        makeSetButtons.pack(anchor="nw", pady=(10,0))
        tk.Button(makeSetButtons, text="add Card", command=lambda: self.displayFrame("MakeCardFrame"), bg=self.bgSecondary, font=("American Typewriter", 14)).pack(anchor='n', side=tk.LEFT, padx=10)
        tk.Button(makeSetButtons, text = "Study Cards", command=self.study_cards, bg = self.buttonColor,font=("American Typewriter", 14)).pack(anchor='n', side=tk.LEFT, padx=10)

        # button to go back
        makebackButtons = tk.Frame(makeSetFrame, bg=self.bgColor)
        makebackButtons.pack(side=tk.BOTTOM,fill="x", pady=10)

        tk.Button(makebackButtons, text="Sets", command=lambda: self.displayFrame("SetPage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.BOTTOM, padx=10)

        self.frames[setName] = makeSetFrame
        # adds empty set to text in case no cards are added
        self.set_names[setName] = ""
        self.file.seek(0)
        js.dump(self.set_names, self.file, indent=4)
        print(f"Set '{setName}' created successfully.")
        self.displaySet()
        self.displayFrame("SetPage")
        self.entrySetName.delete(0, tk.END)

    def displaySet(self): # Makes a button for all the sets in the main homepage
        """Display the sets in the SetPage"""
        for setName in self.set_names:
            if setName not in self.listOfSetsPrinted and setName != "default":
                tk.Button(self.setPage, text=setName, command=lambda name=setName: self.setGroup(name), bg=self.buttonColor, font=("Arial", 12)).pack(anchor="nw",side=tk.LEFT, padx=(10,0), pady=10)
                self.listOfSetsPrinted.append(setName)
    def setGroup(self, setName): # initializes all the proper information once a corresponding set button has been pressed
        self.currentSet = setName
        print(setName)
        if type(self.set_names[setName]) is dict:
            self.cards = self.set_names[setName]
            self.count = self.cards["count"]
            for x in range(1, self.count):
                self.makeCard(self.cards["Question " + str(x)][0], self.cards["Question " + str(x)][1],x)
        else:
            self.count = 1
            self.cards = {}
        self.displayFrame(setName)

    def makeCard(self, ques, answer, x): # Makes a new card frame using the question and answer
        """Creates a card-like frame with a question and answer """
        card = tk.Frame(self.container, bg=self.mainColor, bd=2, relief="groove")
        card.pack(fill="x", pady=5)
        
        title_label = tk.Label(card, text=ques, font=("American Typewriter", 16), fg=self.bgSecondary, bg= self.mainColor)
        title_label.pack(anchor="w", padx=10, pady=5)

        content_label = tk.Label(card, text=answer, font=("American Typewriter", 12), fg=self.mainColor, bg= self.mainColor)
        content_label.pack(anchor="w", padx=10, pady=5)
        tk.Button(card, text="back", command= lambda: (self.hideCard(content_label),self.de_incr_lI()), bg= self.bgSecondary, font=("American Typewriter", 14)).pack(anchor='s', side=tk.LEFT, padx= 20, pady=20)
        tk.Button(card, text="next", command= lambda: (self.hideCard(content_label),self.incr_lI()), bg= self.bgSecondary, font=("American Typewriter", 14)).pack(anchor='s', side=tk.RIGHT, padx= 20, pady=20)
        tk.Button(card, text = "Show answer", command=lambda:content_label.config(fg=self.bgSecondary),font=("American Typewriter", 14),bg = self.mainColor, fg= self.bgSecondary).pack(anchor='center', side=tk.BOTTOM,padx=20,pady=20 )
        tk.Button(card, text = "exit", command=lambda: self.displayFrame(self.currentSet), bg = self.mainColor, fg= self.bgSecondary, font=("American Typewriter", 14)).pack(anchor='center', side=tk.BOTTOM,padx=20,pady=5 )
    
        self.frames["Question " + str(x)] = card
        print(card)
    def hideCard(self,content_label):
            content_label.config(fg=self.mainColor)
    def submit_data(self): # Gets the information to make the card
        answer = self.entryanwser.get().strip()
        question = self.entryquestion.get().strip()
        print(answer, question)
        if not answer or not question:
            messagebox.showerror("Error", "Please enter a name!")
            return
        self.cards["Question " + str(self.count)] = (question, answer)
        self.makeCard(question, answer, self.count)
        self.count += 1
        self.clear_form()
        return answer, question
    def clear_form(self): # Clears the fields for the next question
        """Clear the form fields"""
        self.entryanwser.delete(0, tk.END)
        self.entryquestion.delete(0, tk.END)

    def updateCards(self): # Updates the set and the file once all cards have been inputted
        self.cards["count"] = self.count
        self.set_names[self.currentSet] = self.cards
        
        self.file.seek(0)
        js.dump(self.set_names, self.file, indent=4)
        self.displayFrame(self.currentSet)
        return
    
    def study_cards(self): # Goes through all the cards in a set
        if len(self.cards) == 0: # exits if no cards in set
            messagebox.showerror("Error", "Set Empty")
            return
        self.lI = 1
        self.randomCard.clear()
        numbers = [x for x in range(1,self.count)] # Puts all the numbers into a list
        self.randomCard.append(self.currentSet) # Goes back to the set
        temp = 0
        for x in range(self.count - 1): # gets the question numbers in a random order
            temp = random.choice(numbers)
            self.randomCard.append("Question " + str(temp))
            numbers.remove(temp)
        self.randomCard.append(self.currentSet) # Goes back to the set
        self.displayFrame(self.randomCard[self.lI])
    
    def de_incr_lI(self): # Goes backwards
        self.lI -= 1
        self.displayFrame(self.randomCard[self.lI])
    def incr_lI(self): # Goes forwards
        self.lI += 1
        self.displayFrame(self.randomCard[self.lI]) 

    
    def displayFrame(self, frameName): # Displays the frame
        """Hide all frames and show the needed frame"""
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        for setFrame in self.sets.values():
            setFrame.pack_forget()
        self.container.pack_forget()
        self.menuContainer.pack_forget()

        if frameName == "CreateSetPage" or frameName == "SettingsPage":
            self.menuContainer.pack(fill="both", expand=True, padx=35, pady=35)
            frame = self.frames[frameName]
            frame.pack(fill="both", expand=True)
        else:
            self.container.pack(fill="both", expand=True, padx=10, pady=10)
            # Show the requested frame
            try:
                frame = self.frames[frameName]
                frame.pack(fill="both", expand=True)
            except:
                set = self.sets[frameName]
                set.pack(fill="both", expand=True) if set else None
        
        print(f"Frame: {frameName}")  # For debugging
    def changeColorMode(self):
        """Change the color mode of the application"""
        if self.colorMode == "Dark":
            self.bgColor = "#FFFFFF"
            self.buttonColor = "#000000"
            self.bgSecondary = "#F0F0F0"
            self.colorMode = "Light"
        else:
            self.bgColor = "#172E4A"
            self.buttonColor = "#E74C3C"
            self.bgSecondary = "#27174A"
            self.colorMode = "Dark"

        # Update all frames with new colors
        for frame in self.frames.values():
            frame.configure(bg=self.bgColor)
        for setFrame in self.sets.values():
            setFrame.configure(bg=self.bgColor)
        
        # Repack the container to apply changes
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        print(f"Color mode changed to {self.colorMode}")
dafile = "data.txt"  # Example filename
app = benkyou(dafile)
app.root.mainloop()
