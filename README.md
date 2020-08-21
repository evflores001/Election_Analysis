# Election_Analysis
## Project Overview
A Colorado Board of Elections employee has given us a series of tasks to complete an election audit for a local congressional election.

1. Get the total number of votes in the election
2. Get a list of the candidates and a list of each distinguishable county
3. Keep track of the number of votes each candidate received
4. Keep track of the number of votes for each county
5. Calculate the percentage the each candidate and county had out of the total votes
6. Determine the winner based on popular vote
7. Determine the county with the highest turnout

## Resources
Data Source: election_results.csv
Software: Python 3.7.6, Visual Studio Code, 1.48.0

## Results
The analysis of our results show that:
- There are 369,711 votes
- The total number of votes and percentage from the total number of votes for each county are as follows:
    - Jefferson County had 10.5% of votes having 38,855 votes
    - Denver County had 82.8% of votes with 306,055 votes
    - Arapahoe County had the least number of votes with 6.7% and 24,801 votes
- The county with the most votes was Denver.
- The total number of votes and percentage from the total for each candidate are as follows:
    - Charles Casper Stockham had 23.0% of votes, a total of 85,213 votes
    - Diana DeGette had 73.8% of votes with 272,892 votes
    - Raymon Anthony Doane had 3.1% of votes with a total of 11,606 votes
- The results of the winning candidate
    - Diane Degette won the election by popular vote with 272,892 votes, 73.8% of the total number of votes
    
We can see the results from the following image obtained from the election_results.txt file:

## Summary
The results obtained from our Python program allowed us to complete the election audit fairly easy without having to manually iterate through each row of the election_results.csv file. Although our code was able to tackle this fairly large CSV file, with some modifications we could increase its ability to handle multiple files as well as give us more insight into vote allocation from each county. Using Python's merge functions, we could merge multiple CSV files, which would allow us to audit larger elections. Using a combination of dual alternative decision statements, condition controlled loops and logical operators, we could keep track of the number of votes and percentages of votes each county allocated to each candidate, giving us a breakdown of how each candidate fared within each county. 
