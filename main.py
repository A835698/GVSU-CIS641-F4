from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_code', methods=['POST'])
def run_code():
    # Get data from the frontend
    file_path = '/Users/avinash/Downloads/Untitled form (Responses).xlsx'
    df = pd.read_excel(file_path)
    df = df.sort_values(by='Web Designing', ascending=False)

    m = 5
    team_assignments = [[] for _ in range(m)]
    current_team = 0

    for index, row in df.iterrows():
        team_assignments[current_team].append(row['G-Number'])
        current_team = (current_team + 1) % m

    team_results = []
    for i, team in enumerate(team_assignments):
        team_results.append(f"Team {i + 1}: {', '.join(team)}")

    return jsonify(team_results)


if __name__ == '__main__':
    app.run(debug=True)
