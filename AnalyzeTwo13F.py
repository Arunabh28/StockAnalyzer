from Analyze13F import Analyze13F
from ChangeInData import ChangeInData

class AnalyzeTwo13F:
    def __init__(self, xml_file_1, xml_file_2):
        self.analyze_1 = Analyze13F(xml_file_1)
        self.analyze_2 = Analyze13F(xml_file_2)

    def new_issuers_added(self):
        issuers_1 = {holding.Issuer for holding in self.analyze_1.get_data()}
        issuers_2 = {holding.Issuer for holding in self.analyze_2.get_data()}

        return issuers_2 - issuers_1

    def issuers_removed(self):
        issuers_1 = {holding.Issuer for holding in self.analyze_1.get_data()}
        issuers_2 = {holding.Issuer for holding in self.analyze_2.get_data()}

        return issuers_1 - issuers_2

    def top_n_issuers_increased_shares(self, top_n):
        increase_data = []

        data_1 = {holding.Issuer: holding for holding in self.analyze_1.get_data()}
        data_2 = {holding.Issuer: holding for holding in self.analyze_2.get_data()}

        for issuer, holding_2 in data_2.items():
            holding_1 = data_1.get(issuer)
            if holding_1:
                share_diff:int = holding_2.Shares - holding_1.Shares
                if share_diff > 0:
                    changedData= ChangeInData(issuer, "Increase",share_diff)
                    increase_data.append(changedData)

        increase_data.sort(key=lambda x: x.Quantity, reverse=True)
        return increase_data[:top_n]

    def top_n_issuers_decreased_shares(self, top_n):
        decrease_data = []

        data_1 = {holding.Issuer: holding for holding in self.analyze_1.get_data()}
        data_2 = {holding.Issuer: holding for holding in self.analyze_2.get_data()}

        for issuer, holding_2 in data_2.items():
            holding_1 = data_1.get(issuer)
            if holding_1:
                share_diff = holding_2.Shares - holding_1.Shares
                if share_diff < 0:
                    decrease_data.append(ChangeInData(issuer, "Decrease", share_diff))

        decrease_data.sort(key=lambda x: x.Quantity)
        return decrease_data[:top_n]

    def top_n_issuers_market_value_changed(self, top_n):
        positive_changes = []
        negative_changes = []

        data_1 = {holding.Issuer: holding for holding in self.analyze_1.get_data()}
        data_2 = {holding.Issuer: holding for holding in self.analyze_2.get_data()}

        for issuer, holding_2 in data_2.items():
            holding_1 = data_1.get(issuer)
            if holding_1:
                mv_1 = holding_1.Shares * holding_1.MarketValue
                mv_2 = holding_2.Shares * holding_2.MarketValue
                mv_diff = mv_2 - mv_1
                if mv_diff > 0:
                    positive_changes.append(ChangeInData(issuer, "Increase", mv_diff))
                elif mv_diff < 0:
                    negative_changes.append(ChangeInData(issuer, "Decrease",mv_diff))

        positive_changes.sort(key=lambda x: x.Quantity, reverse=True)
        negative_changes.sort(key=lambda x: x.Quantity)

        return positive_changes[:top_n], negative_changes[:top_n]
