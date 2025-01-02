import xml.etree.ElementTree as ET
from collections import defaultdict
from Holdings import Holdings

class Analyze13F:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.data = [Holdings]
        self._parse_xml()

    def _parse_xml(self):
        # Parse the XML file
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        # Extract the namespace from the root element (if any)
        namespace = {'ns': 'http://www.sec.gov/edgar/document/thirteenf/informationtable'}

       
        # Find all 'infoTable' elements in the XML
        info_tables = root.findall("ns:infoTable",namespace)

        # A dictionary to store the sum of shares grouped by NameOfIssuer and TitleOfClass
        grouped_data = defaultdict(lambda: {'Shares': 0,'Value_Of_Share':0})


        # Extract relevant fields from each infoTable
        for table in info_tables:
            name_of_issuer = table.find("ns:nameOfIssuer",namespace).text if table.find("ns:nameOfIssuer",namespace) is not None else None
            title_of_class = table.find("ns:titleOfClass",namespace).text if table.find("ns:titleOfClass",namespace) is not None else None
            value_of_share = int(table.find("ns:value",namespace).text) if table.find("ns:value",namespace) is not None else 0
                        
            # Extract share details from 'shrsOrPrnAmt' element
            shrs_or_prn_amt = table.find("ns:shrsOrPrnAmt",namespace)
            shares = None
            share_type = None
            
            if shrs_or_prn_amt is not None:
                shares = int(shrs_or_prn_amt.find("ns:sshPrnamt", namespace).text) if shrs_or_prn_amt.find("ns:sshPrnamt", namespace) is not None else 0
                share_type = shrs_or_prn_amt.find("ns:sshPrnamtType",namespace).text if shrs_or_prn_amt.find("ns:sshPrnamtType",namespace) is not None else None

            
            # Store the data in a dictionary
            if name_of_issuer and title_of_class:
                key = (name_of_issuer, title_of_class)
                grouped_data[key]['Shares'] += shares
                grouped_data[key]['Value_Of_Share'] += value_of_share
            
        # Convert grouped data into a list of dictionaries for easier use
        self.data = [
            Holdings(issuer=key[0],title_of_class=key[1],shares=value['Shares'],marketValue=value['Value_Of_Share'])
            for key, value in grouped_data.items()
        ]

    def get_data(self):
        # Return the extracted data
        return self.data

    def print_data(self):
        # Print the extracted data in a readable format
        for entry in self.data:
            print(f"Issuer: {entry.Issuer}, Title of Class: {entry.TitleOfClass}, "
                  f"Shares: {entry.Shares}, Value: {entry.MarketValue}")

    def get_top_n_shares(self, top_n):
        """
        Returns the top N holdings based on the number of shares.
        
        :param top_n: The number of top holdings to return
        :return: A list of the top N Holdings objects sorted by Shares in descending order
        """
        # Sort self.data by Shares in descending order
        sorted_holdings = sorted(self.data, key=lambda x: x.Shares, reverse=True)
        
        # Return the top N holdings
        return sorted_holdings[:top_n]
    
    def get_top_n_marketValue(self, top_n):
        """
        Returns the top N holdings based on the number of shares.
        
        :param top_n: The number of top holdings to return
        :return: A list of the top N Holdings objects sorted by Shares in descending order
        """
        # Sort self.data by Market Value in descending order
        sorted_holdings = sorted(self.data, key=lambda x: x.MarketValue, reverse=True)
        
        # Return the top N holdings
        return sorted_holdings[:top_n]

