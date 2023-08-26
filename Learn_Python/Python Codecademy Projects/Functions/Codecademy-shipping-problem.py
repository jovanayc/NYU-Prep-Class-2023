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
  print("In ground fucnt.")
  #Ground Shipping Prices Per Pound
  flat_charge = 20
  over_zero_leq_two = 1.5
  over_two_leq_six = 3
  over_six_leq_ten = 4
  over_ten = 4.75
  
  if user_weight <= 0:
      print("Package does not meet shipping weight minimum. Restarting Program")
      main()
  elif user_weight > 0 and user_weight < 2:
      #Set variable to be returned
      ground_shipping_estimate = flat_charge + (user_weight * over_zero_leq_two)
      print("Ground Shipping Price Estimate: ", ground_shipping_estimate)
      
  return ground_shipping_estimate


def main():
  #INTRODUCE START OF PROGRAM
  intro = "\nJ.D. PACKAGING"
  print(intro)
  
  #GET WEIGHT FROM USER INPUT
  weight = float(input("\nEnter package weight in pounds: "))
  print("Weight input in main: ", weight)

  #RUN FUNCTIONS
  ground_shipping(weight)
  
      '''
      TO-DO
        # Write two functions for ground premium & Drone costs
        # Write function to compare costs of all three estimates
        # Print suggestion message in main
      '''
  
  #ground_shipping_premium()
  #drone_shipping(weight)
  #compare(ground_shipping(weight), ground_shipping_premium(), drone_shipping(weight))

  #print(f"Cheapest shipping option: {suggested_price}")
  
#Call Program Start 
main()