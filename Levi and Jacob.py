import random

# Function to display the introduction
def intro():
    print("Welcome to the Tesco Adventure!")
    print("You encounter a stranger in the store.")
    print("They could ask you a strange question or be doing something weird.")
    print("Choose how to respond to them!")

# Function to present the stranger's action
def stranger_action():
    actions = [
        "The stranger suddenly stares at you and asks, 'If you could be any vegetable, what would you be?'",
        "You see the stranger pouring milk into a cereal box in the middle of the aisle.",
        "The stranger looks at you and says, 'I can predict the future, and I see a very bad shopping experience for you.'",
        "You notice the stranger dancing with a broom as if it’s a microphone.",
        "The stranger approaches you and whispers, 'What would you do if I just started yelling random numbers?'",
        "The stranger is wearing a colander on their head and claims it's a helmet for 'alien protection.'",
        "The stranger pulls out a rubber chicken and asks, 'Is this your lunch or mine?'",
        "You watch as the stranger tries to communicate with a bag of flour, saying, 'It’s my best friend!'",
        "The stranger starts mimicking the sounds of various fruits, attempting to start a fruit orchestra.",
        "You hear the stranger yelling, 'I found the secret to happiness!' and they hand you a can of beans.",
        "The stranger is rolling around in shopping carts, yelling, 'I'm training for the Olympics!'",
        "You see the stranger trying to build a pillow fort in the frozen food section.",
        "The stranger says, 'I just discovered the perfect recipe for chocolate-covered broccoli!'",
        "The stranger is arguing with a mannequin, insisting it’s their long-lost twin.",
        "The stranger challenges you to vote for the best costume in the store, claiming to be the 'Best Tomato.'",
        "The stranger holds up a bizarre item and asks you to guess what it is, insisting it's the next big trend.",
        "The stranger offers you a 'future food' sample that they claim is 'protein-flavored air.'",
        "You see the stranger trying to juggle fruits in the aisle and asks if you want to join them."
    ]
    return random.choice(actions)

# Function to handle player response
def get_response():
    print("\nHow do you respond?")
    print("1: Give a friendly but confused response.")
    print("2: Respond in an unhinged and rude manner.")
    
    # More specific responses based on the action
    friendly_responses = [
        "You respond, 'Uh, I guess I would be a carrot? That's healthy, right?'",
        "You say, 'That's an interesting thought! Maybe a cucumber? They’re cool under pressure!'",
        "You chuckle and reply, 'I would be a potato! They make everything better!'",
        "You smile and say, 'A colander? That sounds... unique! Are you okay?'",
        "You laugh and say, 'I think your friend might be better off in the pantry!'",
        "You ask, 'Chocolate-covered broccoli? How does that even work?'",
        "You reply, 'Well, that would definitely be a conversation starter!'",
        "You comment, 'Wow, that sounds like a great way to ruin a perfectly good vegetable!'",
        "You say, 'Your costume is amazing! Best tomato I've seen all day!'",
        "You respond, 'Is that the next big trend? I might need to get one!'",
        "You smile and say, 'I love juggling! Let’s do it!'"
    ]
    
    rude_responses = [
        "You shout, 'What kind of question is that? Just get a life and stop wasting my time!'",
        "You respond with a sneer, 'Who asks someone that? You're weird!'",
        "You scoff, 'Yeah, sure! And your rubber chicken is gourmet, right?'",
        "You yell, 'If you want to talk to flour, go buy some and leave me alone!'",
        "You roll your eyes and say, 'This is why I don't talk to strangers!'",
        "You say, 'Why don't you get out of the frozen food aisle and back to your planet?'",
        "That's the dumbest thing I've ever heard! No one wants that!'",
        "You smirk and say, 'Do I look like I care about your silly costume contest?'",
        "You respond sarcastically, 'Oh great, another ridiculous trend to ignore!'",
        "You laugh and say, 'Good luck with your juggling act; it’s not gonna impress anyone!'"
    ]
    
    response = input("Choose 1 or 2: ")
    
    if response == "1":
        return random.choice(friendly_responses)
    elif response == "2":
        return random.choice(rude_responses)
    else:
        return "Invalid choice! Please choose 1 or 2."

# Function for stranger's response based on player choice
def stranger_reply(player_response):
    replies = [
        "The stranger laughs and says, 'That's a good choice! I love carrots!'",
        "They look puzzled and say, 'Huh, I never thought of it that way!'",
        "The stranger nods in agreement, 'I mean, who wouldn't want to be a potato?'",
        "They reply, 'It's all about creativity! I respect that.'",
        "The stranger seems unfazed and says, 'People often don't understand my genius!'",
        "They burst out laughing, 'Chocolate-covered broccoli is the future!'",
        "The stranger grins and replies, 'I love your enthusiasm! Let’s start a movement!'",
        "They shrug and say, 'Not everyone can appreciate a good vegetable dish!'",
        "The stranger beams and says, 'Thanks for supporting the costume contest!'",
        "They say, 'Exactly! This is the hottest trend of the season!'",
        "The stranger smiles and says, 'Juggling is a great skill! Let’s juggle together!'"
    ]
    
    return random.choice(replies)

# Main game loop
def main():
    intro()
    score = 0
    
    while True:
        action = stranger_action()
        print(f"\n{action}")
        
        response = get_response()
        print(response)

        # Get stranger's reply based on the player's response
        stranger_response = stranger_reply(response)
        print(stranger_response)

        # Update score based on the friendliness of the response
        if "You respond" in response or "You say" in response:
            score += 1
        else:
            score -= 1

        print(f"Current score: {score}")

        # Check for special conditions based on score
        if score >= 5:
            print("\nYou've reached a positive vibe! The stranger seems more friendly and open to conversation.")
        elif score <= -5:
            print("\nUh-oh! The stranger looks a bit offended. They might not want to talk anymore.")

        continue_game = input("\nDo you want to encounter the stranger again? (yes/no): ")
        if continue_game.lower() != 'yes':
            print("Thanks for playing! Have a great day shopping at Tesco!")
            break

if __name__ == "__main__":
    main()


