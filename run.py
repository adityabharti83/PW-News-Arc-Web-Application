from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # This will render the index.html template from the templates folder
    return render_template('index.html',show_notification=True)

# Run the Flask application
if __name__ == '__main__':
    # Enabling debugger for development purposes
    app.run(debug=True, host='0.0.0.0', port=8080)

