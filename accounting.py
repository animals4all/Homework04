MELON_COST = 1.00

def customer_orders(file_name):
	"""Go through the given file and create a dictionary with entries for each order."""
	orders_dict = {}
	file_obj = open(file_name)
	file_contents = file_obj.read()
	file_obj.close()

	melon_orders = file_contents.split("\n")
	for order in melon_orders:
		if order != "":
			# Ignore empty lines

			# Split each order into a list of the customer's name, the amount of melons bought, and
			# the amount that the customer paid
			order = order.split(",")

			customer_name = order[1]
			customer_melons = float(order[2])
			customer_paid = float(order[3])

			orders_dict[customer_name] = (customer_melons, customer_paid)

	return orders_dict

def are_melons_underpaid(customer_name, customer_melons, customer_paid):
	"""Check if the given customer didn't pay the right amount, if they didn't then print this
	information."""
	customer_expected = customer_melons * MELON_COST
	if customer_expected != customer_paid:
		print customer_name, "paid %.2f, expected %.2f" % (customer_paid, customer_expected)

def print_report():
	"""Print out a report that shows the incorrect orders."""
	orders_dict = customer_orders("customer_orders.csv")
	
	for customer_name, value in orders_dict.iteritems():
		# Dictionary key = customer's name

		customer_melons = value[0]
		customer_paid = value[1]
		are_melons_underpaid(customer_name, customer_melons, customer_paid)

print_report()
