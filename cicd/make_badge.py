from veracode import Application
import sys
import json

app = Application(sys.argv[1])
score = app.build.report.static_analysis.score

color = 'brightgreen'
if score < 95:
    color = 'red'

badge = {
      "schemaVersion": 1,
      "label": "Veracode Policy Score",
      "message": f"{score}",
      "color": f"{color}"
}

with open('cicd/veracode_score.json', 'w') as f:
    f.write(json.dumps(badge))

