# 🕵️‍♂️ Secret Auction Game (Python)

This is a simple Python console program that simulates a **secret auction**. Multiple users can input their names and bids, and at the end, the program determines the highest bidder and declares the winner — all while keeping bids hidden from others.

---

## 💻 How It Works

1. Each bidder is asked for:
   - Their **name**
   - Their **bid amount**
   - Whether there are any other bidders

2. If there are more bidders, the screen clears (using `print("\n" * 100)`) to simulate secrecy.

3. Once no more bidders remain, the program calculates and prints the **highest bidder** and their bid.

---

## 📂 File Structure
auction_game/
├── main.py          # The main game logic
├── art.py           # Contains the ASCII logo (optional)
├── README.md        # You’re reading it

---

## 📦 Requirements

- Python 3.x

No third-party packages needed — pure Python.

---

## ▶️ How to Run

1. Clone this repository or copy the `main.py` and `art.py` files.
2. Run the script:

```bash
python main.py

Welcome to the Secret auction program.
What is your name?: Alice
What is your Bid?: 100
Are there any other Bidders? Type 'yes' or 'no': yes

What is your name?: Bob
What is your Bid?: 150
Are there any other Bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of $150

🧠 Skills Practiced
	•	Input/output in Python
	•	Dictionaries
	•	While loops and conditionals
	•	Basic functions
	•	Clean terminal simulation

⸻

🏁 Future Improvements
	•	Use the os module for a more reliable screen clear
	•	Add error handling for non-numeric bids
	•	Support auction types like reverse auctions

⸻

Author

Made by Lucas F. while learning Python 
