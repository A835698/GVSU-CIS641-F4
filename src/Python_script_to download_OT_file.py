from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import random
from io import BytesIO

# change name to app.py


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_teams', methods=['POST'])
def create_teams():
    # Get data from the frontend
    file_path = '/Users/avinash/Downloads/Untitled form (Responses).xlsx'
    df = pd.read_excel(file_path)

    df = df.sort_values(by='Web Designing', ascending=False)

    m = 5  # Number of teams
    team_assignments = [[] for _ in range(m)]
    current_team = 0

    for _, row in df.iterrows():
        team_assignments[current_team].append(row['G-Number'])
        current_team = (current_team + 1) % m

    team_results = []
    for i, team in enumerate(team_assignments):
        team_lead = team[0] if team else ''
        team_members = random.sample(team[1:], min(3, len(team) - 1)) if team else []
        team_results.append({'Team Lead': team_lead, 'Team Members': team_members})

    # Create CSV content
    csv_content = "Team Lead,Team Members\n"
    for result in team_results:
        csv_content += f"{result['Team Lead']},{', '.join(result['Team Members'])}\n"

    # Create BytesIO buffer
    buffer = BytesIO()
    buffer.write(csv_content.encode())
    buffer.seek(0)

    return send_file(buffer, download_name='team_results.csv', as_attachment=True, mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
