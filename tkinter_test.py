import tkinter
from tkinter import messagebox

def main():
    root = tkinter.Tk()
    root.title("Tkinter Test")
    root.geometry("300x200")
    
    label = tkinter.Label(root, text="Hermes x Sus Bot", font=("Arial", 14))
    label.pack(pady=20)
    
    button = tkinter.Button(root, text="Click me!", 
                           command=lambda: messagebox.showinfo("Info", "Tkinter is working!"))
    button.pack(padx=20, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
