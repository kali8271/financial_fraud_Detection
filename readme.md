# Financial Fraud Detection System

A Django-based web application for detecting and reporting fraudulent financial transactions using machine learning.

## Features

- Real-time transaction analysis
- Fraud detection using machine learning models
- User-friendly interface for transaction submission
- Fraud reporting system
- Feedback mechanism for improving detection accuracy
- RESTful API for integration
- Dashboard for analytics and monitoring

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd financial_fraud_detection
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application at `http://localhost:8000`

## Project Structure

```
financial_fraud_detection/
├── fraud_app/              # Main application
│   ├── templates/         # HTML templates
│   ├── static/           # Static files (CSS, JS)
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   └── forms.py          # Form definitions
├── fraud_detection_django/  # Project settings
├── models/               # ML models
├── data/                # Dataset storage
├── notebooks/           # Jupyter notebooks
└── src/                # Source code
```

## API Endpoints

- `GET /api/transactions/` - List all transactions
- `GET /api/transactions/<id>/` - Get transaction details
- `POST /api/risk-score/` - Calculate risk score
- `POST /report/` - Submit fraud report
- `POST /feedback/` - Submit feedback

## Development

1. Run tests:
```bash
pytest
```

2. Check code style:
```bash
flake8
black .
```

## Deployment

1. Set DEBUG=False in settings.py
2. Configure production database
3. Set up static files:
```bash
python manage.py collectstatic
```
4. Use gunicorn for production:
```bash
gunicorn fraud_detection_django.wsgi:application
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the maintainers.


