# 🎓 AI Face Recognition Attendance System

A Python-based facial recognition attendance system using `face_recognition`, `OpenCV`, and `Tkinter`. It uses live webcam input to identify registered students and mark their attendance automatically.

---

## 📸 Features

- Real-time face detection and recognition using webcam.
- Static student database with face encodings.
- Attendance marking with time log and GUI notification.
- Simple Tkinter GUI for ease of use.
- Encapsulation using OOP principles.

---

## 🧰 Technologies Used

- [Python 3.12.0](https://www.python.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [OpenCV](https://opencv.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PIL (Pillow)](https://python-pillow.org/)

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/face-authentication-attendance.git
cd face-authentication-attendance
```
### 2. Install Dependencies

```bash
pip install face_recognition opencv-python Pillow numpy
```

### 3. Add Students

```python
Student_List.add_to_students("Your Name", False, "your_photo.jpg")
```

### 4. Run the App

```bash
python Face_Authentication.py
```
## Authors
Developed by Usman Nisar, Hasaan Ayub, Momin Hayat, Shaleem Raza @UETTaxila
