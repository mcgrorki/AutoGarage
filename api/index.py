from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AutoGarage API", description="A simple API for AutoGarage")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to AutoGarage API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

@app.get("/garage/{item_id}")
async def get_garage_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q, "message": f"Garage item {item_id}"}

@app.post("/garage")
async def create_garage_item(item: dict):
    return {"message": "Item created", "item": item}

# Vercel requires this for serverless functions
# This will be the entry point when deployed
def handler(request):
    # Vercel will handle the ASGI app automatically with FastAPI
    return app