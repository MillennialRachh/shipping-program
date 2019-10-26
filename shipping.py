
def ground_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)

print(ground_shipping_cost(8.4))

premium_ground_shipping_cost = 125.00

def drone_shipping_cost(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return (price_per_pound * weight)
print(drone_shipping_cost(1.5))

def print_cheapest_shipping_method(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping_cost
  drone = drone_shipping_cost(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print("The cheapest option available is $%.2f with %s shipping."
        % (cost, method))

print_cheapest_shipping_method(4.8)
print_cheapest_shipping_method(41.5)
