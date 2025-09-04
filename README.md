# KwizPro - Interactive Quiz Application

A modern, feature-rich quiz application built with Python and Tkinter that provides an engaging learning experience across multiple subjects.

![KwizPro Icon](assets/app_icon.jpeg)

## 🌟 Features

- **Multi-Subject Quiz System**: Choose from 8 different categories including Mathematics, Science, History, Geography, Literature, Sports, Computer Science, and Art & Culture
- **Customizable Quiz Experience**: Select exactly 4 subjects from available categories to create your personalized quiz
- **Timed Examinations**: 10-minute timer with real-time countdown display
- **Interactive User Interface**: Modern GUI with gradient backgrounds, custom styling, and intuitive navigation
- **Progress Tracking**: Visual progress indicators and question navigation (Previous/Next)
- **Comprehensive Results**: Detailed score analysis with percentage calculations and grade assignments
- **Answer Review System**: Complete review of all questions with correct answers and user responses
- **Responsive Design**: Full-screen application that adapts to different screen sizes
- **Background Image Support**: Custom background images with fallback to gradient backgrounds

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- tkinter (usually included with Python)
- PIL (Pillow) - Optional, for background image support

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/KwizPro.git
   cd KwizPro
   ```

2. **Install required dependencies**:
   ```bash
   pip install Pillow  # Optional, for image support
   ```

3. **Create assets folder** (optional):
   ```bash
   mkdir assets
   ```
   
4. **Add custom assets** (optional):
   - Place `bgimage.jpg` in the `assets/` folder for custom background
   - Place `app_icon.ico` in the `assets/` folder for custom application icon

## 📖 Usage

### Running the Application

```bash
python KwizPro.py
```

### How to Use

1. **Enter Your Name**: Start by entering your name on the welcome screen
2. **Select Subjects**: Choose exactly 4 subjects from the 8 available categories
3. **Take the Quiz**: Answer 40 questions (10 from each selected subject) within the 10-minute time limit
4. **Navigate Questions**: Use Previous/Next buttons to move between questions
5. **Review Results**: View your score, percentage, and grade upon completion
6. **Review Answers**: Optionally review all questions with correct answers

### Subject Categories

- 🔢 **Mathematics**: Basic arithmetic and mathematical concepts
- 🔬 **Science**: Physics, chemistry, biology, and general science
- 📜 **History**: World history, important events, and historical figures  
- 🌍 **Geography**: World geography, countries, capitals, and natural features
- 📚 **Literature**: Famous authors, books, and literary works
- ⚽ **Sports**: Various sports, rules, and famous events
- 💻 **Computer Science**: Programming, technology, and computer fundamentals
- 🎨 **Art & Culture**: Art movements, artists, music, and cultural knowledge

## 🖼️ Screenshots

### Welcome Screen
![Welcome Screen](https://github.com/user-attachments/assets/1bffee13-a82f-4147-acdd-6f8e8ed368b2)
*Enter your name to begin the quiz*

### Subject Selection
![Subject Selection](https://github.com/user-attachments/assets/27bc7fab-08dc-4470-acb0-84486bcbf1e2)
*Choose 4 subjects from 8 available categories*

### Quiz Interface
![Quiz Interface](https://github.com/user-attachments/assets/4aa49aa7-ebb9-462c-a131-e71220a6c52b)
*Answer questions with a live timer*

### Results Screen
![Results Screen](https://github.com/user-attachments/assets/85fcc934-b3c9-4343-8c1b-56c37513e759)
*View your score and grade*

### Answer Review
![Answer Review](https://github.com/user-attachments/assets/8ec1c21f-c6f8-4e99-8f0e-2d8643130acc)
*Review all questions and correct answers*

## 🏗️ Project Structure

```
KwizPro/
│
├── KwizPro.py          # Main application file
├── assets/             # Optional assets folder
│   ├── bgimage.jpg     # Background image (optional)
│   └── app_icon.ico    # Application icon (optional)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## 🛠️ Technical Details

### Built With

- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework for the user interface
- **PIL/Pillow**: Image processing library (optional)
- **Random**: For question shuffling and selection
- **OS/Sys**: File path handling and system operations

### Key Components

- **Question Database**: 10 questions per subject (80 total questions)
- **Timer System**: Countdown timer with automatic submission
- **State Management**: User progress and answer tracking
- **Responsive UI**: Dynamic layout adaptation
- **Error Handling**: Graceful fallbacks for missing assets

## 📈 Grading System

- **90-100%**: Excellent! 🌟
- **80-89%**: Very Good! 👍  
- **70-79%**: Good! 👍
- **60-69%**: Fair 📖
- **Below 60%**: Needs Improvement 📚

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Make your changes**
4. **Add tests** if applicable
5. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
6. **Push to the branch**: `git push origin feature/AmazingFeature`
7. **Open a Pull Request**

### Areas for Contribution

- Adding more questions to existing subjects
- Creating new subject categories  
- Improving UI/UX design
- Adding sound effects or animations
- Implementing difficulty levels
- Creating question import/export functionality
- Adding multilingual support

## 🐛 Known Issues

- Background image requires PIL/Pillow library
- Application icon may not display without proper .ico file
- Timer continues running in answer review mode (by design)

## 🔮 Future Enhancements

- [ ] Database integration for persistent question storage
- [ ] User profile system with progress tracking
- [ ] Online leaderboards
- [ ] Question difficulty levels (Easy/Medium/Hard)
- [ ] Custom question creation interface
- [ ] Export results to PDF
- [ ] Sound effects and animations
- [ ] Mobile app version

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Abdultawwab Yusuf]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Author

**[Abdultawwab Yusuf]** - (https://github.com/KryptX10)

## 🙏 Acknowledgments

- Built with Python's Tkinter framework
- Icons and emojis for enhanced user experience
- Inspiration from modern quiz applications
- Community feedback and testing

---

### 📞 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/KryptX10/KwizPro/issues) section
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your system and the issue

### ⭐ Show Your Support

Give a ⭐️ if this project helped you learn or if you enjoyed using it!

---

*Happy Learning with KwizPro! 🎓*
