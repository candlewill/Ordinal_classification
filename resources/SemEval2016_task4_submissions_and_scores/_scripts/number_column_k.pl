#!/usr/bin/perl
#
#  Author: Preslav Nakov
#  
#  Description: Numbers column k
#
#  Last modified: February 23, 2016
#
#

use warnings;
use strict;
use utf8;

use Getopt::Std;


#################
####   MAIN   ###
#################

my %options = ();
getopts("k:mt", \%options);

die "-k <COLUMN_NUMBER> required" if (!defined($options{k}));
my $columnNo = $options{k};

my $lineNo = 0;
my $prevScore = -100000;
my $prevLineNo = -100;
while (<>) {
	s/[\n\r]+$//;
	my @arr = split /\t+/;
	if (defined($options{m})) { $arr[$columnNo] *= 100.0; }
	my $str = sprintf "%0.3f", $arr[$columnNo];
	$lineNo++;
	if ($prevScore != $arr[$columnNo]) {
		$prevLineNo = $lineNo;
		$prevScore = $arr[$columnNo];
	}
	$arr[$columnNo] = $str . '$_{' . $prevLineNo . '}$';		

	if (defined($options{t})) { $arr[$columnNo] = '\scriptsize ' . $arr[$columnNo]; }
	print join("\t", @arr), "\n";
}
