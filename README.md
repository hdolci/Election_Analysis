# Election Analysis

## Project Overview
Using mock data of a local election in Colorado, I will use Python to determine the following information:

* Calculate the total number of votes casted
* Generate a complete list of candidates that received votes
* Calculate the total number of votes each candidate received
* Calculate the percentage of votes each candidate received
* Determine the winner of the election

## Resources
* election_results.csv
* Software used: Python (ver. 3.9.5), VS Code (ver 1.57.1)

## Summary of results

Total Votes: 369,711

Charles Casper Stockham: received 85,033 (23.0%) of the vote.
<br>Diana DeGette: received  272,892 (73.8%) of the vote.
<br>Raymon Anthony Doane: received 11,786 (3.1%) of the vote.
 
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

# Election Analysis Audit
## Overview of Election Audit:

In addition to the previous calculations, we wanted to also find out which county had the largest turn out, the number of votes from this county, and the percentage of votes. This information is helpful for future candidates to see where they should focus their efforts on in a future election.

## Election-Audit Results: 
* How many votes were cast in this congressional election?
  * 369,711
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
* Which county had the largest number of votes?
  * Denver: 82.8% (306,055)
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  * Charles Casper Stockham: received 85,033 (23.0%) of the vote.
  * Diana DeGette: received  272,892 (73.8%) of the vote.
  * Raymon Anthony Doane: received 11,786 (3.1%) of the vote.
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  * Winner: Diana DeGette
  * Winning Vote Count: 272,892
  * Winning Percentage: 73.8%


## Election-Audit Summary: 

As demonstrated, the script can be used to quickly identify the winner of an election as well how the votes were casted by county. For future elections, if additional data is needed such as voter age or political party, this script can easily be modified to also provide the count of any additional data point. We can also modify this script to automatically refresh after it runs which is very useful when it is for a high profile election and the script can deliver the latest vote count at any time interval desired(great for websites to report live results).




