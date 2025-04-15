# # Simulate a traffic light system using conditionals and loops
# import time
#
# def traffic_light_simulation():
#     while True:
#         print("Traffic Light: RED")
#         time.sleep(5)
#
#         print("Traffic Light: GREEN")
#         time.sleep(5)
#
#         print("Traffic Light: YELLOW")
#         time.sleep(2)
#
#         print("\033c", end="")
#
# try:
#    print("Traffic Light Simulation Started. Press Ctrl+C to stop.")
#    traffic_light_simulation()
# except KeyboardInterrupt:
#     print("\nTraffic Light Simulation Stopped.")
#
#
# # Create a program to check if a user is eligible for a bank loan based on salary, age, and credit score using nested conditionals.
# def check_loan_eligibility(salary, age, credit_score):
#
#     if age >= 21:
#         if salary >= 30000:
#             if credit_score >= 650:
#                 return "Congratulations! You are eligible for the bank loan."
#             else:
#                 return "Sorry, your credit score is too low for a bank loan."
#         else:
#             return "Sorry, your salary is too low for a bank loan."
#     else:
#         return "Sorry, you must be at least 21 years old to apply for a bank loan."
#
# try:
#     user_salary = float(input("Enter your salary: "))
#     user_age = int(input("Enter your age: "))
#     user_credit_score = int(input("Enter your credit score: "))
#
#     result = check_loan_eligibility(user_salary, user_age, user_credit_score)
#     print(result)
# except ValueError:
#     print("Invalid input. Please enter numeric values for salary, age, and credit score.")
#
#
import smartHome

smart_home = smartHome.SmartHome()
try:
    temperature = float(input("Enter the current temperature (°C): "))
    humidity = float(input("Enter the current humidity (%): "))
    motion_detected = input("Is there motion detected? (yes/no): ").strip().lower() == 'yes'

    smart_home.check_sensors(temperature, humidity, motion_detected)

except ValueError:
    print("Invalid input. Please enter numeric values for temperature and humidity.")
except KeyboardInterrupt:
    print("\nSmart Home Automation Simulation Stopped.")



# Problem 10 stock market tracker
def calculate_moving_average(prices, window_size):
    if len(prices) < window_size:
        return sum(prices) / len(prices)  # fallback
    return sum(prices[-window_size:]) / window_size


def analyze_trend(prices):
    current_price = prices[-1]
    moving_average = calculate_moving_average(prices, 5)
    print("Stock Market indicator")
    print(f"Current Price: {current_price}")
    print(f"5-Day Moving Average: {moving_average:.2f}")

    if current_price > moving_average:
        print("Signal: BUY (Price above moving average)")
    elif current_price < moving_average:
        print("Signal: SELL (Price below moving average)")
    else:
        print("Signal: HOLD (Price equals moving average)")
historical_prices = [100, 102, 101, 105, 110, 108, 107]
analyze_trend(historical_prices)
