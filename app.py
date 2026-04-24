from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask App
app = Flask(__name__)

# -------------------------------
# Home Route (Landing Page)
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -------------------------------
# Prediction Route
# -------------------------------
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    
    # If user just opens the page
    if request.method == 'GET':
        return render_template('home.html')
    
    try:
        # Collect data from form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Convert to DataFrame
        pred_df = data.get_data_as_dataframe()

        # Prediction
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        # Return result to UI (rounded)
        return render_template('home.html', result=round(result[0], 2))

    except Exception as e:
        # Handle errors gracefully
        return render_template('home.html', result=f"Error: {str(e)}")


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run()