# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente: 
properties = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def add_price(property):
	price = (property['metros']*1000 + property['habitaciones']*5000 + property['garaje']+15000)*(1-(2023-property['año'])/100)

	if property['zona'] == 'B':
		price *= 1.5
	
	property['precio'] = price
	return property


def property_finder(propertyList, budget):
	def filtro(property):
		return property['precio'] <= budget
		
			# Devuelve una lista con los inmuebles cuyo precio es menor o igual que el dado
	return list(filter(filtro,map(add_price, propertyList)))


print(property_finder(properties, 200000))
