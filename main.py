import tkinter as tk
from tkinter import ttk, messagebox

class benkyou:
    def __init__(self, filename):
        self.bgColor= "#172E4A"
        self.buttonColor = "#E74C3C"
        self.bgSecondary ="#27174A"
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
        self.sets = {}
        self.listOfSetsPrinted = []
        self.filename = filename
        # Create all frames
        self.makeFrames()
        
        # Show the first frame
        self.displayFrame("HomePage")
    def makeFrames(self):
        """This function creates different frames so they can be showed later"""
        # We will start with making the Home Page Frame
        homeFrame = tk.Frame(self.container, bg=self.bgColor, bd =2)
        homeFrame.pack(fill="both", expand=True)
        # Now we will add the content to this page
        tk.Label(homeFrame, text="Welcome to Benkyou", font=("American Typewriter", 20), bg=self.bgColor, fg=self.buttonColor).pack(pady=5, anchor="center")


        #self.entryanwser = tk.Entry(homeFrame, font=("American Typewriter", 14), bg="#D79ECD")
        #self.entryanwser.pack(fill="x", padx=10, pady=5)

        #self.entryquestion = tk.Entry(homeFrame, font=("American Typewriter", 14), bg="#D79ECD")
        #self.entryquestion.pack(fill="x", padx=10, pady=5)

        homeButtons = tk.Frame(homeFrame, bg=self.bgColor)
        homeButtons.pack(fill="both", pady=100)

        #tk.Button(homeButtons,text="Submit", command=self.submit_data, bg="#D79ECD", font=("American Typewriter", 14)).pack(side=tk.LEFT, padx=5)
        tk.Button(homeButtons, text="View Sets", command=lambda: self.displayFrame("SetPage"), bg=self.buttonColor, font=("American Typewriter", 14)).pack(side=tk.BOTTOM, padx=10)
        tk.Button(homeButtons, text="Settings", command=lambda: self.displayFrame("SettingsPage"), bg=self.buttonColor, font=("American Typewriter", 14)).pack(side=tk.BOTTOM, padx=10)

        self.frames["HomePage"] = homeFrame

        self.setPage = tk.Frame(self.container, bg=self.bgColor, bd =2)
        self.setPage.pack(fill="both", expand=True)

        setButtons = tk.Frame(self.setPage, bg=self.bgColor)
        setButtons.pack(anchor="n",pady=10)
        tk.Button(setButtons, text="Create Set", command=lambda: self.displayFrame("CreateSetPage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.RIGHT, padx=10)
        tk.Button(setButtons, text="Back to Home", command=lambda: self.displayFrame("HomePage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.LEFT, pady=10)

        for i in self.sets.values():
            tk.Button(setButtons, text=i, command=lambda: self.displayFrame(i), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.TOP, padx=10)

        self.frames["SetPage"] = self.setPage

        createSetPage = tk.Frame(self.menuContainer, bg=self.bgSecondary, bd =2)
        createSetPage.pack(fill="both",padx=10,pady=10, expand=True)

        tk.Label(createSetPage, text="Create a Set", font=("Arial", 20), bg=self.bgSecondary, fg=self.buttonColor).pack(pady=5, anchor="center")
        tk.Label(createSetPage, text="Enter the name of the set", font=("Arial", 14), bg=self.bgSecondary, fg=self.buttonColor).pack(pady=5, anchor="center")

        self.entrySetName = tk.Entry(createSetPage, font=("American Typewriter", 14), bg=self.buttonColor)
        self.entrySetName.pack(fill="x", padx=10, pady=5)
            
        creatSetButtons = tk.Frame(createSetPage, bg=self.bgSecondary)
        creatSetButtons.pack(pady=10)
        tk.Button(creatSetButtons, text="Create Set", command=self.createSet, bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)


        self.frames["CreateSetPage"] = createSetPage

    def makeCard(self, parent, title, content):
        """Creates a card-like frame with a title and content"""
        card = tk.Frame(parent, bg=self.buttonColor, bd=2, relief="groove")
        card.pack(fill="x", pady=5)
        
        title_label = tk.Label(card, text=title, font=("American Typewriter", 16), bg=self.buttonColor)
        title_label.pack(anchor="w", padx=10, pady=5)
        
        content_label = tk.Label(card, text=content, font=("American Typewriter", 12), bg=self.buttonColor)
        content_label.pack(anchor="w", padx=10, pady=5)
        
        return card
    
    def createSet(self):
        """Creating a new set"""
        setName = self.entrySetName.get().strip()
        print(f"Creating set: {setName}")
        makeSetFrame = tk.Frame(self.container, bg=self.bgColor, bd=2)
        makeSetFrame.pack(fill="both", expand=True, padx=40, pady=40)

        tk.Label(makeSetFrame, text=f"Set: {setName}", font=("Arial", 20), bg=self.bgColor, fg=self.buttonColor).pack(pady=5, anchor="center")
        makeSetButtons = tk.Frame(makeSetFrame, bg=self.bgColor)
        makeSetButtons.pack(anchor="nw", pady=(10,0))
        tk.Button(makeSetButtons, text="Add Cards", command=lambda: self.displayFrame("MakeCardFrame"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)


        makebackButtons = tk.Frame(makeSetFrame, bg=self.bgColor)
        makebackButtons.pack(side=tk.BOTTOM,fill="x", pady=10)

        tk.Button(makebackButtons, text="Sets", command=lambda: self.displayFrame("SetPage"), bg=self.buttonColor, font=("Arial", 12)).pack(side=tk.BOTTOM, padx=10)

        self.sets[setName] = makeSetFrame
        print(f"Set '{setName}' created successfully.")
        self.displaySet()
        self.displayFrame("SetPage")
        self.entrySetName.delete(0, tk.END)
    def displaySet(self):
        """Display the sets in the SetPage"""
        for setName, setFrame in self.sets.items():
            if setName not in self.listOfSetsPrinted:
                tk.Button(self.setPage, text=setName, command=lambda name=setName: self.displayFrame(setName), bg=self.buttonColor, font=("Arial", 12)).pack(anchor="nw",side=tk.LEFT, padx=(10,0), pady=10)
                self.listOfSetsPrinted.append(setName)
        
        print("Sets displayed successfully.")

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
        for setFrame in self.sets.values():
            setFrame.pack_forget()
        self.container.pack_forget()
        self.menuContainer.pack_forget()

        if frameName == "CreateSetPage":
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

dafile = "data.txt"  # Example filename
app = benkyou(dafile)
app.root.mainloop()