# Artifacts MMO Bot

Automation scripts for managing characters and gathering resources in Artifacts MMO.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your API key:**
   Create a `.env` file in the root directory and add your token:
   ```env
   TOKEN=your_secret_api_key_here
   ```

3. **Configure characters & settings:**
   Update `config.json` with your character names and preferred defaults:
   ```json
   {
       "characters": ["HeroOne", "WoodcutterBob"],
       "default_map": "forest"
   }
   ```

## Usage

Run individual task scripts from the root folder:
```bash
python gather.py
```
