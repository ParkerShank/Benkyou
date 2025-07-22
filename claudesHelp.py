import tkinter as tk
from tkinter import ttk, messagebox

class MultiPageApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Frame Switching Example")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        # Container for all frames
        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Dictionary to store all frames
        self.frames = {}
        
        # Create all frames
        self.create_frames()
        
        # Show the first frame
        self.show_frame("HomePage")
    
    def create_frames(self):
        """Create all the different frames/pages"""
        
        # Home Page Frame
        home_frame = tk.Frame(self.container, bg="#e8f4fd", relief="ridge", bd=2)
        home_frame.pack(fill="both", expand=True)
        
        # Home page content
        tk.Label(home_frame, text="Welcome to Frame Switching Demo", 
                font=("Arial", 18, "bold"), bg="#e8f4fd").pack(pady=30)
        
        tk.Label(home_frame, text="This demonstrates how to switch between different pages", 
                font=("Arial", 12), bg="#e8f4fd").pack(pady=10)
        
        # Buttons to navigate to other frames
        button_frame = tk.Frame(home_frame, bg="#e8f4fd")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Go to Settings", 
                 command=lambda: self.show_frame("SettingsPage"),
                 bg="#4CAF50", fg="white", font=("Arial", 12), 
                 width=15, height=2).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="Go to Data Entry", 
                 command=lambda: self.show_frame("DataEntryPage"),
                 bg="#2196F3", fg="white", font=("Arial", 12), 
                 width=15, height=2).pack(side=tk.LEFT, padx=10)
        
        self.frames["HomePage"] = home_frame
        
        # Settings Page Frame
        settings_frame = tk.Frame(self.container, bg="#fff3e0", relief="ridge", bd=2)
        
        tk.Label(settings_frame, text="Settings Page", 
                font=("Arial", 18, "bold"), bg="#fff3e0").pack(pady=30)
        
        # Some example settings
        settings_content = tk.Frame(settings_frame, bg="#fff3e0")
        settings_content.pack(pady=20)
        
        tk.Label(settings_content, text="Theme:", font=("Arial", 12), bg="#fff3e0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        theme_var = tk.StringVar(value="Light")
        theme_menu = ttk.Combobox(settings_content, textvariable=theme_var, values=["Light", "Dark", "Blue"])
        theme_menu.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(settings_content, text="Font Size:", font=("Arial", 12), bg="#fff3e0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        font_scale = tk.Scale(settings_content, from_=8, to=20, orient=tk.HORIZONTAL, bg="#fff3e0")
        font_scale.set(12)
        font_scale.grid(row=1, column=1, padx=10, pady=5)
        
        # Buttons
        settings_buttons = tk.Frame(settings_frame, bg="#fff3e0")
        settings_buttons.pack(pady=30)
        
        tk.Button(settings_buttons, text="Save Settings", 
                 command=self.save_settings,
                 bg="#FF9800", fg="white", font=("Arial", 12), 
                 width=12, height=1).pack(side=tk.LEFT, padx=10)
        
        tk.Button(settings_buttons, text="Back to Home", 
                 command=lambda: self.show_frame("HomePage"),
                 bg="#607D8B", fg="white", font=("Arial", 12), 
                 width=12, height=1).pack(side=tk.LEFT, padx=10)
        
        self.frames["SettingsPage"] = settings_frame
        
        # Data Entry Page Frame
        data_frame = tk.Frame(self.container, bg="#f3e5f5", relief="ridge", bd=2)
        
        tk.Label(data_frame, text="Data Entry Page", 
                font=("Arial", 18, "bold"), bg="#f3e5f5").pack(pady=30)
        
        # Form-like content
        form_frame = tk.Frame(data_frame, bg="#f3e5f5")
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f3e5f5").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Description:", font=("Arial", 12), bg="#f3e5f5").grid(row=1, column=0, sticky="nw", padx=10, pady=10)
        self.desc_text = tk.Text(form_frame, font=("Arial", 12), width=25, height=4)
        self.desc_text.grid(row=1, column=1, padx=10, pady=10)
        
        # Data entry buttons
        data_buttons = tk.Frame(data_frame, bg="#f3e5f5")
        data_buttons.pack(pady=30)
        
        tk.Button(data_buttons, text="Submit Data", 
                 command=self.submit_data,
                 bg="#9C27B0", fg="white", font=("Arial", 12), 
                 width=12, height=1).pack(side=tk.LEFT, padx=10)
        
        tk.Button(data_buttons, text="Clear Form", 
                 command=self.clear_form,
                 bg="#FF5722", fg="white", font=("Arial", 12), 
                 width=12, height=1).pack(side=tk.LEFT, padx=10)
        
        tk.Button(data_buttons, text="Back to Home", 
                 command=lambda: self.show_frame("HomePage"),
                 bg="#607D8B", fg="white", font=("Arial", 12), 
                 width=12, height=1).pack(side=tk.LEFT, padx=10)
        
        self.frames["DataEntryPage"] = data_frame
    
    def show_frame(self, frame_name):
        """Hide all frames and show the requested one"""
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()
        
        # Show the requested frame
        frame = self.frames[frame_name]
        frame.pack(fill="both", expand=True)
        
        print(f"Switched to: {frame_name}")  # For debugging
    
    def save_settings(self):
        """Example function for settings page"""
        messagebox.showinfo("Settings", "Settings saved successfully!")
    
    def submit_data(self):
        """Example function for data entry page"""
        name = self.name_entry.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        print(name, description)  # For debugging
        if not name:
            messagebox.showerror("Error", "Please enter a name!")
            return
        
        messagebox.showinfo("Success", f"Data submitted!\nName: {name}\nDescription: {description}")
        self.clear_form()
    
    def clear_form(self):
        """Clear the form fields"""
        self.name_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

# Example of how to run the application
if __name__ == "__main__":
    app = MultiPageApp()
    app.run()