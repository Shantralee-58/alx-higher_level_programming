# 0x11-python-network_1

This repository contains Python scripts that demonstrate basic network programming concepts using the `urllib` and `requests` libraries. Each script performs a specific task related to HTTP requests, status codes, headers, and API interactions.

## Scripts

1. **0-hbtn_status.py**
   - Fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status).
   - Uses the `urllib` package.

2. **1-hbtn_header.py**
   - Takes a URL, sends a request, and displays the value of the `X-Request-Id` variable in the header.
   - Uses the `urllib` package.

3. **2-post_email.py**
   - Takes a URL and an email, sends a POST request, and displays the body of the response.
   - Uses the `urllib` package.

4. **3-error_code.py**
   - Takes a URL, sends a request, and displays the body of the response.
   - Handles `urllib.error.HTTPError` exceptions.

5. **4-hbtn_status.py**
   - Fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status).
   - Uses the `requests` package.

6. **5-hbtn_header.py**
   - Takes a URL, sends a request, and displays the value of the `X-Request-Id` variable in the response header.
   - Uses the `requests` package.

7. **6-post_email.py**
   - Takes a URL and an email, sends a POST request, and displays the body of the response.
   - Uses the `requests` package.

8. **7-error_code.py**
   - Takes a URL, sends a request, and displays the body of the response.
   - Prints an error code if the HTTP status code is greater than or equal to 400.
   - Uses the `requests` package.

9. **8-json_api.py**
   - Takes a letter, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
   - Displays the id and name if the response is properly JSON formatted and not empty.

10. **10-my_github.py**
    - Takes GitHub credentials (username and password) and uses the GitHub API to display the user id.
    - Uses Basic Authentication with a personal access token.

11. **100-github_commits.py**
    - Lists 10 commits (from most recent to oldest) of a specified repository by a specified user.
    - Uses the GitHub API.

## Requirements
- Python 3.8.5
- pycodestyle 2.8.* (for code style checking)

## Usage
1. Clone the repository.
2. Navigate to the specific task directory.
3. Run the Python script associated with the task.

Feel free to explore and learn from the provided scripts!
