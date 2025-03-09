# dylan

dylan is a web application that allows users to search for sku codes from product names in relation to Four Fashion Australia. The application leverages Flask for the web framework, BeautifulSoup for web scraping, and Google GenAI for content generation.

I made this to help automate tasks at my part time job at Four Fashion Australia.

## Features

- Search for products by name and brand.
- Extract SKU information from product pages.
- User-friendly interface with responsive design.

## Technologies Used

- Flask: A lightweight WSGI web application framework.
- BeautifulSoup: A library for parsing HTML and XML documents.
- Requests: A simple HTTP library for Python.
- Google GenAI: For generating content based on the extracted data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dylan.git
   cd dylan
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment variables:
   - Create a `.env` file in the root directory and add your API key:
     ```
     API_KEY=your_google_api_key
     ```

## Running the Application

To run the application, use the following command:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## Contributing

This project is not open for contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
