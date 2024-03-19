from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Get the directory of the current script
current_dir = os.path.dirname(r'C:\Users\babin\Downloads\New folder')

# Load the trained classification model
model_path = os.path.join(current_dir, 'fish_species_classification_model.pkl')
model = joblib.load(model_path)

# Dictionary mapping numeric predictions to species labels
species_mapping = {
    0: 'Bream',
    1: 'Roach',
    2: 'Whitefish',
    3: 'Parkki',
    4: 'Perch',
    5: 'Pike',
    6: 'Smelt'
}

# Route to serve the HTML page
@app.route('/')
def index():
    # Render the HTML template
    template_path = os.path.join(current_dir, 'templates', 'fish.html')
    return render_template('fish.html')

# Route to handle prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        length1 = float(request.form['length1'])
        length2 = float(request.form['length2'])
        length3 = float(request.form['length3'])
        height = float(request.form['height'])
        width = float(request.form['width'])
        weight = float(request.form['weight'])

        # Perform prediction using the model
        input_data = [[length1, length2, length3, height, width, weight]]
        prediction = model.predict(input_data)[0]
        predicted_species = species_mapping[prediction]

        # Return the predicted species
        return jsonify({'prediction': predicted_species})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
