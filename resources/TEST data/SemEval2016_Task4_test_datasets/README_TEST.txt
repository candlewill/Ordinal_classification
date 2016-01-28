******************************************************
* SemEval-2016 Task 4: Sentiment Analysis on Twitter *
*                                                    *
*               TEST datasets (input)                *
*                                                    *
* http://alt.qcri.org/semeval2016/task4/             *
* semevaltweet@googlegroups.com                      *
*                                                    *
******************************************************

Version 1.0: January 15, 2016

Task organizers:

Preslav Nakov, Qatar Computing Research Institute, HBKU
Alan Ritter, The Ohio State University
Sara Rosenthal, Columbia University
Fabrizio Sebastiani, Qatar Computing Research Institute, HBKU
Veselin Stoyanov, Facebook


NOTE

Please note that by downloading the Twitter data you agree to abide
by the Twitter terms of service (https://twitter.com/tos),
and in particular you agree not to redistribute the data.



CONTENTS OF THIS DISTRIBUTION

- README_TEST.txt -- this file

- SUBMISSION_DESCRIPTION_TEMPLATE.txt -- template for describing the submitted runs

- SemEval2016-task4-test.subtask-A.txt -- test input for subtask A

- SemEval2016-task4-test.subtask-BCDE.txt -- test input for subtasks B, C, D, and E. 

NOTE: For subtask B, neutrals were excluded from TRAIN, DEV, and DEVTEST, and we should have excluded them now from TEST as well. However, we cannot do this in advance without leaking information that would help subtasks C and E. Thus, the TEST input for subtask B uses the same input as C, D and E, but at scoring time, we will ignore the predictions for test tweets that were annotated as neutral in GOLD.


IMPORTANT

In order to use these test datasets, the participants need (1), 
and most likely also (2) and (3):

1. the official scorers and format checkers
2. the TRAIN, DEV and DEVTEST datasets for 2016
3. test datasets from previous years (CANNOT BE USED FOR TRAINING OR TUNING; CAN BE USED FOR DEVELOPMENT TIME TESTING ONLY): (i) Twitter-2013, (ii) SMS-2013 messages, (iii) Twitter-2014, (iv) Twitter-2014-sarcasm, (v) Live Journal-2014, and (vi) Twitter-2015

You can find links to them here:

	http://alt.qcri.org/semeval2016/task4/index.php?id=data-and-tools

The format checkers released should be used to check the output before submitting the results.


INPUT DATA FORMAT


-----------------------SUBTASK A-----------------------------------------

--Test Data--
The format for the test input file is as follows:

	id<TAB>UNKNOWN<TAB>tweet_text

for example:

	1       UNKNOWN  amoure wins oscar
	2       UNKNOWN  who's a master brogramer now?

--System Output--
We expect the following format for the prediction file:

	id<TAB>predicted_sentiment_4_tweet

where predicted_sentiment_4_tweet can be 'positive', 'neutral' or 'negative'.

For example:
1        positive
2        neutral


-----------------------SUBTASK B-----------------------------------------

--Test Data--
The format for the test input file is as follows:

	id<TAB>topic<TAB>UNKNOWN<TAB>tweet_text

for example:

	1      aaron rodgers       UNKNOWN       I just cut a 25 second audio clip of Aaron Rodgers talking about Jordy Nelson's grandma's pies. Happy Thursday.
	2      aaron rodgers       UNKNOWN       Tough loss for the Dolphins last Sunday in Miami against Aaron Rodgers &amp; the Green Bay Packers: 27-24.

--System Output--
We expect the following format for the prediction file:

	topic<TAB>predicted_sentiment_4_topic

where predicted_sentiment_4_topic can be "positive" or "negative" (NOTE: no "neutral"!)

For example:
	1      aaron rodgers       positive
	2      aaron rodgers       negative


-----------------------SUBTASK C-----------------------------------------
--Test Data--
Same as for subtask B.

--System Output--
We expect the following format for the prediction file:

	id<TAB>topic<TAB>predicted_sentiment_4_topic

where predicted_sentiment_4_topic can be -2, -1, 0, 1, or 2.

For example:
	1      aaron rodgers       1
	2      aaron rodgers       0


-----------------------SUBTASK D-----------------------------------------
--Test Data--
Same as for subtask B.

--System Output--
We expect the following format for the prediction file:

	topic<TAB>part_positive<TAB>part_negative

where part_positive and part_negative are floating point numbers between 0.0 and 1.0, and part_positive + part_negative == 1.0

For example:
	aaron rodgers       0.7       0.3
	peter pan           0.9       0.1


-----------------------SUBTASK E-----------------------------------------
--Test Data--
Same as for subtask B.

--System Output--
We expect the following format for the prediction file:

	topic<TAB>label-2<TAB>label-1<TAB>label0<TAB>label1<TAB>label2

where label-2 to label2 are floating point numbers between 0.0 and 1.0, and the five numbers sum to 1.0. label-2 corresponds to the fraction of tweets labeled as -2 in the data and so on.

For example:
	aaron rodgers       0.025 0.325   0.5    0.1 0.05
	peter pan           0.05  0.40    0.5    0.05 0.0

-------------------------------------------------------------------------


EVALUATION

There are different evaluation measures for the different subtasks. A detailed description can be found here:

	http://alt.qcri.org/semeval2016/task4/data/uploads/eval.pdf

See also the scorers for details on scoring the output:
	
	http://alt.qcri.org/semeval2015/task10/index.php?id=data-and-tools


DATASET USE

The TEST datasets from previous years cannot be used for training or tuning but for development-time testing only. This includes the following TEST datasets: (i) Twitter-2013, (ii) SMS-2013 messages, (iii) Twitter-2014, (iv) Twitter-2014-sarcasm, (v) Live Journal-2014, and (vi) Twitter-2015


TEAMS

We discourage multiple teams with overlapping team members.


SUBMISSION NOTES

1. Participants can choose to download the test data at any moment during the evaluation period (January 15-31, 2016). Regardless of the time of download, results are to be submitted by January 31, 2016, 23:59 hours. The time zone is Midway, Midway Islands, United States: see http://www.timeanddate.com/worldclock/city.html?n=1890).

2. The submission will be done using the SemEval START website:

  https://www.softconf.com/naacl2016/SemEval2016/

3. Participants can make new submissions, which will substitute their earlier submissions on the START server multiple times, but only before the deadline (see above). Thus, we advise that participants submit their runs early, and possibly resubmit later if there is time for that (START was not closed).

4. Participants are free to participate for a single subtask or for any combination of subtasks.

5. We allow a single run per subtask.

6.  Participants are free to use any data: we will not distinguish between closed (that only use the provided data) and open (that also use additional data) runs. However, they will need to describe the resources and tools they have used to train their systems in the Web form they have recieved by email.



SUBMISSION PROCEDURE

1. Each participating team should register on 

  http://goo.gl/forms/cGkRocFFph

Only one registration is necessary per team even when participating in multiple tasks.

2. Each team's submission can include runs for one or more of the five subtasks: A, B, C, D, and/or E.

3. For *each subtask* (A, B, C, D, or E), a team may submit a *single* run, as this year, we make no distinction between closed (constrained) and open (unconstrained) runs. We also do not allow contrastive runs (due to the high number of participants).

4. Format of the submission: a single ZIP file should contain two files *per subtask*

- GROUP-SUBTASK.output
- GROUP-SUBTASK.description

Where GROUP is the group name, and SUBTASK is "A", "B", "C", "D", or E.
For example: "QCRI-A.output" + "QCRI-A.description".

The first file should follow the output format specified above for the respective subtask.

The second file should have the format of the SUBMISSION_DESCRIPTION_TEMPLATE.txt.
It should contain the following information:

	1. Team ID

	2. Team affiliation

	3. Contact information

	4. Submission, i.e., ZIP file name

	5. System specs

	- 5.1 Core approach

	- 5.2 Supervised or unsupervised

	- 5.3 Important/interesting/novel features used

	- 5.4 Important/interesting/novel tools used

	- 5.5 Significant data pre/post-processing

	- 5.6 Other data used (outside of the provided)

	- 5.7 Size of the training Twitter data used (some teams could only download part of the data)

	- 5.8 Did you participate in SemEval-2013 task 2?

	- 5.9 Did you participate in SemEval-2014 task 9?

	- 5.10 Did you participate in SemEval-2015 task 10?

	6 References (if applicable)


LICENSE

The accompanying dataset is released under a Creative Commons Attribution 3.0 Unported License
(http://creativecommons.org/licenses/by/3.0/).


CITATION

You can cite the following paper when referring to the dataset:

@InProceedings{SemEval:2016:task4,
  author    = {Preslav Nakov and Alan Ritter and Sara Rosenthal and Veselin Stoyanov and Fabrizio Sebastiani},
  title     = {{SemEval}-2016 Task 4: Sentiment Analysis in {T}witter},
  booktitle = {Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval 2016)},
  year      = {2016},
  publisher = {Association for Computational Linguistics}
}


USEFUL LINKS:

Google group: semevaltweet@googlegroups.com
SemEval-2016 Task 4 website: http://alt.qcri.org/semeval2016/task4/
SemEval-2016 website: http://alt.qcri.org/semeval2016/
