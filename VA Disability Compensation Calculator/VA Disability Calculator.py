#Zhada Eaves
#No collaborators

#PSEUDOCODE
#This Python program calculates the Veteran's disability compensation including
    #the financial compensation plus benefits (such as dental service)
#Create dictionaries for 2024 financial compensation rates
#Include any additional compensation per child
#Create a dictionary for additional benefits that are not monetary
#Prompt the user to input the number of dependent child,
    #dependent parents, and if he or she has a spouse
#If the user inputs rating 0, 10, or 20, display the benefits and calculations.
#Ask the user if they would like to learn more about the benefits on my blog post or input another rating.
#Ratings of 0, 10, or 20 have flat rates and benefits. They do not change.
#Display the calculated financial compensation rate along with benefits
#Redirect the user to my blog post about how to file a VA Disability Claim

#---VA Calculator---
#Create a dictionary for 2024 compensation rates
compensation_table = {
    "Veteran. No spouse or dependents": {0:0, 10: 171.23, 20:338.49, 30:524.31, 40: 755.28, 50: 1075.16, 60:1361.88,
                                         70:1716.28, 80:1995.01, 90:2241.91, 100:3737.85},
    "Veteran with spouse(no parents or children)": {0:0, 10:171.23, 20:338.49, 30:586.31, 40:838.28, 50:1179.16, 60: 1361.88,
                                                    70: 1861.28, 80:2161.01, 90:2428.91, 100:3946.25},
    "Veteran with 1 child only (no spouse or parents)": {0: 0, 10: 171.23, 20: 338.49,30:565.31, 40:810.28, 50:1144.16, 60:1444.28,
                                                   70:1813.28, 80:2106.01, 90:2366.91, 100:3877.22},
    "Veteran with 1 child and spouse (no parents)": {0: 0, 10:171.23, 20:338.49,30:632.31, 40:899.28, 50:1255.16, 60:1577.88,
                                                     70:1968.28, 80:2283.01, 90:2565.91, 100:4098.87},
    "Veteran with 1 child, spouse, and 1 parent": {0: 0, 10: 171.23, 20:338.49,30:682.31, 40:965.28, 50:1338.16, 60:1677.88,
                                                   70:2085.28, 80:2416.01, 90:2715.91, 100:4266.13},
    "Veteran with 1 child, spouse, and 2 parents": {0: 0, 10: 171.23, 20:338.49, 30:732.31, 40:1031.28, 50: 1421.16, 60:1777.88,
                                                    70:2202.28, 80:2549.01, 90:2865.91, 100:4433.39},
    "Veteran with 1 child and 1 parent (no spouse)": {0: 0, 10: 171.23, 20:338.49, 30:615.31, 40:876.28, 50:1227.16, 60:1544.88,
                                                      70:1930.28, 80:2239.01, 90:2516.91, 100:4044.48},
    "Veteran with 1 child and 2 parents (no spouse)": {0:0, 10: 171.23, 20:338.49,30:665.31, 40:942.28, 50:1310.16, 60:1644.88,
                                                       70:2047.28, 80:2372.01, 90:2666.91, 100:4211.74},
    "Veteran with spouse and 1 parent": {0: 0, 10: 171.23, 20: 338.49, 30: 636.31, 40: 904.28, 50:1262.16, 60: 1586.88,
                                         70: 1978.28, 80:2294.01, 90:2578.91, 100:4113.51},
    "Veteran with spouse and 2 parents": {0: 0, 10: 171.23, 20: 338.49, 30:686.31, 40:970.28, 50:1345.16, 60:1686.88,
                                          70:2095.28, 80:2427.01, 90:2728.91, 100:4280.77},
    "Veteran with 1 parent (no spouse or children)": {0: 0, 10: 171.23, 20: 338.49, 30:574.31, 40:821.28, 50:1158.16, 60:1461.88,
                                                      70:1833.28, 80:2128.01, 90:2391.91, 100:3905.11},
    "Veteran with 2 parents (no spouse or children)": {0: 0, 10: 171.23, 20: 338.49,30:624.31, 40:887.28, 50:1241.16, 60:1561.88,
                                                       70:1950.28, 80:2261.01, 90:2541.91, 100:4072.37}
    }


