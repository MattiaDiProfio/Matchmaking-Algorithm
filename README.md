# A candidate-to-job matchmaking system

## Project Overview

This project aims to serve as proof-of-concept for a system capable of finding an optimal arrangement of offers between a set of jobs and a set of candidates.

The notebook attached serves as a documentation for the process undertaken to complete the task, and I suggest you follow the steps in the *Running instructions* section to gain a better understanding of the project. The main components include :

- A data prep. and visualization section using libraries such as Pandas, Seaborn and Matplotlib.
- A section dedicated to the design, implementation, and testing of a matchmaking algorithm inspired by the work of Gale-Shapley.
- An exploratory section where several machine learning algorithms such as SVMs, KNNs, Decision Trees & Random Forests, and Logistic Regression are trained and tested for the task of classifying the algorithm's output based on the probability of a computed match being turned into a successfull job offer.
- A conclusion section, where the matchmaking algorithm and SVM classifier are used in conjuction to compute and label job offers.

## Running instructions

To run the project :

- Donwload the repository and make sure that you have Anaconda Navigator installed on your machine
- Open the notebook in your editor of choice, and run each cell sequentially using the Cells > Run all option
- Get yourself some popcorns and sit back : the notebook will take a while to fully run, especially when it comes to the *Performance & Metrics Evaluation* section.
- If you encounter an error related to *ModuleNotFoudError* or similar, create a new cell and run the command ``` !pip install <package name here> ```
