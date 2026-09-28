"""Shared settings: base folder, Jinja templates, money filter, dropdown options."""
import logging
from pathlib import Path
from fastapi.templating import Jinja2Templates
from models.schemas import OPTIONS

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "static" / "uploads"
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
templates.env.filters["money"] = lambda v: f"₹{float(v):,.0f}"
templates.env.globals["OPTIONS"] = OPTIONS
