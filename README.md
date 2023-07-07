# ISE Session Information Retriever

This script (`simple_ise.py`) retrieves session information for a device with a given MAC address from Cisco Identity Services Engine (ISE) using the ISE REST API.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `xml.etree.ElementTree`, `urllib3`, `getpass`

## Setup

1. Clone or download the repository.

2. Install the required Python packages:
    ```bash
    pip install 

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing `simple_ise.py`.

3. Run the script and provide the MAC address as a command-line argument:
    ```bash
    python simple_ise.py <MAC_ADDRESS>


Replace `<MAC_ADDRESS>` with the MAC address of the device you want to retrieve session information for.

4. Enter your ISE username and password when prompted.

5. The script will make an API request to the ISE server and retrieve the session information for the provided MAC address.

6. The script will display the following session details if available:
- MAC address
- IP address of the device
- Identity group
- Switch IP address
- Switchport

## Important Notes

- Make sure to update the `ise_base_url` variable in the code with the correct IP address or hostname of your ISE server.

- Ensure that your environment meets the prerequisites before running the script.

- The script uses the `requests` library to make API requests. It disables SSL verification due to the insecure request warning. Please exercise caution when running the script in production environments.

- If any errors occur during the execution of the script, relevant error messages will be displayed.

