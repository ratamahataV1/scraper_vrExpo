Automated Login + Scraping Script
- Install python3-full
```
apt install python3-full
```
- Create a project folder
```
mkdir ~/scraper
cd ~/scraper
```
- Create a virtual environment
```
python3 -m venv venv
```
- Activate the virtual environment
```
source venv/bin/activate
```
- Install Dependencies inside the virtual environment
```
pip install requests beautifulsoup4 pandas openpyxl setuptools py-distutils 
pip install playwright
playwright install
pip install playwright-stealth
```
- Create the scraper script
- Add login credentials
```
nano scrape.py
```
- Run the scraper
```
python scrape.py
```
- When you're done
```
deactivate
```
- Re-run
```
source venv/bin/activate
python scrape.py
```

![Peek 2025-12-04 15-31](https://github.com/user-attachments/assets/58e3f89b-827e-427d-84f4-1a83c1e180d0)


<img width="789" height="209" alt="Screenshot_2025-12-04_15-30-20" src="https://github.com/user-attachments/assets/e27aa91e-0bac-4918-aa01-7a9e77fc7f99" />

