POCKETSMART AI DEMO LINK :https://drive.google.com/file/d/1A-rXXZ7K0Esze4X6eG9fsGuA5EAFwwHi/view?usp=sharing
# PocketSmart AI
Run in VS Code terminal:
    python -m venv venv
    venv\Scripts\activate          (Windows)   |   source venv/bin/activate   (Mac/Linux)
    pip install -r requirements.txt
    uvicorn main:app --reload
Open http://127.0.0.1:8000
Optional AI: put your key in .env as GEMINI_API_KEY=your_key (works without it in fallback mode).
Tests: pip install pytest httpx && python -m pytest tests -q
