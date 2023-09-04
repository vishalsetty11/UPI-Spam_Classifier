'spam-detection.ipynb' access an dataset that has been stored in 'spam.csv'. 
The dataset contains a list of UPI IDs which are declared as spam and not spam.

Using the command 'import matplotlib.pyplot as plt
plt.pie(df['Target'].value_counts(),labels=['ham','spam'],autopct="%0.2f")'
We came to a conclusion that there are 67.37 genuine UPI IDs and 32.63 Fraudulent UPI IDs.
