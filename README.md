# XssPrnv

XssPrnv is a Flask-based web application designed for automated Cross-Site Scripting (XSS) vulnerability testing. Users can input a target domain and query parameter to generate a list of URLs with XSS payloads to test for vulnerabilities.

## Features

- **Input Field for Domain**: Users enter the target URL they want to test.
- **Input Field for Parameter Name**: Allows users to specify a query parameter to inject payloads.
- **50+ Predefined XSS Payloads**: A comprehensive list of XSS payloads, covering different encoding formats and injection techniques.
- **Generated URLs**: Each generated URL is clickable, making it easy to test potential XSS vulnerabilities in a browser.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/xss-testing-tool.git
   cd xss-testing-tool
   ```
2. **Install Dependencies**: Install Flask via pip:
   ```bash
   pip install flask
   ```
3. **Run the Application**:
   ```bash
   python app.py
   ```
4. **Access the Tool**: Open your web browser and navigate to `http://127.0.0.1:5000` to use XssPrnv.

## Usage

1. **Enter the Domain**: Type in the domain you want to test (e.g., `https://example.com`).
2. **Enter the Parameter Name**: Specify the query parameter to which the payloads will be appended (e.g., `search`, `q`, `query`).
3. **Generate URLs**: Click "Generate XSS Test URLs" to create a list of XSS testing URLs.
4. **Test the Generated URLs**: Each URL in the list contains an XSS payload. Click on each link to test if the domain is vulnerable. If successful, the payload may trigger a JavaScript alert or other indication of XSS.

## Example

If you input:

- **Domain**: `https://example.com`
- **Parameter Name**: `query`

The generated list might look like:

```
https://example.com?query=%3Cscript%3Ealert(1)%3C%2Fscript%3E
https://example.com?query=%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E
https://example.com?query=%22%3E%3Cscript%3Ealert(1)%3C%2Fscript%3E
https://example.com?query=%3Ciframe%20src%3D%22javascript%3Aalert(1)%22%3E
...
```

By clicking each link, you can observe the website's response. If an alert or JavaScript execution occurs, the domain may be vulnerable to XSS for that parameter.
