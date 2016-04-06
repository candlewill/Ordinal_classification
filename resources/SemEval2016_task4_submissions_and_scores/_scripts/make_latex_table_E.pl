#!/usr/bin/perl
#
#  Author: Preslav Nakov
#  
#  Description: Generates a LaTeX table for the SemEval-2016 Task 4 results, subtasks B, C, D, and E.
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

print '\begin{table}[tbh]', "\n";
print '\centering', "\n";
print '\begin{small}', "\n";
print '\renewcommand{\arraystretch}{1.0}% Tighter', "\n";
print '\begin{tabular}{|c|l|l|}', "\n";
print '\hline', "\n";
print '   \bf \# & \bf System & \bf Score \\\\', "\n";
print '\hline', "\n";

my $lineNo = 0;
my $prevScore = -100000;
while (<>) {
	next if (/_baseline/);
	s/[\n\r]+$//;
	s/_/\\_/g;
	s/\$\\_/\$_/g;
	my @arr = split /\t+/;
	$lineNo++;
	print "$lineNo " if ($prevScore != $arr[$#arr]);
	$prevScore = $arr[$#arr];
	my $joined = join(" & ", @arr);
#;)	$joined =~ s/0\./\./g;
	print '& ', $joined, " \\\\\n";
}

print '\hline', "\n";
print '\end{tabular}', "\n";
print '\caption{Table caption.}', "\n";
print '\label{table:results}', "\n";
print '\end{small}', "\n";
print '\end{table}', "\n";
