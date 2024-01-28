from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

load_dotenv() 

openai_api_key = os.environ.get('OPENAI_API_KEY')
# client = OpenAI(api_key=openai_api_key)

#from teacher.py import (fxn name)


# Create a Flask app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/testtest')
def hello_world():
    client = OpenAI(api_key=openai_api_key)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    s = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            s += chunk.choices[0].delta.content
    return s



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('message-input')
        print(data)

        # response = student.some_function(user_input)  # Replace with actual function call

        # return jsonify({'response': response})
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    # Process the search_query
    return render_template('search_results.html', query=search_query)

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
