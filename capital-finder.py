import requests

def capital_finder(request):
    # Extract the query parameter from the request
    country = request.args.get('country')
    capital = request.args.get('capital')

    # Check if the country query parameter is provided
    if country:
        # Make a GET request to the REST Countries API
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()

        # Extract the capital from the API response
        capital = data[0]['capital']

        # Send the response
        return f"The capital of {country} is {capital}."

    # Check if the capital query parameter is provided
    elif capital:
        # Make a GET request to the REST Countries API
        response = requests.get(f"https://restcountries.com/v3.1/capital/{capital}")
        data = response.json()

        # Extract the country from the API response
        country = data[0]['name']['common']

        # Send the response
        return f"{capital} is the capital of {country}."

    # Handle the case when no valid query parameters are provided
    else:
        return "Please provide a valid country or capital query parameter."
