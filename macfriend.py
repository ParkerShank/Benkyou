import tkinter as tk
from tkinter import ttk, messagebox
import platform

class MultiPageApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Frame Switching Example")
        self.root.geometry("600x400")
        
        # Check if we're on macOS and configure accordingly
        self.is_mac = platform.system() == "Darwin"
        if self.is_mac:
            # Try to force light appearance on macOS
            try:
                self.root.tk.call('tk', 'appName', 'Frame Switching Example')
                # This might help with some color issues
                self.root.configure(bg="SystemWindowBackgroundColor")
            except:
                self.root.configure(bg="#f0f0f0")
        else:
            self.root.configure(bg="#f0f0f0")
        
        # Container for all frames
        container_bg = "SystemWindowBackgroundColor" if self.is_mac else "#f0f0f0"
        self.container = tk.Frame(self.root, bg=container_bg)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Dictionary to store all frames
        self.frames = {}
        
        # Create all frames
        self.create_frames()
        
        # Show the first frame
        self.show_frame("HomePage")
    
    def get_colors_for_platform(self):
        """Return appropriate colors based on the platform"""
        if self.is_mac:
            return {
                'frame_bg': 'SystemWindowBackgroundColor',
                'button_bg': 'SystemButtonFaceColor',
                'button_fg': 'SystemButtonTextColor',
                'label_bg': 'SystemWindowBackgroundColor',
                'label_fg': 'SystemWindowTextColor'
            }
        else:
            return {
                'frame_bg': '#e8f4fd',
                'button_bg': '#4CAF50',
                'button_fg': 'white',
                'label_bg': '#e8f4fd',
                'label_fg': 'black'
            }
    
    def create_mac_friendly_button(self, parent, text, command, bg_color, fg_color="white", width=15, height=2):
        """Create a button that works better on macOS"""
        if self.is_mac:
            # On macOS, use ttk.Button with styling for better color support
            style = ttk.Style()
            button_style = f"{text.replace(' ', '')}.TButton"
            
            # Configure the style - this may or may not work depending on macOS version
            try:
                style.configure(button_style, foreground=fg_color)
                button = ttk.Button(parent, text=text, command=command, style=button_style, width=width)
            except:
                # Fallback to regular button with system colors
                button = tk.Button(parent, text=text, command=command, 
                                 relief="raised", bd=2, font=("Arial", 12),
                                 width=width, height=height-1)
        else:
            # On other platforms, use regular buttons with custom colors
            button = tk.Button(parent, text=text, command=command,
                             bg=bg_color, fg=fg_color, font=("Arial", 12),
                             width=width, height=height)
        return button

    def create_frames(self):
        """Create all the different frames/pages"""
        
    def create_frames(self):
        """Create all the different frames/pages"""
        colors = self.get_colors_for_platform()
        
        # Home Page Frame
        home_frame = tk.Frame(self.container, bg=colors['frame_bg'], relief="ridge", bd=2)
        home_frame.pack(fill="both", expand=True)
        
        # Home page content
        tk.Label(home_frame, text="Welcome to Frame Switching Demo", 
                font=("Arial", 18, "bold"), bg=colors['label_bg'], fg=colors['label_fg']).pack(pady=30)
        
        tk.Label(home_frame, text="This demonstrates how to switch between different pages", 
                font=("Arial", 12), bg=colors['label_bg'], fg=colors['label_fg']).pack(pady=10)
        
        # Buttons to navigate to other frames
        button_frame = tk.Frame(home_frame, bg=colors['frame_bg'])
        button_frame.pack(pady=30)
        
        settings_btn = self.create_mac_friendly_button(button_frame, "Go to Settings", 
                                                      lambda: self.show_frame("SettingsPage"),
                                                      "#4CAF50")
        settings_btn.pack(side=tk.LEFT, padx=10)
        
        data_btn = self.create_mac_friendly_button(button_frame, "Go to Data Entry", 
                                                  lambda: self.show_frame("DataEntryPage"),
                                                  "#2196F3")
        data_btn.pack(side=tk.LEFT, padx=10)
        
        self.frames["HomePage"] = home_frame
        
        # Settings Page Frame
        settings_frame = tk.Frame(self.container, bg=colors['frame_bg'], relief="ridge", bd=2)
        
        tk.Label(settings_frame, text="Settings Page", 
                font=("Arial", 18, "bold"), bg=colors['label_bg'], fg=colors['label_fg']).pack(pady=30)
        
        # Some example settings
        settings_content = tk.Frame(settings_frame, bg=colors['frame_bg'])
        settings_content.pack(pady=20)
        
        tk.Label(settings_content, text="Theme:", font=("Arial", 12), 
                bg=colors['label_bg'], fg=colors['label_fg']).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        theme_var = tk.StringVar(value="Light")
        theme_menu = ttk.Combobox(settings_content, textvariable=theme_var, values=["Light", "Dark", "Blue"])
        theme_menu.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(settings_content, text="Font Size:", font=("Arial", 12), 
                bg=colors['label_bg'], fg=colors['label_fg']).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        font_scale = tk.Scale(settings_content, from_=8, to=20, orient=tk.HORIZONTAL, 
                            bg=colors['frame_bg'], fg=colors['label_fg'])
        font_scale.set(12)
        font_scale.grid(row=1, column=1, padx=10, pady=5)
        
        # Buttons
        settings_buttons = tk.Frame(settings_frame, bg=colors['frame_bg'])
        settings_buttons.pack(pady=30)
        
        save_btn = self.create_mac_friendly_button(settings_buttons, "Save Settings", 
                                                  self.save_settings, "#FF9800", width=12, height=1)
        save_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn1 = self.create_mac_friendly_button(settings_buttons, "Back to Home", 
                                                   lambda: self.show_frame("HomePage"), 
                                                   "#607D8B", width=12, height=1)
        back_btn1.pack(side=tk.LEFT, padx=10)
        
        self.frames["SettingsPage"] = settings_frame
        
        # Data Entry Page Frame
        data_frame = tk.Frame(self.container, bg=colors['frame_bg'], relief="ridge", bd=2)
        
        tk.Label(data_frame, text="Data Entry Page", 
                font=("Arial", 18, "bold"), bg=colors['label_bg'], fg=colors['label_fg']).pack(pady=30)
        
        # Form-like content
        form_frame = tk.Frame(data_frame, bg=colors['frame_bg'])
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text="Name:", font=("Arial", 12), 
                bg=colors['label_bg'], fg=colors['label_fg']).grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(form_frame, text="Description:", font=("Arial", 12), 
                bg=colors['label_bg'], fg=colors['label_fg']).grid(row=1, column=0, sticky="nw", padx=10, pady=10)
        self.desc_text = tk.Text(form_frame, font=("Arial", 12), width=25, height=4)
        self.desc_text.grid(row=1, column=1, padx=10, pady=10)
        
        # Data entry buttons
        data_buttons = tk.Frame(data_frame, bg=colors['frame_bg'])
        data_buttons.pack(pady=30)
        
        submit_btn = self.create_mac_friendly_button(data_buttons, "Submit Data", 
                                                    self.submit_data, "#9C27B0", width=12, height=1)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        clear_btn = self.create_mac_friendly_button(data_buttons, "Clear Form", 
                                                   self.clear_form, "#FF5722", width=12, height=1)
        clear_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn2 = self.create_mac_friendly_button(data_buttons, "Back to Home", 
                                                   lambda: self.show_frame("HomePage"), 
                                                   "#607D8B", width=12, height=1)
        back_btn2.pack(side=tk.LEFT, padx=10)
        
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