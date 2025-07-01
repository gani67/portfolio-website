from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template with embedded CSS and form
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef2f3;
            padding: 50px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        input, textarea {
            width: 100%%;
            padding: 10px;
            margin-top: 10px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        h1, h2 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, I'm [Your Name]</h1>
        <p>Welcome to my personal portfolio website built using Flask. I'm passionate about web development and Python!</p>

        <h2>Contact Me</h2>
        <form action="/contact" method="post">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit">Send Message</button>
        </form>
    </div>
</body>
</html>
'''

# Thank you page template
thank_you = '''
<!DOCTYPE html>
<html>
<head><title>Thank You</title></head>
<body style="font-family: Arial; text-align: center; padding: 50px;">
    <h2>Thank you, {{ name }}!</h2>
    <p>Your message has been received.</p>
    <a href="/">Back to Home</a>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    return render_template_string(thank_you, name=name)

if __name__ == '__main__':
    app.run(debug=True)

