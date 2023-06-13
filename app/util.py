import json

def save_to_json(entity_data, filename):
    with open(f'/home/ra-terminal/Desktop/portfolio_projects/subway_delays/{filename}.json', 'w') as f_obj:
        json.dump(entity_data, f_obj, indent = 2)
