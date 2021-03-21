import os
import requests
import argparse

"""
Package allows to receive data from API using mac address passing through to the CLI.
"""

def get_vendor_details_data(vendor, vendor_detail=None):
    """
    Function that allows to get the data from api using MAC address.
    The API key is a OS environment variable.
    :param mac_address: type(str) - the mac address.
    :param vendor_detail: type (str) - key of json response data which value should be, by default is None,
                            then the message is a whole returned data.
    :return:
        message: type (str)
    """
    base_url = 'https://api.macaddress.io'
    api_key = os.environ.get('API_KEY')
    api_url = f'{base_url}/v1?apiKey={api_key}&output=json&search={vendor}'
    get_request = requests.request('get', url=api_url)
    if vendor_detail is None:
        message = get_request.json()
    else:
        response = get_request.json()['vendorDetails'][vendor_detail]
        message = f"The value of key {vendor_detail} for MAC address: {vendor} is: {response}"
    print(message)

def mac_address_parser():
    """
    Function that allows user to define details about API request using CLI.
    :return: type(str) - the output of the API request.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", help='The MAC address used to search information.')
    parser.add_argument("-v", "--vendor_details", help='The more specific details for returned data.')
    args = parser.parse_args()
    if args.vendor_details:
        result = get_vendor_details_data(vendor=args.address, vendor_detail=args.vendor_details)
        return result
    if args.address:
        result = get_vendor_details_data(vendor=args.address)
        return result

if __name__ == "__main__":
    mac_address_parser()
