import tkinter as tk
from tkinter import Label, Button, messagebox
import cv2
from PIL import Image, ImageTk
import face_recognition
import numpy as np
from datetime import datetime
class Student:
    
    def __init__(self, name, is_present, image_path):
        self.name = name
        self.is_present = is_present
        self.image_path = image_path
        self.encoding = None

    def compute_encoding(self):
        # Encoding self_image 
        try:
            image = face_recognition.load_image_file('path/to/image.jpg')
            self.encoding = face_recognition.face_encodings(self_image)[0]
        except FileNotFoundError:
            self.encoding = None
        except Exception as e:
            self.encoding = None
        
class Student_List:
    students = []

    @classmethod
    def initialize(cls):
        cls.add_to_students("Usman Nisar", False, "MANI.jpg")

    @classmethod
    def add_to_students(cls, name, is_present, image_path):
        s1 = Student(name , is_present, image_path)
        s1.compute_encoding()
        cls.students.append(s1)
        
class AttendanceApp:
    def __init__(self, root):
        # GUI App
        self.root = root
        self.root.title("AI Attendance System")
        self.cap = cv2.VideoCapture(0)

        # Guard Clause If Camera Not Available
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open camra")
            root.destroy()
        
        self.title_label = Label(root, text="📸 AI Attendance System", font=("Helvetica", 40, "bold"))
        self.title_label.pack(pady=10)
        self.video_label = Label(root)
        self.video_label.pack()
        self.root.configure(bg="#00000A")
        self.mark_btn = Button(root,text="Mark Attendance",font=("Arial", 14, "bold"),fg="white",bg="#00FFFF",activebackground="#00CED1",activeforeground="black",relief="raised",bd=3,command=self.mark_attendance)
        self.mark_btn.pack(pady=10)

        # Event Handling 
        def on_enter(e):
            self.mark_btn['background'] = '#00CED1'
            self.mark_btn['foreground'] = 'black'
        def on_leave(e):
            self.mark_btn['background'] = '#00FFFF'
            self.mark_btn['foreground'] = 'white'
            
        # Bind hover events
        self.mark_btn.bind("<Enter>", on_enter)
        self.mark_btn.bind("<Leave>", on_leave)

        # Initializing Students
        Student_List.initialize()
        for i,x in enumerate(Student_List.students):
            if(x.encoding == None):
                messagebox.showerror("Error", f"{x.name}'s Encoding not Found!")

        # If No Students found in database 
        if(len(Student_List.students)==0):
            messagebox.showerror("Data Error", "No Student Encodings found!")
            root.destroy()
                
        self.update_frame()
        
    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            self.current_frame = frame
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            self.root.after(30, self.update_frame)
            
    def mark_attendance(self):
        if hasattr(self, 'current_frame'):
            img = self.current_frame
            cv2.imwrite("temp.jpg",self.current_frame)
            identity = self.predict()
            if isinstance(identity,Student):
                cv2.imwrite("output.jpg",self.current_frame)
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                record = f"{identity} - {now}"
                messagebox.showinfo("✅ Attendance Marked", f"{identity.name} marked present at {now}")
            else:
                messagebox.showwarning("Unknown", "Face not recognized!")

    def predict(self):
        # Encoding Captured frame
        captured_frame = face_recognition.load_image_file("temp.jpg")
        frame_encoding = face_recognition.face_encodings(captured_frame)[0]

        for i,x in enumerate(Student_List.students):
            if x.encoding != None:
                results = face_recognition.compare_faces([x.encoding], frame_encoding)
                if(results[0] == True):
                    x.is_present = True
                    return x
        
        return None

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
