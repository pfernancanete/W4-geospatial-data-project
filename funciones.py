donde = input
def geocode(address):
    """
    Introduciendo un dirección se obtiene las coordenadas
    """
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":[float(data["latt"]),float(data["longt"])]}
    except:
        return data  