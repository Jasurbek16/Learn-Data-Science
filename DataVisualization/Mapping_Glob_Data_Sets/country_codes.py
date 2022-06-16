from pygal_maps_world import i18n

def get_country_code(country_name):
    # Return the Pygal 2-digit country code for the given country
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code        
    return None
