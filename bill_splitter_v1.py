
#!/usr/bin/env python3


# =========================
# BILL SPLITTER V1
# =========================

# author: Alex Wang

# version: 1.0

# created: 2025

# 1. App starts, runs boot FX.
# 2. App displays bill names (Rent, Hydro, etc.)
# 3. user_1 types in each amount
# 4. user_1 enters any shared costs user_2 paid
# 5. App calculates:
#    - user_1 total
#    - Split cost
#    - Minus what user_2 paid/2
#    - Special items and occasions
#    - Final amount user_2 owed 
# 6. Displays clean result:
#    ➝ [Month] user_2 owes user_1: $$$
# 7. add some fun visual FX, look like the app is thinking.
# 8. add save history function.
# 9. add confirmation for inputs to prevent typos.
# 10. add comfirmation for quitting the app.


#------------------------------------------------
# intro FX banner. title, ver, author, date.
#------------------------------------------------

# --- write several reusable funtions for visual clarity and effects. ---

import time

# make a function that displays the intro with a "type writer" effect.
def boot_intro():
    print("\n")
    print("[BOOT] ", end="", flush=True)
    time.sleep(0.5)

    for word in ["Launching", "Bill", "Splitter"]:
        time.sleep(0.08)
        print(f"{word} ", end="", flush=True)

    for dot in "...":
        time.sleep(0.5)
        print(dot, end="", flush=True)

    print("\n")
 
    print("="*36)
    time.sleep(0.2)
    print("     BILL SPLITTER V1")
    time.sleep(0.08)
    print("       version 1.0 | 2025")
    time.sleep(0.2)
    print("="*36)
    

boot_intro()

# make a function that prints a reusable divider.
def print_divider(divider):
    print("\n")
    time.sleep(0.5)
    print("-"*10, end="", flush=True)
    time.sleep(0.2)
    print(divider, end="", flush=True)
    time.sleep(0.2)
    print("-"*10, end="", flush=True)
    print("\n")


# make a function for visual clarity.
def spacing_line():
    print("\n")
    

# make a function that prints tag and fx lines.
def print_tag(tag, dialogue):
    print("\n")
    print(tag, end="", flush=True)
    time.sleep(0.5)

    for word in dialogue:
        time.sleep(0.08)
        print(f"{word} ", end="", flush=True)

    for dot in "...":
        time.sleep(0.5)
        print(dot, end="", flush=True)


# -----------------------------------------------
# get date.
# -----------------------------------------------


print_divider("[DATE INPUT]")

# global data.
user_1_total = 0
user_2_total = 0
final_amount_owed = 0


# get month and year. input accuracy confirmation.
def get_date():
    spacing_line()

    while True:
        month = input("Enter month:").upper()
        year = input("Enter year:")
        confirm = input(f"{month} {year}. Is this correct? (yes/no)").lower()
        if confirm == "yes":
            break

    spacing_line()
    print(f"{month} {year}")
    return month, year
date = get_date()
date_str = f"{date[0]}, {date[1]}"

# -----------------------------------------------
# main bills.
# -----------------------------------------------

print_divider("[RECURRING BILLS: USER_1 ENTRY]")

# make a function to prompt number inputs, preventing input error crashes when enter bill amounts.
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.Let's try again.")

# [user_1 input]-----------------------------------------------

print_tag("[BILLS]" , ["Gathering", "recurring", "bills"])

# make a functon to display recurring bill types paid by user_1 or user 2.
def get_recurring_bills(user_label):
    spacing_line()
    
    bill_names = []
    bill_dict = {}

    while True:
        name = input("Enter recurring bill name (or type 'finish' to continue):")
        if name.lower() == "finish":
            confirm = input(f"Please confirm the list of bills: {bill_names} (yes/no)").lower()
            if confirm == "yes":
                break
            else:
                bill_names.clear()
                continue    

        bill_names.append(name)

    print(f"Here are the recurring bills paid by {user_label}:")

    # display bill names.
    for index, name in enumerate(bill_names, start=1): 
        print(f"{index}.{name}", end="  ")
    spacing_line()

    # ask user_1 to input amount for each bill. amount accuracy confirmation.
    while True:
        for name in bill_names:
            amount = get_float(f"Enter the amount for {name}:")
            bill_dict[name] = amount
        confirm = input(f"{bill_dict} Is this correct? (yes/no)").lower()    
        if confirm == "yes":
            break
        else:
            bill_dict.clear()

    spacing_line()
    
    #display bill names with amount.
    for index, (name,amount) in enumerate(bill_dict.items(), start=1): 
        print(f"{index}. {name}: $ {amount}")
    

    # add up the totals. 
    spacing_line()
    total = round(sum(bill_dict.values()),2)
    print(f"The total of recurring bills paid by {user_label} is: $ {total}")
    return bill_dict, total

user_1_bills, user_1_total = get_recurring_bills("User_1")


# [user_2 input]-----------------------------------------------

# collect recurring bills that user_2 paid.
print_divider("[RECURRING BILLS: USER_2 ENTRY]")


user_2_bills, user_2_total = get_recurring_bills("User_2")


# [calculation of result]-----------------------------------------------

# calculate the split and owed amount.
owed = round((user_1_total/2) - (user_2_total/2),2)
spacing_line()
print_divider("[RECURRING BILLS TOTAL]")

