# anime_boy.py
# Scalable anime-style boy drawn using only loops and print()
# Run: python3 anime_boy.py

def safe_int_input(prompt):
    try:
        x = int(input(prompt).strip())
        if x < 3:
            print("Minimum size is 3, using 3.")
            return 3
        return x
    except:
        print("Invalid input, using 4.")
        return 4

n = safe_int_input("Enter size (number of stars, e.g. 3..10): ")

# We'll compute some dimensions relative to n
head_w = n * 2 + 1        # width of face area
hair_extra = n // 2 + 1
eye_gap = max(1, n - 2)
torso_w = head_w + n      # torso wider than head
arm_length = n + 1
torso_h = n + 1
leg_h = n
foot_w = n + 1

# Helper: print centered block with total width for alignment
total_width = torso_w + arm_length * 2 + 6  # overall canvas width (approx)

def center(s):
    # center string s in total_width by leading spaces
    lead = (total_width - len(s)) // 2
    if lead < 0: lead = 0
    return " " * lead + s

# 1) Hair (spiky, a couple of rows)
for r in range(hair_extra):
    # create spikes using alternating star groups
    spikes = ""
    for i in range(head_w):
        if (i + r) % 3 == 0:
            spikes += "*"
        else:
            spikes += " "
    print(center(spikes.rstrip()))

# 2) Top of head (rounded)
for i in range(1):
    print(center(" " + "*" * head_w + " "))

# 3) Face rows: eyes, nose, mouth (use loops to print each row)
# eyes row
left_eye = "*"
right_eye = "*"
eyes = "*" + " " * 2 + left_eye + " " * eye_gap + right_eye + " " * 2 + "*"
# pad eyes to head_w
pad = (head_w - len(eyes)) // 2
eyes_line = "*" + " " * pad + eyes + " " * (head_w - len(eyes) - pad) + "*"
print(center(eyes_line))

# nose row
nose_space = (head_w - 1) // 2
print(center("*" + " " * nose_space + "^" + " " * (head_w - nose_space - 1) + "*"))

# mouth row (smile)
mouth_len = max(1, n)
mouth = " " + "_" * mouth_len + " "
pad = (head_w - len(mouth)) // 2
print(center("*" + " " * pad + mouth + " " * (head_w - len(mouth) - pad) + "*"))

# chin / bottom of head
print(center(" " + "*" * head_w + " "))

# 4) neck (two rows)
for i in range(2):
    print(center(" " * (head_w//2) + "*" * 1))

# 5) Shoulders and connected arms (one or two rows to show sleeves)
# We'll draw lines where arms extend out left/right and connect to torso
for r in range(2):
    left_arm = "*" + " " * (arm_length - r)  # slightly angled
    right_arm = " " * (arm_length - r) + "*"
    torso_block = "*" * torso_w
    line = left_arm + " " * 2 + torso_block + " " * 2 + right_arm
    print(center(line))

# 6) Torso (several rows)
for i in range(torso_h):
    # we can add a shirt pattern in middle using alternating stars
    if i % 2 == 0:
        shirt = "*" * torso_w
    else:
        # small gap stripes
        shirt = "*" + " " * (torso_w - 2) + "*"
    print(center(" " * 2 + shirt + " " * 2))

# 7) Waist narrowing
print(center(" " * (arm_length + 2) + "*" * (torso_w - n)))

# 8) Legs (two vertical columns, separated)
leg_gap = 3
for i in range(leg_h):
    left = "*" 
    right = "*"
    body = " " * (arm_length + 2)  # left padding to align under torso
    middle = " " * ((torso_w - 2) // 2)
    # place left leg and right leg with some gap
    line = body + " " * ( (torso_w//2) - leg_gap ) + left + " " * (leg_gap*2) + right
    print(center(line))

# 9) Feet
feet_line = " " * (arm_length + 2 + (torso_w//2) - leg_gap - 1) + "*" * foot_w + " " * 4 + "*" * foot_w
print(center(feet_line))

# 10) Small flourish / optional accessory (a small star near head like a hair spike)
print()  # blank line
print(center("  " + "*" * 1 + "  (you can increase n for bigger boy)"))
