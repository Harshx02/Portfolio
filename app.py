from flask import Flask, render_template, jsonify, request

# Set correct paths for Flask to locate templates and static folders
app = Flask(__name__, template_folder="templates", static_folder="static")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Other static routes
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# API route to handle contact form submission
@app.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Validate input
        if not all([name, email, subject, message]):
            return jsonify({"status": "error", "message": "All fields are required!"}), 400

        # You can add database/email logic here
        print(f"[Contact] Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")
        return jsonify({"status": "success", "message": "Message sent successfully!"})

    except Exception as e:
        print(f"Error handling contact form: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Optional: only runs when testing locally
if __name__ == '__main__':
    app.run(debug=True)
