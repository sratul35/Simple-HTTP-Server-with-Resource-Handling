# Simple HTTP Server with Resource Handling

This project is a simple implementation of an HTTP server in Python that can handle GET and POST requests, serving static resources and responding to user input. It provides a basic foundation for understanding how web servers work and how different HTTP methods can be processed.

## Features

- Listens for incoming client connections on a specified host and port.
- Handles GET requests by serving static HTML, image, video, PDF, and icon files from the server's local directory.
- Processes POST requests, extracting and displaying the user parameter value.
- Handles 404 Not Found errors gracefully.
- Utilizes multithreading to handle multiple client connections simultaneously.

## How to Use

1. Clone this repository to your local machine.

```bash
git clone REPO_URL
cd simple-http-server-with-resource-handling
```

1. Modify the `urls.py` file to define the mapping between requested URLs and corresponding resource files.

2. Run the `server.py` script to start the HTTP server. You can specify a custom port number by adding the --port option followed by your desired port number.

python server.py --port PORT_NUMBER

replace PORT_NUMBER with your desired port number

3. Open your web browser and navigate to http://localhost:PORT_NUMBER/ to view the server's home page.

4. Navigate to http://localhost:PORT_NUMBER/PATH_TO_RESOURCE to view the specified resource.

replace PATH_TO_RESOURCE with the path to the desired resource file


