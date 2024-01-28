from flask import Flask, render_template, request, jsonify, make_response
from openai import OpenAI
# from dotenv import load_dotenv
import scripts.student as student

# load_dotenv() 

assistant_id = 'asst_s1VW5o5OyeMfMF7qu9PK9SOt'

# Create a Flask app instance
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    global assistant_id
    if request.method == 'POST':
        question = request.form.get('message-input')

        student.run_user_bot(assistant_id)
        messages = student.ask_tutor(question)

        response = make_response (
            jsonify(
                {"messages": messages}
            )
        )

        return response
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
