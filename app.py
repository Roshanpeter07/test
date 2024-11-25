from flask import Flask, render_template, request

app = Flask(__name__)

# Route to serve the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/process', methods=['POST'])
def process_input():
    # Get input from the form
    user_input = request.form.get('userInput')
    return f"You entered: {user_input}"  # Display the result

if __name__ == '__main__':
    # Set the port for the Flask app
    app.run(host='0.0.0.0', port=5000)
