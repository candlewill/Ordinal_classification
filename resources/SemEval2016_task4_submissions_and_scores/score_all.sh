###
### Description: Scoring script for all results for SemEval-2016 Task 4
### Author: Preslav Nakov
### Last modified: February 25, 2016
###

echo ...Scoring subtask A...
find . -name "*-A.output" \
	 -exec perl _scripts/SemEval2016_task4_test_scorer_subtaskA.pl {} \; \
     | perl -p -e 's/^.+\/([^\/]+)\/[^\/]+\.output/$1/g' \
     | sort -r -n -k15 > _results/results-A.txt

cat _results/results-A.txt



echo ...Scoring subtask B...
find . -name "*-B.output" \
	 -exec perl _scripts/SemEval2016_task4_test_scorer_subtaskB.pl _scripts/SemEval2016_task4_subtaskB_test_gold.txt {} \; \
     | perl -p -e 's/^.+\/([^\/]+)\/[^\/]+\.output/$1/g' \
     | sort -r -n -k2 > _results/results-B.txt

cat _results/results-B.txt



echo ...Scoring subtask C...
find . -name "*-C.output" \
	 -exec perl _scripts/SemEval2016_task4_test_scorer_subtaskC.pl _scripts/SemEval2016_task4_subtaskC_test_gold.txt {} \; \
     | perl -p -e 's/^.+\/([^\/]+)\/[^\/]+\.output/$1/g' \
     | sort -n -k2 > _results/results-C.txt

cat _results/results-C.txt



echo ...Scoring subtask D...
find . -name "*-D.output" \
	 -exec perl _scripts/SemEval2016_task4_test_scorer_subtaskD.pl _scripts/SemEval2016_task4_subtaskD_test_gold.txt {} \; \
     | perl -p -e 's/^.+\/([^\/]+)\/[^\/]+\.output/$1/g' \
     | sort -n -k2 > _results/results-D.txt

cat _results/results-D.txt



echo ...Scoring subtask E...
find . -name "*-E.output" \
	 -exec perl _scripts/SemEval2016_task4_test_scorer_subtaskE.pl _scripts/SemEval2016_task4_subtaskE_test_gold.txt {} \; \
     | perl -p -e 's/^.+\/([^\/]+)\/[^\/]+\.output/$1/g' \
     | sort -n -k2 > _results/results-E.txt

cat _results/results-E.txt



cat _results/results-A.txt \
	| grep -v _baseline \
    | awk -v OFS='\t' '{ print $1, $11, $7, $15, $19, $3, $23, $27; }' \
	| sort -k2 -n -r | perl _scripts/number_column_k.pl -k 1 \
	| sort -k3 -n -r | perl _scripts/number_column_k.pl -k 2 \
	| sort -k4 -n -r | perl _scripts/number_column_k.pl -k 3 \
	| sort -k5 -n -r | perl _scripts/number_column_k.pl -k 4 \
	| sort -k6 -n -r | perl _scripts/number_column_k.pl -k 5 \
	| sort -k7 -n -r | perl _scripts/number_column_k.pl -k 6 \
	| sort -k8 -n -r | perl _scripts/number_column_k.pl -k 7 \
	| perl _scripts/make_latex_table_A_historical.pl \
       > _results/results_subtask_A_historical.tex

cat _results/results-A.txt \
	| grep -v _baseline \
    | awk -v OFS='\t' '{ print $1, $27, $28, $29; }' \
	| sort -k4 -n -r | perl _scripts/number_column_k.pl -k 3 \
	| sort -k3 -n -r | perl _scripts/number_column_k.pl -k 2 \
	| sort -k2 -n -r | perl _scripts/number_column_k.pl -k 1 \
	| perl _scripts/make_latex_table_A.pl \
       > _results/results_subtask_A.tex

cat _results/results-B.txt \
	| grep -v _baseline \
	| grep -v late \
    | awk -v OFS='\t' '{ print $1, $2, $3, $4; }' \
	| sort -k4 -n -r | perl _scripts/number_column_k.pl -k 3 \
	| sort -k3 -n -r | perl _scripts/number_column_k.pl -k 2 \
	| sort -k2 -n -r | perl _scripts/number_column_k.pl -k 1 \
	| perl _scripts/make_latex_table_B.pl \
       > _results/results_subtask_B.tex

cat _results/results-C.txt \
	| grep -v _baseline \
	| sort -k3 -n | perl _scripts/number_column_k.pl -k 2 \
	| sort -k2 -n | perl _scripts/number_column_k.pl -k 1 \
	| perl _scripts/make_latex_table_C.pl \
       > _results/results_subtask_C.tex

cat _results/results-D.txt \
	| grep -v _baseline \
	| sort -k4 -n | perl _scripts/number_column_k.pl -k 3 \
	| sort -k3 -n | perl _scripts/number_column_k.pl -k 2 \
	| sort -k2 -n | perl _scripts/number_column_k.pl -k 1 \
	| perl _scripts/make_latex_table_D.pl \
       > _results/results_subtask_D.tex

cat _results/results-E.txt \
	| grep -v _baseline \
	| perl _scripts/make_latex_table_E.pl \
       > _results/results_subtask_E.tex

find . -type d -exec perl _scripts/generate_bibtex.pl {} \; > _results/systems.bib

