# 🚀 Harsh Tiwari - Data Scientist Portfolio

A modern, animated, single-page portfolio website showcasing data science skills and projects. Built with Flask, Tailwind CSS, and JavaScript featuring beautiful black and white animations.

![Portfolio Preview](static/images/2.jpg)

## ✨ Features

### 🎨 Design & Animations
- **Single-page design** with smooth scrolling navigation
- **Black and white theme** with elegant animations
- **Responsive design** that works on all devices
- **Modern glassmorphism** effects and subtle gradients
- **Typing animation** for dynamic text display
- **Floating elements** with organic movement
- **Scroll-triggered animations** for engaging user experience

### 🔧 Technical Features
- **Flask backend** for contact form handling
- **Tailwind CSS** for modern, utility-first styling
- **Vanilla JavaScript** for interactive features
- **Mobile-responsive** navigation with hamburger menu
- **Smooth scrolling** between sections
- **Progress indicators** for page scroll
- **Back-to-top button** for easy navigation
- **Form validation** with success/error notifications

### 📱 Sections
- **Hero Section**: Dynamic introduction with typing animation
- **About Me**: Personal information with animated statistics
- **Skills**: Interactive skill bars with progress animations
- **Projects**: Featured projects with hover effects
- **Contact**: Working contact form with validation

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom animations and transitions
- **Tailwind CSS** - Utility-first CSS framework
- **JavaScript (ES6+)** - Interactive features and animations
- **Font Awesome** - Icons and visual elements
- **Google Fonts** - Inter typography

### Backend
- **Flask** - Python web framework
- **Python 3.x** - Backend logic
- **Jinja2** - Template engine

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
portfolio/
├── app.py                 # Flask application main file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── Templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles and animations
│   ├── js/
│   │   └── script.js     # Interactive JavaScript features
│   └── images/
│       └── 2.jpg         # Profile image
└── __pycache__/          # Python cache files
```

## 🎯 Key Features Breakdown

### Animation System
- **CSS Keyframes**: Smooth, hardware-accelerated animations
- **Intersection Observer**: Scroll-triggered animations for performance
- **Transform3D**: GPU-accelerated transformations
- **Staggered animations**: Sequential element reveals

### JavaScript Features
- **Smooth Scrolling**: Native `scrollTo()` with easing
- **Typing Animation**: Dynamic text cycling with realistic typing
- **Mobile Menu**: Touch-friendly navigation
- **Form Handling**: Async form submission with validation
- **Scroll Progress**: Visual progress indicator
- **Lazy Loading**: Performance-optimized content loading

### CSS Architecture
- **Modular Styles**: Organized CSS with clear naming conventions
- **Custom Properties**: CSS variables for consistent theming
- **Responsive Design**: Mobile-first approach with breakpoints
- **Performance**: Optimized animations using `transform` and `opacity`

## 🎨 Customization

### Colors & Theme
The portfolio uses a black and white theme with customizable accents:

```css
:root {
  --primary-bg: #000;
  --secondary-bg: #111;
  --text-primary: #fff;
  --text-secondary: #ccc;
  --accent: #fff;
}
```

### Content Updates
1. **Personal Information**: Update `Templates/index.html`
2. **Skills**: Modify skill percentages in the skills section
3. **Projects**: Add/edit project cards with your work
4. **Contact Info**: Update contact details and social links

### Adding New Sections
1. Add HTML section to `Templates/index.html`
2. Add corresponding styles to `static/css/style.css`
3. Update navigation in both desktop and mobile menus
4. Add scroll animations in `static/js/script.js`

## 📧 Contact Form

The contact form includes:
- **Client-side validation** for immediate feedback
- **Server-side processing** via Flask
- **Success/error notifications** for user feedback
- **Form reset** after successful submission

To add email functionality:
1. Install email library: `pip install flask-mail`
2. Configure SMTP settings in `app.py`
3. Update the contact form handler

## 🔧 Development

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run in development mode
python app.py

# The server runs on http://localhost:5000
```

### Production Deployment
For production deployment, consider:
- Using a WSGI server like Gunicorn
- Setting up environment variables for sensitive data
- Configuring a reverse proxy (nginx)
- Adding SSL certificate for HTTPS

## 📝 TODO / Future Enhancements

- [ ] Add blog section with markdown support
- [ ] Implement dark/light theme toggle
- [ ] Add more project filtering options
- [ ] Include testimonials section
- [ ] Add resume download functionality
- [ ] Implement contact form email integration
- [ ] Add Google Analytics integration
- [ ] Create admin panel for easy content updates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

**Harsh Tiwari** - Data Scientist
- Email: harsh.tiwari@example.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- GitHub: [Your GitHub](https://github.com/yourusername)

---

⭐ **Star this repository if you found it helpful!**

Built with ❤️ using Flask, Tailwind CSS, and JavaScript