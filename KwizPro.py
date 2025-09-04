import tkinter as tk
from tkinter import messagebox, font as tkfont
import random
import os
import sys

try:
    from PIL import Image, ImageTk

    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# Sample questions data structure
questions_data = {
    "Mathematics": [
        ("What is 2 + 2?", "4", ["2", "3", "4", "5"]),
        ("What is 5 × 3?", "15", ["10", "12", "15", "18"]),
        ("What is the square root of 16?", "4", ["2", "3", "4", "5"]),
        ("What is 10 ÷ 2?", "5", ["3", "4", "5", "6"]),
        ("What is 7 - 3?", "4", ["2", "3", "4", "5"]),
        ("What is 8 + 7?", "15", ["14", "15", "16", "17"]),
        ("What is 9 × 2?", "18", ["16", "17", "18", "19"]),
        ("What is 20 ÷ 4?", "5", ["4", "5", "6", "7"]),
        ("What is 12 - 5?", "7", ["6", "7", "8", "9"]),
        ("What is 6 + 8?", "14", ["12", "13", "14", "15"])
    ],
    "Science": [
        ("What is the chemical symbol for water?", "H2O", ["H2O", "CO2", "O2", "H2"]),
        ("How many planets are in our solar system?", "8", ["7", "8", "9", "10"]),
        ("What gas do plants absorb from the atmosphere?", "Carbon dioxide",
         ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"]),
        ("What is the speed of light?", "299,792,458 m/s",
         ["299,792,458 m/s", "300,000,000 m/s", "299,000,000 m/s", "298,000,000 m/s"]),
        ("What is the largest organ in the human body?", "Skin", ["Heart", "Brain", "Liver", "Skin"]),
        ("What is the boiling point of water?", "100°C", ["90°C", "95°C", "100°C", "105°C"]),
        ("Which planet is closest to the Sun?", "Mercury", ["Venus", "Earth", "Mercury", "Mars"]),
        ("What is the hardest natural substance?", "Diamond", ["Gold", "Iron", "Diamond", "Silver"]),
        ("What type of animal is a dolphin?", "Mammal", ["Fish", "Reptile", "Mammal", "Amphibian"]),
        ("How many chambers does a human heart have?", "4", ["2", "3", "4", "5"])
    ],
    "History": [
        ("In what year did World War II end?", "1945", ["1943", "1944", "1945", "1946"]),
        ("Who was the first President of the United States?", "George Washington",
         ["John Adams", "Thomas Jefferson", "George Washington", "Benjamin Franklin"]),
        ("Which ancient wonder was located in Alexandria?", "Lighthouse",
         ["Colossus", "Lighthouse", "Hanging Gardens", "Mausoleum"]),
        ("What year did the Berlin Wall fall?", "1989", ["1987", "1988", "1989", "1990"]),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci",
         ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"]),
        ("In which year did the Titanic sink?", "1912", ["1910", "1911", "1912", "1913"]),
        ("Who was the first man to walk on the moon?", "Neil Armstrong",
         ["Buzz Aldrin", "Neil Armstrong", "John Glenn", "Alan Shepard"]),
        ("Which empire was ruled by Julius Caesar?", "Roman Empire",
         ["Greek Empire", "Roman Empire", "Byzantine Empire", "Ottoman Empire"]),
        ("What year did World War I begin?", "1914", ["1912", "1913", "1914", "1915"]),
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare",
         ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"])
    ],
    "Geography": [
        ("What is the capital of France?", "Paris", ["London", "Berlin", "Paris", "Madrid"]),
        ("Which is the largest ocean?", "Pacific", ["Atlantic", "Indian", "Pacific", "Arctic"]),
        ("What is the longest river in the world?", "Nile", ["Amazon", "Nile", "Mississippi", "Yangtze"]),
        ("Which country has the most natural lakes?", "Canada", ["Russia", "USA", "Canada", "Finland"]),
        ("What is the smallest country in the world?", "Vatican City",
         ["Monaco", "San Marino", "Vatican City", "Liechtenstein"]),
        ("Which desert is the largest in the world?", "Antarctica", ["Sahara", "Gobi", "Antarctica", "Arabian"]),
        ("What is the highest mountain in the world?", "Mount Everest",
         ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"]),
        ("Which continent has the most countries?", "Africa", ["Asia", "Europe", "Africa", "South America"]),
        ("What is the deepest ocean trench?", "Mariana Trench",
         ["Puerto Rico Trench", "Japan Trench", "Mariana Trench", "Peru-Chile Trench"]),
        ("Which river flows through Egypt?", "Nile", ["Amazon", "Mississippi", "Nile", "Euphrates"])
    ],
    "Literature": [
        ("Who wrote 'Pride and Prejudice'?", "Jane Austen",
         ["Charlotte Bronte", "Jane Austen", "Emily Dickinson", "Virginia Woolf"]),
        ("What is the first book in the Harry Potter series?", "Philosopher's Stone",
         ["Chamber of Secrets", "Philosopher's Stone", "Prisoner of Azkaban", "Goblet of Fire"]),
        ("Who wrote '1984'?", "George Orwell", ["Aldous Huxley", "George Orwell", "Ray Bradbury", "H.G. Wells"]),
        ("Which Shakespeare play features the character Hamlet?", "Hamlet",
         ["Macbeth", "Othello", "Hamlet", "King Lear"]),
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee",
         ["Toni Morrison", "Harper Lee", "Maya Angelou", "Flannery O'Connor"]),
        ("What is the opening line of 'A Tale of Two Cities'?", "It was the best of times",
         ["Call me Ishmael", "It was the best of times", "In a hole in the ground", "All children, except one"]),
        ("Who wrote 'The Great Gatsby'?", "F. Scott Fitzgerald",
         ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"]),
        ("Which novel begins with 'Call me Ishmael'?", "Moby Dick",
         ["The Old Man and the Sea", "Moby Dick", "20,000 Leagues Under the Sea", "Treasure Island"]),
        ("Who wrote 'Jane Eyre'?", "Charlotte Bronte",
         ["Emily Bronte", "Charlotte Bronte", "Anne Bronte", "George Eliot"]),
        ("What is the last book in the Chronicles of Narnia series?", "The Last Battle",
         ["The Magician's Nephew", "The Last Battle", "The Silver Chair", "The Horse and His Boy"])
    ],
    "Sports": [
        ("How many players are on a basketball team on the court?", "5", ["4", "5", "6", "7"]),
        ("In which sport would you perform a slam dunk?", "Basketball",
         ["Volleyball", "Basketball", "Tennis", "Badminton"]),
        ("How many holes are there in a full round of golf?", "18", ["16", "17", "18", "19"]),
        ("Which country won the FIFA World Cup in 2018?", "France", ["Germany", "Brazil", "France", "Argentina"]),
        ("How many players are on a soccer team on the field?", "11", ["9", "10", "11", "12"]),
        ("What is the maximum score possible in ten-pin bowling?", "300", ["250", "280", "300", "350"]),
        ("In tennis, what does the term 'love' mean?", "Zero", ["One", "Zero", "Fifteen", "Thirty"]),
        ("How many bases are there in baseball?", "4", ["3", "4", "5", "6"]),
        ("Which sport is played at Wimbledon?", "Tennis", ["Golf", "Cricket", "Tennis", "Badminton"]),
        ("How long is a marathon?", "26.2 miles", ["24.2 miles", "25.2 miles", "26.2 miles", "27.2 miles"])
    ],
    "Computer Science": [
        ("What does CPU stand for?", "Central Processing Unit",
         ["Central Processing Unit", "Computer Personal Unit", "Central Program Unit", "Computer Processing Unit"]),
        ("Which language is used for web development?", "HTML", ["Python", "C++", "HTML", "Java"]),
        ("What does RAM stand for?", "Random Access Memory",
         ["Read Access Memory", "Random Access Memory", "Rapid Access Memory", "Real Access Memory"]),
        ("Which company developed Java?", "Sun Microsystems", ["Microsoft", "Sun Microsystems", "Apple", "Google"]),
        ("What is the binary representation of 8?", "1000", ["1000", "1001", "1010", "1100"]),
        ("Which protocol is used for secure web browsing?", "HTTPS", ["HTTP", "HTTPS", "FTP", "SMTP"]),
        ("What does SQL stand for?", "Structured Query Language",
         ["Simple Query Language", "Structured Query Language", "Standard Query Language", "System Query Language"]),
        ("Which data structure uses LIFO?", "Stack", ["Queue", "Array", "Stack", "Tree"]),
        ("What is the full form of URL?", "Uniform Resource Locator",
         ["Universal Resource Locator", "Uniform Resource Locator", "Unique Resource Locator",
          "Universal Resource Link"]),
        ("Which sorting algorithm has O(n²) time complexity?", "Bubble Sort",
         ["Merge Sort", "Quick Sort", "Bubble Sort", "Heap Sort"])
    ],
    "Art & Culture": [
        ("Who painted the Starry Night?", "Vincent van Gogh",
         ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"]),
        ("Which museum houses the Mona Lisa?", "Louvre",
         ["British Museum", "Louvre", "Metropolitan Museum", "Uffizi Gallery"]),
        ("What art movement was Pablo Picasso associated with?", "Cubism",
         ["Impressionism", "Surrealism", "Cubism", "Expressionism"]),
        ("Which instrument has 88 keys?", "Piano", ["Organ", "Piano", "Harpsichord", "Accordion"]),
        ("Who composed 'The Four Seasons'?", "Antonio Vivaldi",
         ["Johann Sebastian Bach", "Wolfgang Mozart", "Antonio Vivaldi", "Ludwig Beethoven"]),
        ("What does Renaissance mean?", "Rebirth", ["Revival", "Rebirth", "Revolution", "Reform"]),
        ("Which dance originated in Argentina?", "Tango", ["Salsa", "Flamenco", "Tango", "Waltz"]),
        ("Who sculpted 'The Thinker'?", "Auguste Rodin", ["Michelangelo", "Auguste Rodin", "Donatello", "Bernini"]),
        ("What is the art of paper folding called?", "Origami", ["Kirigami", "Origami", "Ikebana", "Calligraphy"]),
        ("Which period came after the Renaissance?", "Baroque", ["Gothic", "Baroque", "Romantic", "Classical"])
    ]
}


class KwizPro:
    def __init__(self, root):
        self.root = root
        self.root.title("KwizPro - Interactive Quiz Application")
        self.root.state('zoomed')  # Maximize window on Windows

        # Load custom fonts with fallback
        try:
            self.quicksand_regular = tkfont.Font(family="Arial", size=16)
            self.quicksand_bold = tkfont.Font(family="Arial", size=16, weight="bold")
        except:
            self.quicksand_regular = ("Arial", 16)
            self.quicksand_bold = ("Arial", 16, "bold")

        # Set up main canvas with background color
        self.canvas = tk.Canvas(self.root, bg="#f0f8ff")  # Light blue background
        self.canvas.pack(fill="both", expand=True)

        # Create background
        self.create_background()
        self.bg_image = None  # To store background image reference

        # Initialize variables
        self.exam_duration = 600  # 10 minutes
        self.timer_label = None
        self.timer = None

        # Start with name screen
        self.name_screen()

    def load_background_image(self, image_path):
        """Load and resize background image"""
        try:
            if PIL_AVAILABLE and os.path.exists(image_path):
                # Get screen dimensions
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()

                # Open and resize image
                image = Image.open(image_path)
                image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

                # Convert to PhotoImage
                return ImageTk.PhotoImage(image)
            else:
                return None
        except Exception as e:
            print(f"Error loading background: {e}")
            return None

    def create_background(self):
        """Create background - either image or gradient"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Try to load your background image first
        bg_image = self.load_background_image(resource_path("assets/bgimage.jpg"))

        if bg_image:
            # Use your image as background
            self.canvas.create_image(0, 0, anchor="nw", image=bg_image)
            self.bg_image = bg_image  # Keep reference to prevent garbage collection
        else:
            # Fallback to gradient background
            self.create_gradient_background()

    def create_gradient_background(self):
        """Create a gradient background effect"""
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        # Create gradient rectangles
        for i in range(height):
            # Calculate color gradient from light blue to white
            ratio = i / height
            r = int(240 + (255 - 240) * ratio)  # Red component
            g = int(248 + (255 - 248) * ratio)  # Green component
            b = 255  # Blue component stays 255
            color = f"#{r:02x}{g:02x}{b:02x}"

            if i % 3 == 0:  # Draw every 3rd line for performance
                self.canvas.create_line(0, i, width, i, fill=color, width=3)

    def name_screen(self):
        self.clear_screen()
        self.create_background()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Reset variables
        self.name = ""
        self.selected_subjects = []
        self.current_question_index = 0
        self.score = 0
        self.questions = []
        self.remaining_time = self.exam_duration
        self.user_answers = []

        # Create decorative header
        self.canvas.create_rectangle(0, 0, screen_width, 120, fill="#4a90e2", outline="")

        # Create name input widgets
        title_label = tk.Label(
            self.root,
            text="🎯 QUIZ APPLICATION 🎯",
            font=("Arial", 28, "bold"),
            fg="white",
            bg='#4a90e2'
        )

        name_label = tk.Label(
            self.root,
            text="Enter your name to begin:",
            font=("Arial", 18),
            fg="#2B2B2B",
            bg='#f0f8ff'
        )

        self.name_entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            fg="#2B2B2B",
            bg="white",
            relief="solid",
            width=25,
            bd=2,
            justify='center'
        )

        next_button = tk.Button(
            self.root,
            text="🚀 START",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#4CAF50",
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.select_subjects
        )

        # Position widgets
        self.canvas.create_window(screen_width // 2, 60, window=title_label)
        self.canvas.create_window(screen_width // 2, 200, window=name_label)
        self.canvas.create_window(screen_width // 2, 260, window=self.name_entry)
        self.canvas.create_window(screen_width // 2, 340, window=next_button)

    def select_subjects(self):
        self.name = self.name_entry.get().strip()
        if not self.name:
            messagebox.showerror("Input Error", "Please enter your name.")
            return

        self.clear_screen()
        self.create_background()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Create decorative header
        self.canvas.create_rectangle(0, 0, screen_width, 100, fill="#4a90e2", outline="")

        # Welcome message
        welcome_text = f"Welcome {self.name}! 👋"
        welcome_label = tk.Label(
            self.root,
            text=welcome_text,
            font=("Arial", 20, "bold"),
            fg="white",
            bg='#4a90e2'
        )
        self.canvas.create_window(screen_width // 2, 35, window=welcome_label)

        # Title
        title_label = tk.Label(
            self.root,
            text="📚 Select exactly 4 subjects for your quiz:",
            font=("Arial", 18, "bold"),
            fg="#2B2B2B",
            bg='#f0f8ff'
        )
        self.canvas.create_window(screen_width // 2, 140, window=title_label)

        # Reset selection
        self.selected_subjects = []
        self.subject_buttons = {}
        subjects = list(questions_data.keys())

        # Create subject buttons in a 4x2 grid to show all 8 subjects
        cols = 4
        rows = 2

        # Calculate positions for better spacing
        button_width = 200
        button_height = 60
        total_width = cols * button_width + (cols - 1) * 30  # 30px spacing
        start_x = (screen_width - total_width) // 2 + button_width // 2
        start_y = 200
        spacing_x = button_width + 30  # button width + spacing
        spacing_y = button_height + 40  # button height + spacing

        # Subject icons for visual appeal
        subject_icons = {
            "Mathematics": "🔢",
            "Science": "🔬",
            "History": "📜",
            "Geography": "🌍",
            "Literature": "📚",
            "Sports": "⚽",
            "Computer Science": "💻",
            "Art & Culture": "🎨"
        }

        for index, subject in enumerate(subjects):
            row = index // cols
            col = index % cols
            x = start_x + col * spacing_x
            y = start_y + row * spacing_y

            icon = subject_icons.get(subject, "📖")
            btn_text = f"{icon}\n{subject}"

            btn = tk.Button(
                self.root,
                text=btn_text,
                font=("Arial", 12, "bold"),
                width=16,
                height=3,
                bg='white',
                fg='#2B2B2B',
                relief='solid',
                bd=2,
                cursor="hand2",
                activebackground='lightblue',
                command=lambda s=subject: self.toggle_subject(s)
            )
            self.canvas.create_window(x, y, window=btn)
            self.subject_buttons[subject] = btn

        # Selected count indicator
        self.count_label = tk.Label(
            self.root,
            text="Selected: 0/4",
            font=("Arial", 14, "bold"),
            fg="#e74c3c",
            bg='#f0f8ff'
        )
        self.canvas.create_window(screen_width // 2, start_y + rows * spacing_y + 20, window=self.count_label)

        # Start button
        start_btn = tk.Button(
            self.root,
            text="🎯 START QUIZ",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#e74c3c",
            relief="flat",
            padx=40,
            pady=15,
            cursor="hand2",
            command=self.start_quiz
        )
        self.canvas.create_window(screen_width // 2, screen_height - 100, window=start_btn)

    def toggle_subject(self, subject):
        if subject in self.selected_subjects:
            self.selected_subjects.remove(subject)
            self.subject_buttons[subject].config(bg='white', relief='solid', fg='#2B2B2B')
        else:
            if len(self.selected_subjects) >= 4:
                messagebox.showwarning("Limit Reached", "You can only select 4 subjects.")
                return
            self.selected_subjects.append(subject)
            self.subject_buttons[subject].config(bg='#4CAF50', relief='sunken', fg='white')

        # Update counter
        self.count_label.config(text=f"Selected: {len(self.selected_subjects)}/4")
        if len(self.selected_subjects) == 4:
            self.count_label.config(fg="#4CAF50")
        else:
            self.count_label.config(fg="#e74c3c")

    def start_quiz(self):
        if len(self.selected_subjects) != 4:
            messagebox.showerror("Selection Error", "Please select exactly 4 subjects.")
            return

        # Collect questions from selected subjects
        self.questions = []
        for subject in self.selected_subjects:
            subject_questions = questions_data[subject]
            if len(subject_questions) < 10:
                messagebox.showerror("Data Error", f"Not enough questions in {subject}.")
                return
            self.questions.extend(random.sample(subject_questions, 10))

        # Shuffle questions
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.user_answers = [None] * len(self.questions)
        self.remaining_time = self.exam_duration

        # Create timer
        self.create_timer()
        self.start_timer()
        self.show_question()

    def create_timer(self):
        screen_width = self.root.winfo_screenwidth()
        if self.timer_label:
            self.timer_label.destroy()

        self.timer_label = tk.Label(
            self.root,
            text="10:00",
            font=('Arial', 16, 'bold'),
            fg='red',
            bg='white'
        )
        self.canvas.create_window(screen_width - 100, 30, window=self.timer_label)

    def show_question(self):
        if self.current_question_index >= len(self.questions):
            return self.show_result()

        self.clear_screen(keep_timer=True)
        self.create_background()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Create header
        self.canvas.create_rectangle(0, 0, screen_width, 80, fill="#4a90e2", outline="")

        question, correct_answer, options = self.questions[self.current_question_index]
        self.correct_answer = correct_answer
        self.selected_option = None

        # Question number in header
        progress_text = f"Question {self.current_question_index + 1} of {len(self.questions)}"
        progress_label = tk.Label(
            self.root,
            text=progress_text,
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#4a90e2'
        )
        self.canvas.create_window(200, 40, window=progress_label)

        # Question text with background
        question_frame = tk.Frame(self.root, bg='white', relief='solid', bd=2)
        question_label = tk.Label(
            question_frame,
            text=question,
            font=('Arial', 16, 'bold'),
            fg='black',
            bg='white',
            wraplength=screen_width - 150,
            justify='center',
            padx=20,
            pady=20
        )
        question_label.pack()
        self.canvas.create_window(screen_width // 2, 160, window=question_frame)

        # Options with better styling
        self.option_buttons = []
        start_y = 260
        spacing = 70

        def select_option(opt, btn):
            for b in self.option_buttons:
                b.config(bg='white', relief='solid', fg='#2B2B2B')
            btn.config(bg='#4CAF50', relief='sunken', fg='white')
            self.selected_option = opt

        for i, option in enumerate(options):
            btn = tk.Button(
                self.root,
                text=f"{chr(65 + i)}. {option}",  # A, B, C, D
                font=('Arial', 14),
                width=60,
                height=2,
                anchor='w',
                justify='left',
                bg='white',
                fg='#2B2B2B',
                relief='solid',
                bd=2,
                cursor="hand2",
                activebackground='lightblue'
            )
            btn.config(command=lambda o=option, b=btn: select_option(o, b))
            self.option_buttons.append(btn)
            self.canvas.create_window(screen_width // 2, start_y + i * spacing, window=btn)

        # Restore previous selection if exists
        previous_selection = self.user_answers[self.current_question_index]
        if previous_selection:
            for btn in self.option_buttons:
                if previous_selection in btn['text']:
                    btn.config(bg='#4CAF50', relief='sunken', fg='white')
                    self.selected_option = previous_selection
                    break

        # Navigation buttons with better styling
        btn_y = start_y + len(options) * spacing + 50

        if self.current_question_index > 0:
            prev_btn = tk.Button(
                self.root,
                text="⬅️ Previous",
                font=('Arial', 14, 'bold'),
                padx=25,
                pady=10,
                bg='#6c757d',
                fg='white',
                relief='flat',
                cursor="hand2",
                command=self.prev_question
            )
            self.canvas.create_window(screen_width // 2 - 120, btn_y, window=prev_btn)

        next_text = "Finish Quiz" if self.current_question_index == len(self.questions) - 1 else "Next ➡️"
        next_btn = tk.Button(
            self.root,
            text=next_text,
            font=('Arial', 14, 'bold'),
            padx=25,
            pady=10,
            bg='#007bff',
            fg='white',
            relief='flat',
            cursor="hand2",
            command=self.next_question
        )
        self.canvas.create_window(screen_width // 2 + 120, btn_y, window=next_btn)

        self.update_timer_display()

    def next_question(self):
        self.user_answers[self.current_question_index] = self.selected_option
        self.current_question_index += 1
        self.show_question()

    def prev_question(self):
        self.user_answers[self.current_question_index] = self.selected_option
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

    def show_result(self):
        if self.timer:
            self.root.after_cancel(self.timer)

        self.clear_screen()
        self.create_background()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Create decorative header
        self.canvas.create_rectangle(0, 0, screen_width, 120, fill="#4a90e2", outline="")

        # Calculate score
        score = sum(1 for i, answer in enumerate(self.user_answers)
                    if answer == self.questions[i][1])
        self.score = score
        percentage = (self.score / len(self.questions)) * 100

        # Result header
        header_label = tk.Label(
            self.root,
            text="🎉 QUIZ COMPLETED! 🎉",
            font=('Arial', 24, 'bold'),
            fg='white',
            bg='#4a90e2'
        )
        self.canvas.create_window(screen_width // 2, 60, window=header_label)

        # Results card
        result_frame = tk.Frame(self.root, bg='white', relief='solid', bd=3)

        # Name
        name_label = tk.Label(
            result_frame,
            text=f"Student: {self.name}",
            font=('Arial', 18, 'bold'),
            fg='#2B2B2B',
            bg='white'
        )
        name_label.pack(pady=10)

        # Score
        score_text = f"Score: {self.score} / {len(self.questions)}"
        score_label = tk.Label(
            result_frame,
            text=score_text,
            font=('Arial', 22, 'bold'),
            fg='#4CAF50' if percentage >= 70 else '#e74c3c',
            bg='white'
        )
        score_label.pack(pady=5)

        # Percentage
        percentage_label = tk.Label(
            result_frame,
            text=f"Percentage: {percentage:.1f}%",
            font=('Arial', 18),
            fg='#007bff',
            bg='white'
        )
        percentage_label.pack(pady=5)

        # Grade
        if percentage >= 90:
            grade, emoji = "Excellent! 🌟", "🌟"
        elif percentage >= 80:
            grade, emoji = "Very Good! 👍", "👍"
        elif percentage >= 70:
            grade, emoji = "Good! 👍", "👍"
        elif percentage >= 60:
            grade, emoji = "Fair 📖", "📖"
        else:
            grade, emoji = "Needs Improvement 📚", "📚"

        grade_label = tk.Label(
            result_frame,
            text=f"{grade}",
            font=('Arial', 16, 'bold'),
            fg='#6f42c1',
            bg='white'
        )
        grade_label.pack(pady=(10, 20))

        self.canvas.create_window(screen_width // 2, 280, window=result_frame)

        # Buttons
        button_frame = tk.Frame(self.root, bg='#f0f8ff')

        restart_btn = tk.Button(
            button_frame,
            text="🔄 New Quiz",
            font=('Arial', 14, 'bold'),
            padx=25,
            pady=12,
            bg='#28a745',
            fg='white',
            relief='flat',
            cursor="hand2",
            command=self.name_screen
        )
        restart_btn.pack(side='left', padx=15)

        view_btn = tk.Button(
            button_frame,
            text="📋 Review Answers",
            font=('Arial', 14, 'bold'),
            padx=25,
            pady=12,
            bg='#007bff',
            fg='white',
            relief='flat',
            cursor="hand2",
            command=self.view_answers
        )
        view_btn.pack(side='left', padx=15)

        self.canvas.create_window(screen_width // 2, 450, window=button_frame)

    def view_answers(self):
        # Create new window for answers
        answer_window = tk.Toplevel(self.root)
        answer_window.title("📋 Answer Review")
        answer_window.state('zoomed')
        answer_window.configure(bg='#f0f8ff')

        # Create header
        header_frame = tk.Frame(answer_window, bg='#4a90e2', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)

        tk.Label(header_frame, text="📋 ANSWER REVIEW",
                 font=('Arial', 20, 'bold'), bg='#4a90e2', fg='white').pack(pady=25)

        # Create scrollable frame
        main_frame = tk.Frame(answer_window, bg='#f0f8ff')
        main_frame.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        canvas = tk.Canvas(main_frame, bg="#f0f8ff", highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        second_frame = tk.Frame(canvas, bg="#f0f8ff")
        canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # Display each question and answer
        for i, (question, correct_answer, options) in enumerate(self.questions):
            user_answer = self.user_answers[i] or "No Answer"
            is_correct = user_answer == correct_answer

            # Question frame with better styling
            q_frame = tk.Frame(second_frame, bg="white", relief="solid", bd=2)
            q_frame.pack(fill="x", padx=10, pady=8)

            # Question number and text
            q_header = tk.Frame(q_frame, bg='#e3f2fd')
            q_header.pack(fill='x')

            tk.Label(q_header, text=f"Question {i + 1}",
                     font=('Arial', 14, 'bold'), bg='#e3f2fd', fg='#1976d2').pack(anchor="w", padx=10, pady=5)

            tk.Label(q_frame, text=question, font=('Arial', 12, 'bold'),
                     bg="white", fg='#2B2B2B', wraplength=800, justify="left").pack(anchor="w", padx=15, pady=5)

            # Answer section
            answer_frame = tk.Frame(q_frame, bg='white')
            answer_frame.pack(fill='x', padx=15, pady=5)

            # User answer
            status_icon = "✅" if is_correct else "❌"
            color = "#4CAF50" if is_correct else "#f44336"

            tk.Label(answer_frame, text=f"{status_icon} Your Answer: {user_answer}",
                     font=('Arial', 11, 'bold'), fg=color, bg="white").pack(anchor="w")

            # Correct answer (only show if wrong)
            if not is_correct:
                tk.Label(answer_frame, text=f"✔️ Correct Answer: {correct_answer}",
                         font=('Arial', 11), fg="#2196F3", bg="white").pack(anchor="w", pady=(2, 0))

            tk.Label(q_frame, text="", bg="white", height=1).pack()  # Spacer

        # Summary at the end
        summary_frame = tk.Frame(second_frame, bg='#4CAF50', relief='solid', bd=2)
        summary_frame.pack(fill='x', padx=10, pady=20)

        correct_count = sum(1 for i, answer in enumerate(self.user_answers)
                            if answer == self.questions[i][1])

        tk.Label(summary_frame, text=f"📊 SUMMARY: {correct_count}/{len(self.questions)} Correct",
                 font=('Arial', 16, 'bold'), bg='#4CAF50', fg='white').pack(pady=15)

        # Close button
        close_btn = tk.Button(second_frame, text="❌ Close Review",
                              font=('Arial', 14, 'bold'), bg='#f44336', fg='white',
                              padx=30, pady=10, cursor="hand2",
                              command=answer_window.destroy)
        close_btn.pack(pady=20)

    def start_timer(self):
        if self.remaining_time > 0:
            self.timer = self.root.after(1000, self.decrement_timer)

    def decrement_timer(self):
        self.remaining_time -= 1
        self.update_timer_display()
        if self.remaining_time <= 0:
            messagebox.showinfo("Time Up!", "Time is up! Quiz will be submitted.")
            self.show_result()
        else:
            self.start_timer()

    def update_timer_display(self):
        if self.timer_label:
            mins = self.remaining_time // 60
            secs = self.remaining_time % 60
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")

    def clear_screen(self, keep_timer=False):
        for widget in self.root.winfo_children():
            if widget != self.canvas and (keep_timer and widget != self.timer_label):
                widget.destroy()
            elif not keep_timer and widget != self.canvas:
                widget.destroy()

        self.canvas.delete("all")

        if keep_timer and self.timer_label:
            # Recreate timer position after clearing
            screen_width = self.root.winfo_screenwidth()
            self.canvas.create_window(screen_width - 100, 30, window=self.timer_label)


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = KwizPro(root)

    # Try to set icon with proper error handling
    try:
        icon_path = resource_path("assets/app_icon.ico")
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
        else:
            print(f"Icon file not found at: {icon_path}")
            # Fallback - create a simple icon using tkinter
            root.iconbitmap(default='')  # Use default system icon
    except Exception as e:
        print(f"Error setting icon: {e}")
        # Continue without custom icon

    root.mainloop()