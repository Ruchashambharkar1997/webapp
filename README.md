# webapp
# Flask Application README

This Flask application demonstrates basic routing and error handling.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the following command:

```bash
python app.py
The application will start running on http://127.0.0.1:5000/.

Routes
/
Description: Homepage route
Method: GET
Response: "Hello, World!"
/hello
Description: Route for saying hello
Method: GET
Response: "Hello, World!"
/invalid-route
Description: Route for testing invalid route handling
Method: GET
Response: JSON response with error message "Route not found" and status code 404
/post-method
Description: Route for testing POST method not allowed handling
Method: GET
Response: JSON response with message "GET method allowed"

Error Handling
404 Not Found: Returned when accessing an invalid route
405 Method Not Allowed: Returned when trying to access a route with an unsupported HTTP method
