# HW 4

## Assignment 1: Review of Xu Chunqing's Citibike data

## Assignment 2: Literature Choices of Statistical Tests
I worked on this assignment with Jonathan Geis. He chose the logistic regression for 
differences between groups, and I chose a chi-square analysis. The paper I read was titled *True versus False Parasite Interactions: A Robust Method to Take Risk Factors into Account and Its Application to Feline Viruses* by Eléonore Hellard, Dominique Pontier, Frank Sauvage, Hervé Poulet, David Fouchet, and can be found at http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0029618

Jonathan's article was titled *Acceptance of Home-Based Chlamydia Genital and Anorectal Testing Using Short Message Service (SMS) in Previously Tested Young People and Their Social and Sexual Networks* by Nicole H. T. M. Dukers-Muijrers,  Kevin A. T. M. Theunissen,  Petra T. Wolffs,  Gerjo Kok,  Christian J. P. A. Hoebe and can be found at http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133575

| **Statistical Analyses      | IV(s)    | IV type(s)  | DV(s)  | DV type(s) | Control Var  | Control Var type |  Question to be answered | _H0_ | alpha | link to paper** |
|:--------------:|:--------------:|:------:|:---------:|:-----------:|:-----------:|:------------:|:------------------:|:-------:|:---------:|:---------|
Chi-Square Analysis  |  Number of Viruses/Parasites in Cats; | continuous | Different combinations of status (seropositive or seronegative) for the two pathogens | discrete | N/A | N/A | Do pathogen and parasite combinations increase risk (seropositive or seronegative) of virus pairing in domestic cats? | H0: Independent viruses and pathogens are equally or less likely to synergize or double associate and pair in cats possessing multiple parasite and pathogens. | N/A | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0029618 |


| **Statistical Analyses      | IV(s)    | IV type(s)  | DV(s)  | DV type(s)  | Control Var  | Control Var type |  Question to be answered | _H0_ | alpha | link to paper** |
|:--------------:|:--------------:|:------:|:---------:|:-----------:|:-----------:|:------------:|:------------------:|:-------:|:---------:|:---------|
Logistic Regression |  previously tested positive or negative to STI, sent SMS and reminders, sent extra test kit| categorical | requested a test kit, actually re-tested, had a peer tested | categorical | n/a | n/a | Does communication by SMS increase response rate?, How does previous test result affect response?, Will they get their peers tested? | SMS communication has no effect on specimens' response    |  n/a   | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133575 |


## Assignment 3: 
Worked with Sofiya and Jonathan to complete Assignment 3. Sofiya had previously worked with Mark and Sebastian on the file, which we reviewed together as a group and then completed. 

## Assignment 4:
I worked with Jonathan and Sofiya to complete Assignment 4. I initially had some issues comparing the male and female riders because of null values in either dataframe, but eventually overcame that by creating separate dataframes for each, which I then used for correlation testing in the Pearson and Spearman tests. 
