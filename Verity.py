import random

# ANSI Escape Codes for terminal colours
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"

WORD_LIST = ["VERITY", "CRUELTY", "FALSITY", "LOVITY", "OBESITY"]
MAX_ATTEMPTS = 6


def evaluate_guess(guess_list: list, secret_list: list) -> str:
    ## This function checks the guess and returns the list coloured
    result = []
    secret_copy = secret_list.copy()
    guess_copy = guess_list.copy()
    feedback = [""] * 4

    # Searching for correct veritys
    for i in range(4):
        if guess_copy[i] == secret_copy[i]:
            feedback[i] = f"{GREEN}[{guess_copy[i]}]{RESET}"
            secret_copy[i] = None  # Marked as used
            guess_copy[i] = None

    # 2. Searching for wrong veritys
    for i in range(4):
        if guess_copy[i] is not None:
            if guess_copy[i] in secret_copy:
                feedback[i] = f"{YELLOW}[{guess_copy[i]}]{RESET}"
                secret_copy[secret_copy.index(guess_copy[i])] = None
            else:
                feedback[i] = f"{GRAY}[{guess_copy[i]}]{RESET}"

    return " ".join(feedback)


def play_game():
    secret_list  = random.choices(WORD_LIST,k=4)


    print(f"=== VERITY GAME ===")
    print(f"FIND THE VERITYS!! \n")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        while True:
            guess = input(f"TRY {attempt}/{MAX_ATTEMPTS}: ").strip().upper()
            guess_list = guess.split()

            if len(guess_list) == 4:
                break


        formatted_result = evaluate_guess(guess_list, secret_list)
        print(f"Result:   {formatted_result}\n")

        # Success check
        if guess_list == secret_list:
            print(f"🎉 YOU WON VERITY!!!")
            return

    print(f"❌ YOU LOST, IT WAS {secret_list}\n")


if __name__ == "__main__":
    play_game()