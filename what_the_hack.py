import time
import sys
import os

CHEAT_CODE = "what the hack!"
MAX_ATTEMPTS = 3

# ================= UTILITIES =================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(text="Loading", duration=2):
    sys.stdout.write(text + " ")
    sys.stdout.flush()
    for _ in range(20):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(duration / 20)
    print()

def check_cheat(user_input, answer_hint):
    if user_input.strip().lower() == CHEAT_CODE:
        slow_print("\n🧨 CHEAT CODE ACTIVATED!")
        slow_print(f"✔ Correct solution: {answer_hint}")
        time.sleep(1.2)
        return True
    return False

def header(lives, level_name):
    clear()
    slow_print(f"❤ Attempts left: {lives}", 0.01)
    slow_print(f"🧠 {level_name}", 0.01)
    slow_print("-" * 40, 0.005)

# ================= ASCII TITLE =================
def title_animation():
    clear()
    title = [
        "██╗    ██╗██╗  ██╗ █████╗ ████████╗",
        "██║    ██║██║  ██║██╔══██╗╚══██╔══╝",
        "██║ █╗ ██║███████║███████║   ██║   ",
        "██║███╗██║██╔══██║██╔══██║   ██║   ",
        "╚███╔███╔╝██║  ██║██║  ██║   ██║   ",
        " ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ",
        "",
        "      ████████╗██╗  ██╗███████╗",
        "      ╚══██╔══╝██║  ██║██╔════╝",
        "         ██║   ███████║█████╗  ",
        "         ██║   ██╔══██║██╔══╝  ",
        "         ██║   ██║  ██║███████╗",
        "         ╚═╝   ╚═╝  ╚═╝╚══════╝",
        "",
        "           ██╗  ██╗ █████╗  ██████╗██╗  ██╗",
        "           ██║  ██║██╔══██╗██╔════╝██║ ██╔╝",
        "           ███████║███████║██║     █████╔╝ ",
        "           ██╔══██║██╔══██║██║     ██╔═██╗ ",
        "           ██║  ██║██║  ██║╚██████╗██║  ██╗",
        "           ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝",
        "",
        "                WHAT THE HACK!",
        "",
        "              By Aymen Ftita",
    ]
    for line in title:
        slow_print(line, 0.01)
    time.sleep(2)

# ================= INTRO =================
def intro():
    clear()
    slow_print("Initializing secure terminal...")
    loading_bar("Bypassing firewall")
    slow_print("\nACCESS GRANTED\n")
    slow_print("Rule: You only have 3 attempts.")
    slow_print("Cheat code exists. Find it.\n")
    time.sleep(1)

# ================= LEVELS =================
def level_1(lives):
    header(lives, "LEVEL 1 — LOGIC PASSWORD")
    slow_print("Hints:")
    slow_print("1️⃣ I am always in front, but I never move.")
    slow_print("2️⃣ I start every story.")
    slow_print("3️⃣ I am the same in every language.\n")

    answer = input("Enter the password: ")
    if check_cheat(answer, "a"):
        return True
    return answer.strip().lower() == "a"

def level_2(lives):
    header(lives, "LEVEL 2 — POLITENESS TEST")
    slow_print(">>> i will **ck you\n")

    response = input("Your response: ")
    if check_cheat(response, "A polite reply like: 'Please stop'"):
        return True

    aggressive = ["fuck", "kill", "idiot", "stupid", "shit"]
    polite = ["please", "respect", "stop", "don't", "do not"]

    if any(w in response.lower() for w in aggressive):
        return False
    return any(w in response.lower() for w in polite)

def level_3(lives):
    header(lives, "LEVEL 3 — META RULE")
    slow_print("Do NOT type the password.\n")

    answer = input("Input: ")
    if check_cheat(answer, "Anything except the password"):
        return True
    return answer.strip().lower() != "a"

def level_4(lives):
    header(lives, "LEVEL 4 — WRONG ANSWER WINS")
    slow_print("Answer INCORRECTLY:\n2 + 2 = ?\n")

    answer = input("Answer: ")
    if check_cheat(answer, "Any number except 4"):
        return True
    return answer.strip() != "4"

def level_5(lives):
    header(lives, "LEVEL 5 — HUMILITY TEST")
    slow_print("Are you smart? (yes / no)\n")

    answer = input("Answer: ")
    if check_cheat(answer, "Anything except yes or no"):
        return True
    return answer.strip().lower() not in ["yes", "no"]

def level_6(lives):
    header(lives, "LEVEL 6 — PATIENCE")
    slow_print("This level has no solution.")
    slow_print("Type anything.\n")

    start = time.time()
    answer = input("Input: ")

    if check_cheat(answer, "Wait without typing"):
        return True
    return time.time() - start >= 10

# ================= ENDING =================
def ending():
    clear()
    slow_print("SYSTEM UNLOCKED\n")
    loading_bar("Decrypting truth", 1.5)
    slow_print("\nYou didn’t hack the system.")
    slow_print("You hacked your thinking.\n")
    slow_print("— WHAT THE HACK! —")
    slow_print("By Aymen Ftita\n")

# ================= MAIN =================
def main():
    title_animation()
    intro()

    lives = MAX_ATTEMPTS
    levels = [
        level_1,
        level_2,
        level_3,
        level_4,
        level_5,
        level_6
    ]

    for lvl in levels:
        while True:
            if lvl(lives):
                slow_print("\n✔ Level passed.")
                time.sleep(1)
                break
            else:
                lives -= 1
                slow_print("\n❌ Level failed.")
                if lives == 0:
                    slow_print("\n💀 GAME OVER — No attempts left.")
                    return
                time.sleep(1)

    ending()

if __name__ == "__main__":
    main()