#Create a dictionary for the compensation per child
additional_compensation ={
    "Each additional child under the age of 18": {30:31.00, 40:41.00, 50:51.00, 60:62.00, 70:72.00, 80:82.00, 90:93.00, 100:103.55},
    "Each additional child over the age of 18 in a qualifying school program": {30:100.00, 40:133.00, 50:167.00, 60:200.00, 70:234.00, 80:267.00, 90:301.00, 100:334.49},
    "Spouse receiving aid and attendance": {30:57.00, 40:76.00, 50:95.00, 60:114.00, 70:134.00, 80:153.00, 90:172.00, 100:191.14}
    }


#Finally, create a dictionary for additional benefits based on disability rating (not financial)
additional_benefits = {
    0: [
        "10 point Veteran preference in federal hiring",
        "No cost health care and prescription drugs for service connected disabilities (if income limits are met)",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    10: [
        "No cost health care",
        "Prescription medications for service connected disabilities",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Vocational Rehabilitation & Employment (with a serious employment handicap)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    20: [
        "No cost health care",
        "Prescription medications for service connected disabilities",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Vocational Rehabilitation & Employment",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    30: [
        "No cost health care",
        "Prescription medications for service connected disabilities",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouse)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    40: [
        "No cost health care",
        "Prescription medications for service connected disabilities",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouse)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    50: [
        "No cost health care and prescription medications",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouses)",
        "Concurrent receipt of military retired pay",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    60: [
        "No cost health care and prescription medications",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouses)",
        "Concurrent receipt of military retired pay",
        "Individual Unemployability (must be unemployable due to service connected disabilities)",
        "Dependents Educational Assistance (unemployable condition must be considered permanent)",
        "Special restorative training",
        "CHAMPVA–Civilian Health and Medical Program (unemployable condition must be considered permanent)",
        "Dental care (if rated unemployable)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    70: [
        "No cost health care and prescription medications",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouses)",
        "Concurrent receipt of military retired pay",
        "Individual Unemployability (must be unemployable due to service connected disabilities)",
        "Dependents Educational Assistance (unemployable condition must be considered permanent)",
        "Special restorative training",
        "CHAMPVA–Civilian Health and Medical Program (unemployable condition must be considered permanent)",
        "Dental care (if rated unemployable)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    80: [
        "No cost health care and prescription medications",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouses)",
        "Concurrent receipt of military retired pay",
        "Individual Unemployability (must be unemployable due to service connected disabilities)",
        "Dependents Educational Assistance (unemployable condition must be considered permanent)",
        "Special restorative training",
        "CHAMPVA–Civilian Health and Medical Program (unemployable condition must be considered permanent)",
        "Dental care (if rated unemployable)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    90: [
        "No cost health care and prescription medications",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouses)",
        "Concurrent receipt of military retired pay",
        "Individual Unemployability (must be unemployable due to service connected disabilities)",
        "Dependents Educational Assistance (unemployable condition must be considered permanent)",
        "Special restorative training",
        "CHAMPVA–Civilian Health and Medical Program (unemployable condition must be considered permanent)",
        "Dental care (if rated unemployable)",
        "Burial and plot allowance",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ],
    100: [
        "No cost health care and prescription medications",
        "Travel allowance for scheduled appointments for care at a VA medical facility or VA authorized health care facility",
        "No cost dental care",
        "Waiver of VA funding fee for home loan",
        "10 point Veteran preference in federal hiring",
        "Direct hire authority",
        "Vocational Rehabilitation & Employment",
        "Additional compensation for eligible dependents (may include aid and attendance for eligible spouses)",
        "Concurrent receipt of military retired pay",
        "Dependents Education Assistance (must be considered permanent)",
        "Special restorative training",
        "CHAMPVA–Civilian Health and Medical Program (must be considered permanent)",
        "Burial and plot allowance",
        "Uniformed Services ID card",
        "Commissary and Exchange Privileges (Use of commissaries, exchanges, and morale, welfare and recreation (MWR) retail facilities, in-person and online)"
    ]
}


