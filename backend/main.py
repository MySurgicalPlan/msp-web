from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My Surgical Plan API")

# Essential for React (localhost:5173) to talk to FastAPI (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "online", "message": "My Surgical Plan API is active"}


@app.get("/health")
async def health_check():
    # This is vital for AWS Load Balancers later
    return {"status": "healthy", "service": "segmentation-engine"}
