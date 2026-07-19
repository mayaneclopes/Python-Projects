"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

emojis = { #emoji dic
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

message = input(f"What is your message? ")
updated_words = []

for word in message.split():
#split breaks a string into a list of substrings 
# (default is separating by whitespace)
    cleaned_message = word.lower().strip(".,!?")
    emoji = emojis.get(cleaned_message, "")
    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = "  ".join(updated_words)
#Join merges in iterable of string into 1 single string using 
#a specified separator.
print("\n Enhanced message:\n")
print(updated_message)