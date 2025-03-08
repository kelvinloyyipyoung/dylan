from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import json
from dotenv import load_dotenv
import os
from google import genai
from googlesearch import search
import re

# Load environment variables and set up Google AI client
load_dotenv()
api_key = os.environ.get("API_KEY")
client = genai.Client(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_product_name():
    product_name = request.form['product_name']
    selected_brand = request.form['selected_brand']
    
    # Map brand selections to their domains
    brand_domains = {
        'madison': 'www.madisonthelabel.com',
        'lostinlunar': 'www.lostinlunar.com',
        'bydyln': 'bydyln.com'
    }
    
    domain = brand_domains[selected_brand]
    search_query = f"site:{domain} {product_name}"
    url = ""
    
    response = search(search_query, num_results=3, unique=True, advanced=True)
    pattern = re.compile(rf"https://{re.escape(domain)}/products/[^/?]+")

    # Filter the matching URL
    for result in response:
        if pattern.match(result.url):
            url = result.url

    url = url.split('?')[0]

    try:
        # Get product page and extract SKU
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.find("script", {"type": "application/json", "data-product-json": True})
        script_tag = json.loads(script_tag.get_text())

        prompt = "extract the sku from the following json. only output the sku, nothing else:" 
        prompt = prompt + str(script_tag)

        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt,
        )
        
        sku = response.text
        return render_template('index.html', result=sku, error=None)
    
    except Exception as e:
        return render_template('index.html', result=None, error=f"This product is no longer online. {url}")

if __name__ == '__main__':
    app.run(debug=True) 