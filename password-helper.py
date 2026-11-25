import secrets
from pathlib import Path

# Find the wordlist beside this script, even if you run it from another folder.
wordlist_path = Path(__file__).with_name("eff_large_wordlist.txt")

# Read the wordlist and store each dice result with its matching word.
wordlist = {}
with open(wordlist_path, encoding="utf-8") as wordlist_file:
    for line in wordlist_file:
        # Split a line like "11111 abacus" into its number and word.
        parts = line.split()
        dice_result_from_file = parts[0]
        matching_word = parts[1]
        wordlist[dice_result_from_file] = matching_word

# Keep the six chosen words so we can print them together at the end.
passphrase_words = []

# Make six words. Each word comes from rolling five dice.
for roll_number in range(1, 7):
    dice_result = ""

    # Pick one number for each of the five dice.
    for die_number in range(1, 6):
        die_result = secrets.choice("123456")
        dice_result = dice_result + die_result

    # Use the five dice results to find the matching word.
    matching_word = wordlist[dice_result]
    passphrase_words.append(matching_word)

    # Show the dice result and the word it selected.
    print(f"Roll {roll_number}: {dice_result} -> {matching_word}")

# Join the six words with spaces to make the passphrase.
passphrase = " ".join(passphrase_words)
print(f"Passphrase: {passphrase}")
