text = 'I travelled for two years in Tibet, therefore, and amused myself by visiting Lhassa, and spending some days with the head lama. You may have read of the remarkable explorations of a Norwegian named Sigerson, but I am sure that it never occurred to you that you were receiving news of your friend. I then passed through Persia, looked in at Mecca, and paid a short but interesting visit to the Khalifa at Khartoum the results of which I have communicated to the Foreign Office. Returning to France, I spent some months in a research into the coal-tar derivatives, which I conducted in a laboratory at Montpellier, in the south of France. Having concluded this to my satisfaction and learning that only one of my enemies was now left in London, I was about to return when my movements were hastened by the news of this very remarkable Park Lane Mystery, which not only appealed to me by its own merits, but which seemed to offer some most peculiar personal opportunities. I came over at once to London, called in my own person at Baker Street, threw Mrs. Hudson into violent hysterics, and found that Mycroft had preserved my rooms and my papers exactly as they had always been.'

# Step 1 remove periods
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace('-', ' ')

text = text.lower()

list_of_words = text.split()

n = list_of_words.count('the')
print(n)
