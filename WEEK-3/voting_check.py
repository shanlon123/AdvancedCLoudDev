"""
Write a program that takes in a user’s age and determines if they are old enough to vote.
If they are, the program should ask if they are registered to vote.
 If they are registered to vote.
 The program should tell them where their polling place is.
 If they are not registered, the program should tell them how to register.


"""


def check_voting_status():
    try:
        users_age = float(input('Please enter your age in numbers e.g 18: '))
        if users_age >= 18:
            users_quest_vote = input('Are you registered to vote (please enter Yes or No: ')
            if users_quest_vote.lower() == 'yes' or users_quest_vote.lower() == 'y':
                return 'Please visit the following to check your polling unit https://goiodhjh.uk.godh'
            else:
                return 'Please visit https://kjhkjhfd.com to register to vote'
        else:
            return 'Please wait till you are 18 years old to register to vote'
    except ValueError:
        print('Error: input not a number.')

chec_status = check_voting_status()
print(chec_status)
