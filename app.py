# project-folder/app.py
from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)

# Load CSV data
csv_file = 'symptoms.csv'
df = pd.read_csv(csv_file)
columns = df.columns.tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_columns')
def get_columns():
    return json.dumps(columns)

@app.route('/get_data', methods=['POST'])
def get_data():
    selected_columns = request.form.getlist('columns[]')
    selected_data = df[selected_columns].to_html(index=False)
    return selected_data

if __name__ == '__main__':
    app.run(debug=True)