print_tag("[RESULT]" , ["Calculating", "total", "amount"])
spacing_line()
print(f"User_2 owes User_1 on regular bills: \n{user_1_total}/2 - {user_2_total}/2 = $ {owed}")


# -----------------------------------------------
# special one time items.
# -----------------------------------------------

print_divider("[SPECIAL ITEMS: USER_1 ENTRY]")
print("Enter any one-time special costs you paid for the other user.")
print("Type 'yes' to add an item, or 'no' to continue.\n")

# calculate special one time items that user_1 paid or user_2 paid for each other.
def get_special_items():

    user1_paid_for_user2 = {}
    user2_paid_for_user1 = {}

    # [user_1 input]-----------------------------------------------
    # get what user_1 paid for user_2. ask if there are more items.
    while True:
        spacing_line()
        add_item = input("Add a special item? (yes/no)").lower()

        if add_item == "no":
            confirm = input(f"{user1_paid_for_user2} Is this correct? (yes/no)")
            if confirm == "yes":
                break
            else:
                user1_paid_for_user2.clear()

        elif add_item == "yes":
            user1_name = input(f"What item did User_1 pay for User_2 in {date[0]}:")
            user1_amount = get_float(f"How much for {user1_name}:")
            user1_paid_for_user2[user1_name] = user1_amount

        else:
            print("Invalid input. Please answer 'yes' or 'no'.Let's try again.")
            

    # [user_2 input]-----------------------------------------------
    # get what user_2 paid for user_1. asks to add item.
    print_divider("[SPECIAL ITEMS: USER_2 ENTRY]")
    print("Enter any one-time special costs you paid for the other user.")
    print("Type 'yes' to add an item, or 'no' to continue.\n")

    while True:
        spacing_line()
        add_user2_item = input("Add a special item from user_2? (yes/no)").lower()

        if add_user2_item == "no":
            confirm = input(f"{user2_paid_for_user1} Is this correct? (yes/no)")
            if confirm == "yes":
                break
            else:
                user2_paid_for_user1.clear()

        elif add_user2_item == "yes":
            user2_name = input(f"What item did User_2 paid for User_1 in {date[0]}:")
            user2_amount = get_float(f"How much for {user2_name}:")
            user2_paid_for_user1[user2_name] = user2_amount

        else:
            print("Invalid input. Please answer 'yes' or 'no'.Let's try again.")

    # [calculation of result]-----------------------------------------------
    # sum up all the special items data.
    print_tag("[RESULT]" , ["Calculating", "total", "amount"])

    user1_special_total = round(sum(user1_paid_for_user2.values()),2)
    user2_special_total = round(sum(user2_paid_for_user1.values()),2)

    spacing_line()
    print(f"Here're the one time items User_1 paid for User_2 in {date[0]}: \n{user1_paid_for_user2} \n Total is: $ {user1_special_total}")

    spacing_line()
    print(f"Here're the one time items User_2 paid for User_1 in {date[0]}: \n{user2_paid_for_user1} \n Total is: $ {user2_special_total}")
    return user1_special_total, user2_special_total

user1_special_total, user2_special_total = get_special_items()
spacing_line()

# -----------------------------------------------
# sum up the total of the month.
# -----------------------------------------------
print("="*40)
print_divider("[TOTAL OF THE MONTH]")


# calculate the final result for the month.
print_tag("[FINAL RESULT]" , ["Calculating", "final", "total", "amount"])
final_amount_owed = round(owed + user1_special_total - user2_special_total,2)

def final_result():
    spacing_line()
    print(f"User_2 owes User_1 after special items: \n{owed} + {user1_special_total} - {user2_special_total} = $ {final_amount_owed}")
    spacing_line()

    if final_amount_owed > 0:
        print_divider("[USER_2 OWES]")
        print(f"{date_str}, this month User_2 owes User_1: $ {final_amount_owed}")
        who_owes = "[USER_2 OWES]"

    elif final_amount_owed < 0:
        print_divider("[USER_1 OWES]")
        print(f"{date_str}, this month User_1 owes User_2: $ {final_amount_owed}")
        who_owes = "[USER_1 OWES]"

    else:
        print_divider("[EVEN SPLIT]")
        print(f"{date_str}, this month is even.")
        who_owes = "[EVEN SPLIT]"

    return who_owes, final_amount_owed

who_owes, final_amount_owed = final_result()

spacing_line()
print("="*40)
spacing_line()

# -------------------------------------------------------
# add save history function. ask to save, and close app.
# -------------------------------------------------------

# make a function to save history. date, user_1_total, user_2_total, owed, user1_special_total, user2_special_total, final_amount_owed.
# make sure it is at the same spot with the app.

import os

def save_history():

    app_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(app_dir, "bill_splitter_history.txt")

    with open (file_path, "a", encoding = "utf-8") as save:

        log = f"""
        {date_str}
        User_1 bill total is: {user_1_total}
        User_2 bill total is: {user_2_total}
        Total bill owed is: {owed}
        User_1 special total is: {user1_special_total}
        User_2 special total is: {user2_special_total}
        Final result for {date[0]} is: {who_owes} | Amount: ${final_amount_owed}
        """    
        save.write(log)
    
# make a function to ask permission to close window.
def end_session():
    print("\n" + "="*40)
    input("\n[SESSION COMPLETED] Press Enter to exit Bill Splitter...")

# ask to save or exit.
confirm_save = input("Save history? (yes/no)").lower()
if confirm_save == "yes":
    save_history()
    end_session()
else:
    end_session() 


