from twilio.rest import Client

account_sid = 'ACa92e1908b4091f16296fce610afd6338'
auth_token = '9d686ac70aa25a9874b44694f0d04d1e'
my_cell = '+17205561310'
twilio_number = '+14357740352'

client = Client(account_sid, auth_token)

user_input = input("Welcome to music suggestor! Reply with your preferred genre: 'Rap', 'Alternative', or 'Pop': ")

if user_input == 'Rap':
    user_input = input("Which artist is your favorite: 'Drake', 'Kanye West', or 'Wu-Tang Clan' ? (Inputs are case sensitive): ")

    if user_input == 'Drake':
        print("Your preferred artist was Drake. We think you will like Future! We'll send you a text with a link to his Spotify page :)")
        message = client.messages.create(body="Future on Spotify: https://open.spotify.com/artist/6TiNbcfVoO3SppeLYJbnSr", from_=twilio_number, to=my_cell)

    if user_input == 'Kanye West':
        print("Your preferred artist was Kanye West. We think you will like Kid Cudi! We'll send you a text with a link to his Spotify page :)")
        message = client.messages.create(body="Kid Cudi on Spotify: https://open.spotify.com/artist/0fA0VVWsXO9YnASrzqfmYu", from_=twilio_number, to=my_cell)

    if user_input == 'Wu-Tang Clan':
        print("Your preferred artist was Wu-Tang Clan. We think you will like N.W.A.! We'll send you a text with a link to their Spotify page :)")
        message = client.messages.create(body="N.W.A. on Spotify: https://open.spotify.com/artist/4EnEZVjo3w1cwcQYePccay", from_=twilio_number, to=my_cell)

if user_input == 'Alternative':
    user_input = input("Which artist is your favorite: 'Tame Impala', 'Cage the Elephant', or 'Red Hot Chili Peppers' ? (Inputs are case sensitive): ")

    if user_input == 'Tame Impala':
        print("Your preferred artist was Tame Impala. We think you will like Still Woozy! We'll send you a text with a link to his Spotify page :)")
        message = client.messages.create(body="Still Woozy on Spotify: https://open.spotify.com/artist/4iMO20EPodreIaEl8qW66y", from_=twilio_number, to=my_cell)

    if user_input == 'Cage the Elephant':
        print("Your preferred artist was Cage the Elephant. We think you will like Arctic Monkeys! We'll send you a text with a link to their Spotify page :)")
        message = client.messages.create(body="Arcitc Monkeys on Spotify: https://open.spotify.com/artist/7Ln80lUS6He07XvHI8qqHH", from_=twilio_number, to=my_cell)

    if user_input == 'Red Hot Chili Peppers':
        print("Your preferred artist was Red Hot Chili Peppers. We think you will like Kings of Leon! We'll send you a text with a link to their Spotify page :)")
        message = client.messages.create(body="Kings of Leon on Spotify: https://open.spotify.com/artist/2qk9voo8llSGYcZ6xrBzKx", from_=twilio_number, to=my_cell)

if user_input == 'Pop':
    user_input = input("Which artist is your favorite: 'Harry Styles', 'Ariana Grande', or 'Bruno Mars' ? (Inputs are case sensitive): ")

    if user_input == 'Harry Styles':
        print("Your preferred artist was Harry Styles. We think you will like John Mayer! We'll send you a text with a link to his Spotify page :)")
        message = client.messages.create(body="John Mayer on Spotify: https://open.spotify.com/artist/0hEurMDQu99nJRq8pTxO14", from_=twilio_number, to=my_cell)

    if user_input == 'Ariana Grande':
        print("Your preferred artist was Ariana Grande. We think you will like Rihanna! We'll send you a text with a link to her Spotify page :)")
        message = client.messages.create(body="Rihanna on Spotify: https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H", from_=twilio_number, to=my_cell)

    if user_input == 'Bruno Mars':
        print("Your preferred artist was Drake. We think you will like Charlie Puth! We'll send you a text with a link to his Spotify page :)")
        message = client.messages.create(body="Charlie Puth on Spotify: https://open.spotify.com/artist/6VuMaDnrHyPL1p4EHjYLi7", from_=twilio_number, to=my_cell)
