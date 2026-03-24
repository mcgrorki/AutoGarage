# AutoGarage API

A simple FastAPI application deployed on Vercel.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn api.index:app --reload
```

3. Visit http://localhost:8000/docs for interactive API documentation

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /garage/{item_id}` - Get garage item by ID
- `POST /garage` - Create a new garage item

## Deployment to Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

Or for production deployment:
```bash
vercel --prod
```

## Environment Variables

Add any environment variables in Vercel dashboard or using:
```bash
vercel env add VARIABLE_NAME
```

## Project Structure

```
AutoGarage/
├── api/
│   └── index.py          # Main API application
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md           # This file
```