"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""
import textwrap
name = input("What is your name? ").strip().title()
profession = input("What is your profession? ").strip().title()
passion = input("Describe your passion in one line: ").strip().capitalize()
emoji = input("Show us your favorite emoji: ").strip()
website = input("What's your website? ").strip().lower()

print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Now choose 1, 2 or 3? ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name}\n{profession}\n {passion}\n {website}"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"
    
bio = generate_bio(style)
print("*" * 50)
print("\nYour stylish bio: ")
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save your bio to a text file? [Y/N] ").lower()

if save == 'y' or 'yes':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("Bio saved!")
