"""
Codecademy Module 1 Functions & Loops Practice
August 26, 2023

Write a program that:
  1. Takes user package weight
  2. Runs the user package weight in 3 shipping options: (ground shipping, ground shipping premium, and drone shipping)
  3. Compares the cost of the 3 shipping options
  4. Recommends to the user which shipping option to use based on cheapest cost
"""

def ground_shipping(user_weight):
  #Ground Shipping Prices Per Pound
  flat_charge = 20
  over_zero_leq_two = 1.5
  over_two_leq_six = 3
  over_six_leq_ten = 4
  over_ten = 4.75
  
  if user_weight <= 0:
      print("Package does not meet shipping weight minimum. Restarting Program")
      main()
  elif user_weight > 0 and user_weight <= 2:
      ground_shipping_estimate = flat_charge + (user_weight * over_zero_leq_two)
      print("Ground Shipping Estimate: ", ground_shipping_estimate)
  elif user_weight > 2 and user_weight <= 6:
      ground_shipping_estimate = flat_charge + (user_weight * over_two_leq_six)
      print("Ground Shipping Estimate: ", ground_shipping_estimate)
  elif user_weight > 6 and user_weight <= 10:
      ground_shipping_estimate = flat_charge + (user_weight * over_six_leq_ten)
      print("Ground Shipping Estimate: ", ground_shipping_estimate)
  elif user_weight > 10:
      ground_shipping_estimate = flat_charge + (user_weight * over_ten)
      print("Ground Shipping Estimate: ", ground_shipping_estimate)
  
  return ground_shipping_estimate

def ground_premium_shipping():
  ground_premium_estimate, flat_charge = (125, 125)
  print("Ground Premium Shipping Estimate: ", flat_charge)
  
  return ground_premium_estimate

def drone_shipping(user_weight):
  #Ground Shipping Prices Per Pound
  over_zero_leq_two = 4.5
  over_two_leq_six = 9
  over_six_leq_ten = 12
  over_ten = 14.25
  
  if user_weight <= 0:
      print("Package does not meet shipping weight minimum. Restarting Program")
      main()
  elif user_weight > 0 and user_weight <= 2:
      drone_shipping_estimate = user_weight * over_zero_leq_two
      print("Drone Shipping Estimate: ", drone_shipping_estimate)
  elif user_weight > 2 and user_weight <= 6:
      drone_shipping_estimate = user_weight * over_two_leq_six
      print("Drone Shipping Estimate: ", drone_shipping_estimate)
  elif user_weight > 6 and user_weight <= 10:
      drone_shipping_estimate = user_weight * over_six_leq_ten
      print("Drone Shipping Estimate: ", drone_shipping_estimate)
  elif user_weight > 10:
      drone_shipping_estimate = user_weight * over_ten
      print("Drone Shipping Estimate: ", drone_shipping_estimate)
  
  return drone_shipping_estimate

def compare_shipping_prices(ground_estimate, ground_premium_estimate, drone_estimate):
  if ground_estimate <= ground_premium_estimate and ground_estimate <= drone_estimate:
    best_shipping_type = "Ground Shipping"
    cheapest_price = ground_estimate
  elif ground_premium_estimate <= ground_estimate and ground_premium_estimate <= drone_estimate:
    best_shipping_type = "Ground Premium Shipping"
    cheapest_price = ground_premium_estimate
  elif drone_estimate <= ground_estimate and drone_estimate <= ground_premium_estimate:
    best_shipping_type = "Drone Shipping"
    cheapest_price = drone_estimate
  
  print(f"Recommended shipping: {best_shipping_type}, Price: ${cheapest_price}\n")
  return best_shipping_type

def main():
  #INTRODUCE START OF PROGRAM
  intro = "\nJ.D. PACKAGING"
  print(intro)
  
  #GET WEIGHT FROM USER INPUT
  weight = float(input("\nEnter package weight in pounds: "))

  #RUN FUNCTIONS
  final_ground = ground_shipping(weight)
  final_ground_premium = ground_premium_shipping()
  final_drone = drone_shipping(weight)
  
  compare_shipping_prices(final_ground, final_ground_premium, final_drone)


#Call Program Start 
main()