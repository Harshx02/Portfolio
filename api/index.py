# # from flask import Flask, render_template
# # app = Flask(__name__)



# from flask import Flask, render_template

# app = Flask(__name__, template_folder="../Templates", static_folder="../static")

# @app.route('/')
# def home():
#     return render_template("index.html")

# # Required by Vercel to treat this as a serverless function
# handler = app




# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# @app.route('/projects')
# def projects():
#     return render_template('projects.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, jsonify, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/api/contact', methods=['POST'])
# def handle_contact():
#     try:
#         # Get form data
#         name = request.form.get('name')
#         email = request.form.get('email')
#         subject = request.form.get('subject')
#         message = request.form.get('message')
        
#         # Basic validation
#         if not all([name, email, subject, message]):
#             return jsonify({"status": "error", "message": "All fields are required!"}), 400
        
#         # Here you would typically save to database or send email
#         # For now, we'll just log the data and return success
#         print(f"Contact form submission:")
#         print(f"Name: {name}")
#         print(f"Email: {email}")
#         print(f"Subject: {subject}")
#         print(f"Message: {message}")
        
#         return jsonify({"status": "success", "message": "Message sent successfully!"})
        
#     except Exception as e:
#         print(f"Error handling contact form: {e}")
#         return jsonify({"status": "error", "message": "Internal server error"}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)







from flask import Flask, render_template, jsonify, request

# Setup Flask with correct paths for Vercel
app = Flask(__name__, template_folder="../Templates", static_folder="../static")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Other routes
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# API route for contact form
@app.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not all([name, email, subject, message]):
            return jsonify({"status": "error", "message": "All fields are required!"}), 400

        print(f"[Contact] Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")
        return jsonify({"status": "success", "message": "Message sent successfully!"})
    
    except Exception as e:
        print(f"Error handling contact form: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Required by Vercel to route requests
handler = app
