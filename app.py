from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        print(f"New message from {name} ({email}): {message}")

        success = "Thank you for your message! I will get back to you soon."

    return render_template('contact.html', active_page='contact', success=success)

if __name__ == '__main__':
    app.run(debug=True)
