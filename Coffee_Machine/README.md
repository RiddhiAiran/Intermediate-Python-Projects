# Coffee Machine

## Overview
The Coffee Machine program simulates a virtual coffee vending machine that allows users to:
- Choose from three coffee options: Espresso, Latte, or Cappuccino.
- Insert coins to pay for the chosen coffee.
- Check resource availability (water, milk, coffee).
- View a report of available resources and machine profit.

The program is designed to ensure sufficient resources are available before serving coffee and to handle user transactions accurately, including change.

---
## Program Demo
Below is a quick demo of Coffee Machine program:


---
## Features
- **Coffee Selection:** Offers three drink options with predefined recipes and costs.
- **Resource Management:** Tracks ingredients like water, milk, coffee, and the machine’s profit.
- **Transaction Handling:** Calculates total inserted money and determines whether the payment is sufficient.
- **Interactive Feedback:** Provides clear messages to guide the user.
- **Report Generation:** Displays current resource levels and profit earned.
- **Admin Mode:** Includes an `off` option to shut down the machine.

---

## Working
1. **Start the Program:** Run the script, and the welcome screen will appear.
2. **Choose an Option:** Type your choice (`espresso`, `latte`, `cappuccino`, `report`, or `off`).
3. **Insert Coins:** If a coffee option is selected, follow the prompt to insert coins.
4. **Receive Coffee:** If the transaction is successful, the coffee is served.
5. **Admin Options:**
   - `report`: Displays the machine’s resources and profit.
   - `off`: Exits the program.

---

## Code Overview

### Key Concepts
- **Resource Management:**
  - The program checks if enough resources (water, milk, coffee) are available before making a drink.
  - Resources are deducted when a coffee is served.
- **Transaction Handling:**
  - The `insert_coint` function calculates the total money inserted.
  - The `is_transaction_successful` function validates the transaction and updates the machine’s profit.
- **Dynamic Interaction:**
  - `typing`, `hold_screen`, and `clear_screen` functions enhance the user experience with dynamic prompts and screen updates.

### Core Functions
- `print_report`: Displays the current resource levels and profit.
- `is_resource_sufficient`: Checks if there are enough resources to make the chosen drink.
- `insert_coint`: Handles coin insertion and calculates the total amount.
- `is_transaction_successful`: Validates payment and calculates change if applicable.
- `make_coffee`: Deducts resources and serves the coffee.

---

## Prerequisites
- Python 3.8 +
- Modules required:
  - `typing`
  - `hold_screen`
  - `clear_screen`
  - `get_input`

Ensure these modules and the `MENU`, `resources`, and `profit` data structures are available in the program.

---

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run the program:
   ```bash
   python coffee_machine.py
   ```

---

## Acknowledgements
- **Design Inspiration:** Simulating real-world coffee machine operations.
- **Modules and Libraries:** Leveraged Python’s interactive input/output capabilities for seamless user interaction.

---

## Future Enhancements
- Add more coffee options and customizable recipes.
- Implement a graphical user interface (GUI).
- Introduce a maintenance mode to refill resources.

---

Enjoy your coffee experience! ☕
