from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Correct answers for each house in the Zebra puzzle
correct_answers = {
    'house1': {'color': 'Yellow', 'nationality': 'Norwegian', 'drink': 'Water', 'pet': 'Fox', 'cigarette': 'Kools'},
    'house2': {'color': 'Blue', 'nationality': 'Ukrainian', 'drink': 'Tea', 'pet': 'Horse', 'cigarette': 'Chesterfields'},
    'house3': {'color': 'Red', 'nationality': 'Englishman', 'drink': 'Milk', 'pet': 'Snails', 'cigarette': 'Old Gold'},
    'house4': {'color': 'Green', 'nationality': 'Japanese', 'drink': 'Coffee', 'pet': 'Zebra', 'cigarette': 'Parliaments'},
    'house5': {'color': 'Ivory', 'nationality': 'Spaniard', 'drink': 'Orange Juice', 'pet': 'Dog', 'cigarette': 'Lucky Strike'}
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user's selections
        answers = request.form.to_dict()

        # Validate answers and create feedback (correct or incorrect)
        result = {}
        for house, correct in correct_answers.items():
            result[house] = {attr: (answers.get(f'{house}_{attr}') == correct[attr]) for attr in correct}

        return jsonify(result)

    return render_template('zebra.html')

if __name__ == '__main__':
    app.run(debug=True)
