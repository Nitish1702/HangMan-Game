from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


root = Tk()
root.config(bg='cyan')
root.title('Hangman-GUESS COUNTRY NAME')
w_list = ['Afghanistan', 'Aland Islands', 'Albania',
             'Algeria', 'American Samoa', 'Andorra', 'Angola',
             'Anguilla', 'Antarctica', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
             'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
             'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan',
             'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba',
             'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'Brunei Darussalam', 'Bulgaria',
            'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
            'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China',
            'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo',
            'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire",
            'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
            'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
            'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
            'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
            'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
             'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)',
             'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq',
             'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya',
             'Kiribati', "Korea", 'Kuwait',
            'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
            'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands',
            'Somalia', 'South Africa',  'Spain', 'Sri Lanka', 'Sudan',
            'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
            'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau',
            'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu',
             'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands',
            'Uruguay', 'Uzbekistan',
            'Venezuela, Bolivarian Republic of', 'Viet Nam',
             'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(
              file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"), PhotoImage(
              file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]


def reset():
    global word
    global numberOfGuesses
    numberOfGuesses = 0

    the_word = random.choice(w_list)
    word = " ".join(the_word)
    wordlabel.set(' '.join("_"*len(the_word)))


def guess(letter):
    global numberOfGuesses
    if numberOfGuesses < 11:
        txt = list(word)
        guessed = list(wordlabel.get())
        if word.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
                wordlabel.set("".join(guessed))
                if wordlabel.get() == word:
                    messagebox.showinfo("Hangman", "You guessed it!")
        else:
            numberOfGuesses += 1
            imgLabel.config(image=photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman", "Game Over")


imgLabel = Label(root)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)


wordlabel = StringVar()
Label(root, textvariable=wordlabel, font=('Arial')).grid(
    row=0, column=3, columnspan=6, padx=10)

n = 0
for c in ascii_uppercase:
    Button(root, text=c, command=lambda c=c: guess(c), font=(
        'Helvetica 18'), fg='red', width=4).grid(row=1+n//9, column=n % 9)
    n += 1

Button(root, text="New\nGame", command=lambda: reset(),
       font=("Helvetica 10 bold")).grid(row=3, column=8)

reset()
root.mainloop()
