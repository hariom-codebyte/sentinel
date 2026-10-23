import os
from pathlib import Path

from flask import Flask, jsonify, render_template
from core.engine import ThreatIntelligenceEngine

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
threat_engine = ThreatIntelligenceEngine(BASE_DIR / 'raw_threat_data.json')

@app.route('/')
def dashboard():
    """Serves the main HTML template."""
    return render_template('index.html')

@app.route('/api/threat_data')
def api_threat_data():
    """Returns the full list of IoCs."""
    data = threat_engine.fetch_raw_data()
    return jsonify(data), data.get("status", 200)

@app.route('/api/metrics')
def api_metrics():
    """Returns calculated statistics for the dashboard."""
    metrics = threat_engine.get_dashboard_metrics()
    return jsonify(metrics), metrics.get("status", 200)

if __name__ == '__main__':
    print("[*] Enterprise Threat Intelligence Aggregator starting...")
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_DEBUG', '').lower() == 'true',
    )
