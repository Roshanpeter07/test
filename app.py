from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML file

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