#Create a function to calculate VA Compensation
def calculate_va_compensation(rating, children_under_18=0, children_over_18=0, has_spouse=False, spouse_needs_aid=False, parents=0):
    #Determine compensation using base_keys
    if children_under_18 > 0 or children_over_18 > 0:
        if has_spouse:
            if parents == 1:
                base_key = "Veteran with 1 child, spouse, and 1 parent"
            elif parents == 2:
                base_key = "Veteran with 1 child, spouse, and 2 parents"
            else:
                base_key = "Veteran with 1 child and spouse (no parents)"
        else:
            if parents == 1:
                base_key = "Veteran with 1 child and 1 parent (no spouse)"
            elif parents == 2:
                base_key = "Veteran with 1 child and 2 parents (no spouse)"
            else:
                base_key = "Veteran with 1 child only (no spouse or parents)"
    elif has_spouse:
        if parents == 1:
            base_key = "Veteran with spouse and 1 parent"
        elif parents == 2:
            base_key = "Veteran with spouse and 2 parents"
        else:
            base_key = "Veteran with spouse(no parents or children)"
    else:
        if parents == 1:
            base_key = "Veteran with 1 parent (no spouse or children)"
        elif parents == 2:
            base_key = "Veteran with 2 parents (no spouse or children)"
        else:
            base_key = "Veteran. No spouse or dependents"

    #Base compensation
    base_comp = compensation_table.get(base_key, {}).get(rating, 0)

    #Define base child compensation
    child_comp = 0

    #Add additional compensation for each additional child (excluding the first)
    if children_under_18 > 1:
        child_comp += (children_under_18 - 1) * additional_compensation["Each additional child under the age of 18"].get(rating, 0)
    if children_over_18 > 1:
        child_comp += (children_over_18 - 1) * additional_compensation["Each additional child over the age of 18 in a qualifying school program"].get(rating, 0)


    #Additional compensation for spouse requiring aid
    spouse_comp = additional_compensation["Spouse receiving aid and attendance"].get(rating, 0) if has_spouse and spouse_needs_aid else 0

    #Total compensation
    total_comp = base_comp + child_comp + spouse_comp

    return total_comp

#Function to display additional benefits
def display_benefits(rating):
    benefits = additional_benefits.get(rating, [])
    if benefits:
        print(f"Additional benefits for {rating}% rating:")
        for benefit in benefits:
            print(f"- {benefit}")
    else:
        print("No additional benefits available.")


#Main function
def main():
    #Create a loop
       while True:
        #Prompt user to input rating and other details with error handling
        while True:
            try:
                rating = int(input("What is your disability rating (Example: 30)? "))
                break  #Exit loop if valid input
            except ValueError:
                print("Please enter a valid number for the disability rating. (Example: 0 or 80)")

        has_spouse = input("Do you have a spouse? (yes/no): ").lower() == "yes"
        
        while True:
            try:
                children_under_18 = int(input("How many dependent children UNDER the age of 18 do you have? "))
                break
            except ValueError:
                print("Please enter a valid number for children under 18. (Example: 2)")

        while True:
            try:
                children_over_18 = int(input("How many dependent children OVER the age of 18 do you have? "))
                break
            except ValueError:
                print("Please enter a valid number for children over 18. (Example: 0)")

        while True:
            try:
                parents = int(input("How many of your parents depend on you (0, 1, 2)? "))
                if parents not in [0, 1, 2]:
                    raise ValueError  #Ensure only 0, 1, or 2 is allowed
                break
            except ValueError:
                print("Please enter 0, 1, or 2 for the number of dependent parents. (The VA does not calculate more than 2.)")

        aid_attendance = input("Does your spouse require Aid & Attendance? (yes/no): ").lower() == "yes"
   

        #Calculate and display the result
        monthly_compensation = calculate_va_compensation(rating, children_under_18, children_over_18, has_spouse, aid_attendance, parents)
        print(f"\nYour estimated monthly VA compensation is: ${monthly_compensation:,.2f}")

        print("\n")
        #Display additional benefits
        display_benefits(rating)
    
        blog_link = "https://www.zhadaray.com/post/va-disability-guide"
        #Allow the user to choose whether to enter another rating or read my blog post
        next_action = input("\nWould you like to input another rating or learn more about filing a VA disbility claim? (another/learn more): ").lower()

        if next_action == "learn more":
            print(f"\nGreat! You can learn more about VA disability compensation and claims here: {blog_link}")
        elif next_action == "another":
            continue  #Restart the loop
        else:
            print("\nThank you for using the VA Disability Calculator! I hope it helped.")
        break


#Call the program
if __name__ == "__main__":
    main()


