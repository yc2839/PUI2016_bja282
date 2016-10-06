# HW 4

## Assignment 1: Review of Xu Chunqing's Citibike data

## Assignment 2: Literature Choices of Statistical Tests
I worked on this assignment with Jonathan Geis. He chose the logistic regression for 
differences between groups, and I chose a chi-square analysis. The research paper for the latter
is *True versus False Parasite Interactions: A Robust Method to Take Risk Factors into Account and Its Application to Feline Viruses* by 
    
    Eléonore Hellard,
    Dominique Pontier,
    Frank Sauvage,
    Hervé Poulet,
    David Fouchet, and can be found at http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0029618

| **Statistical Analyses      | IV(s)    | IV type(s)  | DV(s)  | DV type(s) |  Question to be answered | _H0_ | link to paper** |
|:--------------:|:--------------:|:------:|:---------:|:-----------:|:-----------:|:------------:|:------------------:|:-------:|:---------:|:---------|
Chi-Square Analysis  |  Number of Viruses/Parasites in Cats; | continuous | Different combinations of status (seropositive or seronegative) for the two pathogens | discrete | Do pathogen and parasite combinations increase risk (seropositive or seronegative) of virus pairing in domestic cats? | H0: Independent viruses and pathogens are equally or less likely to synergize or double associate and pair in cats possessing multiple parasite and pathogens. | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0029618 |
| **Statistical Analyses      | IV(s)    | IV type(s)  | DV(s)  | DV type(s)  | Control Var  | Control Var type |  Question to be answered | _H0_ | alpha | link to paper** |
|:--------------:|:--------------:|:------:|:---------:|:-----------:|:-----------:|:------------:|:------------------:|:-------:|:---------:|:---------|
Logistic Regression |  previously tested positive or negative to STI, sent SMS and reminders, sent extra test kit| categorical | requested a test kit, actually re-tested, had a peer tested | categorical | n/a | n/a | Does communication by SMS increase response rate?, How does previous test result affect response?, Will they get their peers tested? | SMS communication has no effect on specimens' response    |  n/a   | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0133575 |
