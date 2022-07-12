import requests
from data_manager import DataManager

tool = DataManager()

destination_data = tool.get_destination_data()
edited_destionation_data = tool.add_destination_code()