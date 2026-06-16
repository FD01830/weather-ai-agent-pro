
import os
from dotenv import load_dotenv
load_dotenv()
XAI_API_KEY=os.getenv("XAI_API_KEY")
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")
XAI_BASE_URL="https://api.x.ai/v1"
MODEL_NAME="grok-4-latest"
