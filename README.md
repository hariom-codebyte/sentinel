# Enterprise Threat Intelligence Aggregator

An enterprise-style Flask dashboard for reviewing Indicators of Compromise (IoCs). The application reads a local threat-intelligence feed, calculates operational metrics, and presents the results through a responsive SOC-inspired interface.

## Features

- REST endpoints for threat data and dashboard metrics.
- Severity distribution visualization powered by Chart.js.
- Search, sortable columns, pagination, CSV export, and click-to-copy IoC values.
- Responsive dark glassmorphism interface with keyboard search (`Ctrl/Cmd + K`) and reduced-motion support.
- Production-friendly Waitress configuration and environment-based port selection.

## Technology Stack

| Area | Technology |
| --- | --- |
| Backend | Python, Flask |
| Production server | Waitress |
| Frontend | HTML5, CSS3, vanilla JavaScript |
| Visualization | Chart.js (CDN) |
| Data source | Local JSON feed |

## Project Structure

```text
Threat-Intel-Project/
├── app.py                  # Flask routes and WSGI application
├── raw_threat_data.json    # Sample IoC feed
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment process command
├── core/
│   └── engine.py           # Feed loading and metric calculation
├── templates/
│   └── index.html          # Dashboard structure
└── static/
    ├── css/style.css       # Responsive visual system
    └── js/app.js           # Data loading and UI behavior
```

## Run Locally

### Prerequisites

- Python 3.10 or newer
- pip

### Installation

**Windows quick start:** Double-click `START_DASHBOARD.bat`. It creates a Windows virtual environment, installs dependencies, launches Flask, and opens the dashboard in your browser.

Do not click VS Code's **Go Live** button. Live Server is only a static file server, which is why it displays a folder listing instead of this Flask dashboard.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

If PowerShell prevents virtual-environment activation, run this once for the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## API Reference

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | GET | Renders the dashboard |
| `/api/threat_data` | GET | Returns the complete IoC feed |
| `/api/metrics` | GET | Returns total, critical, high, and medium counts |

## Deployment

The committed `Procfile` runs the application with Waitress:

```text
web: waitress-serve --host=0.0.0.0 --port=$PORT app:app
```

Most PaaS hosts set `PORT` automatically. For a direct server deployment, set `PORT` to the desired listening port and run the same Waitress command after installing dependencies. Flask debug mode is off by default; only set `FLASK_DEBUG=true` during local development.

## Data Format

The input feed is a JSON object containing a timestamp, source list, and an `iocs` array. Each indicator includes `type`, `value`, `severity`, `threat_actor`, and `description`.

```json
{
  "type": "IPv4",
  "value": "192.168.100.45",
  "severity": "High",
  "threat_actor": "APT29",
  "description": "Known command and control server."
}
```

## Notes

This project uses mock data for demonstration purposes. Before connecting real threat-intelligence providers, secure API credentials with environment variables, validate incoming data, and add authentication and authorization around production endpoints.
