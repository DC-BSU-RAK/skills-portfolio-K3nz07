from tkinter import *
from tkinter import ttk, messagebox
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENT_FILE = os.path.join(SCRIPT_DIR, "..", "A1 - Resources", "studentMarks.txt")


class Student:
    def __init__(self, student_num, name, coursework1, coursework2, coursework3, exam):
        self.student_num = student_num
        self.name = name
        self.coursework1 = int(coursework1)
        self.coursework2 = int(coursework2)
        self.coursework3 = int(coursework3)
        self.exam = int(exam)

    def total_coursework(self):
        t = self.coursework1 + self.coursework2 + self.coursework3
        return t

    def overall_marks(self):
        return self.total_coursework() + self.exam

    def percentage(self):
        return (self.overall_marks() / 160) * 100

    def grade(self):
        p = self.percentage()
        if p >= 70:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 50:
            return "C"
        elif p >= 40:
            return "D"
        return "F"

    def format_record(self):
        return (
            "Student Name: " + self.name + "\n"
            "Student Number: " + self.student_num + "\n"
            "Total Coursework Mark: " + str(self.total_coursework()) + "/60\n"
            "Exam Mark: " + str(self.exam) + "/100\n"
            "Overall Percentage: " + f"{self.percentage():.2f}%" + "\n"
            "Grade: " + self.grade() + "\n"
        )


class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.attributes("-fullscreen", True)
        self.root.config(bg="#1a1f3a")

        self.students = []
        self.load_students()
        self.setup_ui()

    def load_students(self):
        try:
            with open(STUDENT_FILE, "r") as f:
                lines = f.readlines()
                for line in lines[1:]:
                    parts = line.strip().split(",")
                    if len(parts) < 6:
                        continue
                    s = Student(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    self.students.append(s)
        except:
            messagebox.showerror("Error", "Could not load student file.")

    def setup_ui(self):
        title = Label(self.root, text="Student Management System", font=("Arial", 30, "bold"),
                      bg="#1a1f3a", fg="#00d9ff")
        title.pack(pady=25)

        main = Frame(self.root, bg="#23324f")
        main.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.75, relheight=0.75)

        left = Frame(main, bg="#23324f")
        left.pack(side=LEFT, fill=Y, padx=15, pady=15)

        Label(left, text="Menu", fg="#00d9ff", bg="#23324f",
              font=("Arial", 18, "bold")).pack(pady=(10, 25))

        btn_style = {
            "font": ("Arial", 12, "bold"),
            "fg": "white",
            "bd": 0,
            "relief": "raised",
            "cursor": "hand2",
            "activebackground": "#00d9ff",
            "activeforeground": "black",
            "width": 24,
            "height": 2
        }

        Button(left, text="1. View All Students",
               command=self.view_all_students, bg="#1e3d59", **btn_style).pack(pady=8)

        Button(left, text="2. View Individual Student",
               command=self.view_individual_student, bg="#1e3d59", **btn_style).pack(pady=8)

        Button(left, text="3. Highest Scoring Student",
               command=self.show_highest, bg="#1e3d59", **btn_style).pack(pady=8)

        Button(left, text="4. Lowest Scoring Student",
               command=self.show_lowest, bg="#1e3d59", **btn_style).pack(pady=8)

        exit_btn_style = btn_style.copy()
        exit_btn_style["activebackground"] = "#ff6b6b"
        Button(left, text="Exit", command=self.root.destroy,
               bg="#c0392b", **exit_btn_style).pack(pady=(35, 0))

        right = Frame(main, bg="#1a1f3a")
        right.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)

        scroll = Scrollbar(right)
        scroll.pack(side=RIGHT, fill=Y)

        self.display_text = Text(right, font=("Courier New", 11),
                                 bg="#1a1f3a", fg="white",
                                 wrap=WORD, yscrollcommand=scroll.set)
        self.display_text.pack(fill=BOTH, expand=True)
        scroll.config(command=self.display_text.yview)

    def clear_display(self):
        self.display_text.delete(1.0, END)

    def view_all_students(self):
        self.clear_display()
        self.display_text.insert(END, "ALL STUDENT RECORDS\n")
        self.display_text.insert(END, "-" * 60 + "\n\n")

        total = 0
        for s in self.students:
            self.display_text.insert(END, s.format_record() + "\n")
            total += s.percentage()

        if self.students:
            avg = total / len(self.students)
            self.display_text.insert(END, "Average Percentage: " + f"{avg:.2f}%" + "\n")

    def view_individual_student(self):
        win = Toplevel(self.root)
        win.title("Students")
        win.geometry("350x450")
        win.config(bg="#23324f")
        win.grab_set()

        Label(win, text="Select Student", bg="#23324f", fg="#00d9ff",
              font=("Arial", 15, "bold")).pack(pady=15)

        frame = Frame(win, bg="#23324f")
        frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)

        lb = Listbox(frame, bg="#1a1f3a", fg="white",
                     font=("Arial", 10), yscrollcommand=scroll.set)
        lb.pack(side=LEFT, fill=BOTH, expand=True)
        scroll.config(command=lb.yview)

        for s in self.students:
            lb.insert(END, s.student_num + " - " + s.name)

        def show_sel():
            sel = lb.curselection()
            if sel:
                idx = sel[0]
                st = self.students[idx]
                self.clear_display()
                self.display_text.insert(END, st.format_record())
                win.destroy()
            else:
                messagebox.showwarning("Warning", "Please select a student")

        Button(win, text="View", bg="#002244", fg="white",
               font=("Arial", 11), width=15, command=show_sel).pack(pady=10)

        Button(win, text="Close", bg="#b93232", fg="white",
               font=("Arial", 11), width=15, command=win.destroy).pack()

    def show_highest(self):
        if not self.students:
            return
        h = max(self.students, key=lambda x: x.overall_marks())
        self.clear_display()
        self.display_text.insert(END, "HIGHEST SCORING STUDENT\n\n")
        self.display_text.insert(END, h.format_record())

    def show_lowest(self):
        if not self.students:
            return
        l = min(self.students, key=lambda x: x.overall_marks())
        self.clear_display()
        self.display_text.insert(END, "LOWEST SCORING STUDENT\n\n")
        self.display_text.insert(END, l.format_record())


def main():
    root = Tk()
    StudentManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
