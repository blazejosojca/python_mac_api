# python_mac_api

The python based CLI programme allows to access the website API and receive the data about company.
The required python additional packages should be installed using requirements file.

To use the programme firstly create account at:
https://macaddress.io/

Next define the OS enviromental variable called API_KEY.

`export API_KEY=<your_api_key>`.

The API_KEY should be the same as the API_KEY from the https://macaddres.io.

The programme allows user to insert two variables:
- mac_address (-a, --address)
- vendor_details (-v, --vendor_details)

Example input:
`python3 cli_parser.py -a 44:38:39:ff:ef:57 -v companyName`

Example output:
`The value of companyName for MAC address: 44:38:39:ff:ef:57 is: Cumulus Networks, Inc`


At the moment the programme allows only to receive data using JSON.