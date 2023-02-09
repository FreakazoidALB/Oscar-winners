import pandas as pd

# Read the CSV file into a DataFrame
oscars_df = pd.read_csv('oscars.csv')


# Convert the values in the 'Year' column to integers
oscars_df['Year'] = oscars_df['Year'].astype(int)

# Ask the user for the year
year = int(input("Enter the year of the Oscars: "))


# Filter the DataFrame to only include the winner for the specified year
winner_df = oscars_df[oscars_df['Year'] == year]


# Get the winner's name, birth year, birthplace, and movie name
name = winner_df['Name'].iloc[0]
age = winner_df['Age'].iloc[0]
birthplace = winner_df['Birthplace'].iloc[0]
gender = winner_df['Gender'].iloc[0]
movie = winner_df['Movie'].iloc[0]


# Determine the correct pronoun to use based on the winner's gender
if gender == 'Male':
    pronoun = 'He'
else:
    pronoun = 'She'

# Display the winner's information
print("The winner of the Oscar for Best Actor in " + str(year) + " was " + name + ".")
print(pronoun + " was born in " + birthplace + " and won the award for their performance in " + movie + ".")
print("At the time " + pronoun + " won the award, " + pronoun + " was " + str(age) + " years old.")
