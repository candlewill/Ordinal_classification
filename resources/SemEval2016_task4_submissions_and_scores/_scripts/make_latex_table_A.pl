#!/usr/bin/perl
#
#  Author: Preslav Nakov
#  
#  Description: Generates a LaTeX table for the SemEval-2016 Task 4 results, subtask A.
#
#  Last modified: February 25, 2016
#
#

use warnings;
use strict;
use utf8;


#################
####   MAIN   ###
#################

print '\begin{table*}[tbh]', "\n";
print '\centering', "\n";
print '\begin{small}', "\n";
print '\renewcommand{\arraystretch}{1.0}% Tighter', "\n";
print '\begin{tabular}{|c|l|l|l|l|}', "\n";
print '\hline', "\n";
print ' & & \multicolumn{3}{c|}{\bf Tweet 2016} \\\\', "\n";
print '   \bf \# & \bf System & \multicolumn{1}{c}{\bf AvgF1} & \multicolumn{1}{c}{\bf AvgR} & \multicolumn{1}{c|}{\bf Acc} \\\\', "\n";
print '\hline', "\n";

my $lineNo = 0;
my $prevArr1 = 'NA';
while (<>) {
	next if (/_baseline/);
	s/[\n\r]+$//;
	s/_/\\_/g;
	s/\$\\_/\$_/g;
	my @arr = split /\t+/;
	$arr[1] =  '\bf ' . $arr[1];
	$lineNo++;
	print "\\bf $lineNo " if ($prevArr1 ne $arr[1]);
	$prevArr1 = $arr[1];
	my $joined = join(" & ", @arr);
#;)	$joined =~ s/0\./\./g;
	print '& ', $joined, " \\\\\n";
}

print '\hline', "\n";
print '\end{tabular}', "\n";
print '\caption{Results for SemEval-2016 Task 4, subtask A.}', "\n";
print '\label{table:results}', "\n";
print '\end{small}', "\n";
print '\end{table*}', "\n";
