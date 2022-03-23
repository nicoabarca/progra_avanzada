import re
from dateutil.parser import parse
from utils import get_json_data

class GameLogic():

    def __init__(self):
        self.connected_players = []

    #https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
    #Check if the user name and birth date is valid
    def verify_user(self, user_name, birth_date):
        min, max = get_json_data("min_caracteres"), get_json_data("max_caracteres")
        valid_alphanumeric = re.match('^[a-zA-Z0-9_]+$', user_name)
        valid_date = True
        valid_length = min <= len(user_name) <= max
        valid_name = user_name in self.connected_players
        try: 
            parse(birth_date, fuzzy=False)
        except ValueError:
            valid_date = False
        valid_user = True

        if not valid_alphanumeric or not valid_date or not valid_length or not valid_name:
            valid_user = False
        else:
            self.connected_players.append(user_name)

        verify_user_dict = {"target_function": "", "valid_user_response": valid_user}
        
        return verify_user_dict