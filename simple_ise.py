import requests
import xml.etree.ElementTree as ET
import urllib3
import getpass
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ise_base_url = "https://<IP or hostname>"
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")


def get_session_info(mac_address):
    # Disable SSL verification and specify headers
    session = requests.Session()
    session.verify = False
    session.headers = {"Accept": "application/xml"}

    try:
        # Make the API request
        response = session.get(f"{ise_base_url}/admin/API/mnt/Session/MACAddress/{mac_address}", auth=(username, password))
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        # Parse the XML response
        root = ET.fromstring(response.content)

        # Find and extract the value of the device_ip_address element
        device_ip_address = root.find(".//device_ip_address").text
        identity_group = root.find(".//identity_group").text
        nas_ip_address = root.find(".//nas_ip_address").text
        nas_port_id = root.find(".//nas_port_id").text

        return {
            "mac_address": mac_address,
            "device_ip_address": device_ip_address,
            "identity_group": identity_group,
            "nas_ip_address": nas_ip_address,
            "nas_port_id": nas_port_id
        }

    except requests.HTTPError as e:
        print(f"HTTP Error: {str(e)}")

    except (requests.RequestException, ET.ParseError) as e:
        if str(e) == "no element found: line 1, column 0":
            print(f"Error: MAC address not found")
        else:
            print(f"Error: {str(e)}")

    except AttributeError:
        print("Error: Failed to extract device IP address.")

    finally:
        session.close()  # Close the session to release resources


# Retrieve the MAC address from the command line argument
if len(sys.argv) > 1:
    mac_address = sys.argv[1]
else:
    print("Error: Please provide the MAC address as a command-line argument. Example: python3 simple_ise.py <MAC>")
    sys.exit(1)

session_info = get_session_info(mac_address)
if session_info:
    print(f"\nMAC: {session_info['mac_address']}\nIP address: {session_info['device_ip_address']}\nIdentity Group: {session_info['identity_group']}\nSwitch IP: {session_info['nas_ip_address']}\nSwitchport: {session_info['nas_port_id']}\n")

