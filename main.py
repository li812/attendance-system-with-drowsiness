import tkinter as tk
from tkinter import messagebox
import check
import capture_face
import train_image
import recognize
import monitor

def check_camera_gui():
    check.check_camera()
    messagebox.showinfo("Check Camera", "Camera checked successfully.")

def register_face_gui():
    def register():
        Id = id_entry.get()
        name = name_entry.get()
        if not Id or not name:
            messagebox.showerror("Error", "Please enter both ID and name.")
            return
        capture_face.register_face(Id, name)
        messagebox.showinfo("Success", "Face registered successfully.")

    register_window = tk.Toplevel(root)
    register_window.title("Register Face")

    id_label = tk.Label(register_window, text="ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(register_window)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    name_label = tk.Label(register_window, text="Name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(register_window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.grid(row=2, columnspan=2, padx=5, pady=5)

def train_gui():
    train_image.train()
    messagebox.showinfo("Train Image", "Image trained successfully.")

def recognize_attendance_gui():
    recognize.recognize_attendance()
    messagebox.showinfo("Recognize Attendance", "Attendance recognized successfully.")

def monitor_gui():
    monitor.monitor()
    messagebox.showinfo("Monitor", "Monitoring started.")

print("Before main block")

if __name__ == "__main__":
    print("Inside main block")
    root = tk.Tk()
    root.title("Face Recognition Attendance System")

    check_camera_button = tk.Button(root, text="Check Camera", command=check_camera_gui)
    check_camera_button.pack(pady=10)

    register_face_button = tk.Button(root, text="Register Face", command=register_face_gui)
    register_face_button.pack(pady=10)

    train_button = tk.Button(root, text="Train Image", command=train_gui)
    train_button.pack(pady=10)

    recognize_attendance_button = tk.Button(root, text="Recognize Attendance", command=recognize_attendance_gui)
    recognize_attendance_button.pack(pady=10)

    monitor_button = tk.Button(root, text="Monitor", command=monitor_gui)
    monitor_button.pack(pady=10)

    root.mainloop()

print("After main block")
