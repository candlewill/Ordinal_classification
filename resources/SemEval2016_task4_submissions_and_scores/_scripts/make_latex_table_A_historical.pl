#!/usr/bin/perl
#
#  Author: Preslav Nakov
#  
#  Description: Generates a LaTeX table for the SemEval-2016 Task 4 results, subtask A, historical comparison.
#
#  Last modified: February 23, 2016
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
print '\begin{tabular}{|c|l|ll|lll|l|l|}', "\n";
print '\hline', "\n";
print '   & & \multicolumn{2}{c|}{\bf 2013} & \multicolumn{3}{c|}{\bf 2014} & \multicolumn{1}{c|}{\bf 2015} & \multicolumn{1}{c|}{\bf 2016} \\\\', "\n";
print '   \bf \# & \multicolumn{1}{c|}{\bf System} & \bf Tweet & \bf SMS & \bf Tweet & \bf Tweet & \bf Live- & \bf Tweet & \bf Tweet \\\\', "\n";
print '   & &  &  & \bf & \bf sarcasm & \bf Journal & & \bf \\\\', "\n";
print '\hline', "\n";

my $lineNo = 0;
my $prevArrLast = 'NA';
while (<>) {
	next if (/_baseline/);
	s/[\n\r]+$//;
	s/_/\\_/g;
	s/\$\\_/\$_/g;
	my @arr = split /\t+/;
	$arr[$#arr] =  '\bf ' . $arr[$#arr];
	$lineNo++;
	print "\\bf $lineNo " if ($prevArrLast ne $arr[$#arr]);
	$prevArrLast = $arr[$#arr];
	my $joined = join(" & ", @arr);
#;)	$joined =~ s/0\./\./g;
	print '& ', $joined, " \\\\\n";
}

print '\hline', "\n";
print '\end{tabular}', "\n";
print '\caption{Table caption.}', "\n";
print '\label{table:results}', "\n";
print '\end{small}', "\n";
print '\end{table*}', "\n";
