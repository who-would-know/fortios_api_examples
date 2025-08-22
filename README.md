# FortiOS API get inline-casb application list

## Requirements

This script requires the following Python libraries:

- `requests`
- `sys`
- `urllib3` (usually installed as a dependency of `requests`)
- `json` (built-in, no installation needed)

- `FortiOS 7.2`
- `FortiOS API User` [Fortinet FortiGate REST API Administrator Guide](https://docs.fortinet.com/document/fortigate/7.4.8/administration-guide/399023/rest-api-administrator)

## Installation & Setup

### 0. Download the Script

Clone this repository or download the `fos_get_session_filter.py` file directly from this repo.

> If you're viewing this on GitHub, click the green **Code** button, then **Download ZIP**, or download just the script file.

### 1. To install the required external libraries, run:

```bash
pip install requests urllib3
```

### 2. Configure Script

Open the `fos_get_session_filter.py` file and update the following variables at the top:

```
### UPDATE FOR YOUR ENVIRONMENT ###
HOST_IP = "1.1.1.1"
API_TOKEN = "xxxxxx"
##################################
```

Can update filter or do not pass it as an argue to pull max sessions per API

```
    # Created a filter for destionation port 8922. Update as needed.
    filter = "destport=8922"

    # If filter variable not passed, it will just get sessions with ?count=9999
    result = get_session_filter(filter)

```

Make sure to save the file after editing.

### 3. Run

```bash
python fos_get_session_filter.py
```

### Output

JSON
