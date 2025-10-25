# AI-Based Daily Habit Tracker
# ----------------------------
# This program helps users track daily habits, store progress,
# and use AI to predict how consistent they are and give suggestions.

import json
import os
import random
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

# File to store habit data
DATA_FILE = "habit_data.json"

# Load existing data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"habits": {}}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new habit
def add_habit(data):
    habit = input("Enter a new habit to track: ").strip().title()
    if habit in data["habits"]:
        print("This habit already exists!")
    else:
        data["habits"][habit] = []
        print(f"Habit '{habit}' added successfully!")
    save_data(data)

# Mark today's progress
def mark_progress(data):
    if not data["habits"]:
        print("No habits found! Add one first.")
        return

    print("\nYour habits:")
    for i, habit in enumerate(data["habits"], 1):
        print(f"{i}. {habit}")

    choice = int(input("Enter habit number to mark as done: ")) - 1
    habits = list(data["habits"].keys())
    if 0 <= choice < len(habits):
        habit = habits[choice]
        today = str(datetime.now().date())
        if today not in data["habits"][habit]:
            data["habits"][habit].append(today)
            print(f"Marked '{habit}' as done for today!")
        else:
            print(f"'{habit}' already marked for today.")
    else:
        print("Invalid choice!")

    save_data(data)

# Show habit report
def show_report(data):
    print("\n--- Habit Report ---")
    for habit, dates in data["habits"].items():
        print(f"{habit}: {len(dates)} days completed")

# Simple AI suggestion using Linear Regression
def ai_suggestion(data):
    if not data["habits"]:
        print("No data to analyze yet.")
        return

    print("\n--- AI Habit Suggestions ---")

    for habit, dates in data["habits"].items():
        days = len(dates)
        if days < 2:
            print(f"{habit}: Not enough data yet.")
            continue

        # Fake data for demonstration
        X = np.array(range(1, days + 1)).reshape(-1, 1)
        y = np.array([random.randint(0, 1) for _ in range(days)])

        model = LinearRegression()
        model.fit(X, y)
        prediction = model.predict(np.array([[days + 1]]))[0]

        if prediction > 0.5:
            print(f"✅ You’re doing well with '{habit}'. Keep it up!")
        else:
            print(f"⚠️ You might skip '{habit}' soon. Try setting a reminder!")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n=== AI Daily Habit Tracker ===")
        print("1. Add New Habit")
        print("2. Mark Today's Progress")
        print("3. View Habit Report")
        print("4. Get AI Suggestions")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_habit(data)
        elif choice == "2":
            mark_progress(data)
        elif choice == "3":
            show_report(data)
        elif choice == "4":
            ai_suggestion(data)
        elif choice == "5":
            print("Goodbye! Stay consistent with your habits 💪")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()




