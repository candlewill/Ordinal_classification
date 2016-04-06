#!/usr/bin/perl
#
#  Author: Preslav Nakov
#  
#  Description: Generates BibTex stub.
#
#  Last modified: March 3, 2016
#
#

use warnings;
use strict;
use utf8;


################
###   MAIN   ###
################

die "Team ID expected!" if (0 != $#ARGV);

my $teamName = $ARGV[0];
$teamName =~ s/^[^\/]+\///;

if ($teamName !~ /^[\._]/) {
	$teamName =~ s/_/\\_/g;
	print "\@InProceedings{SemEval:2016:task4:$teamName,\n";
	print "  author    = {$teamName\\\_author},\n";
	print "  title     = {$teamName at {SemEval}-2016 Task 4: ...}, \n";
	print '  booktitle = {Proceedings of the 10th International Workshop on Semantic Evaluation},', "\n";
	print '  series    = {SemEval \'16},', "\n";
	print '  month     = {June},', "\n";
	print '  year      = {2016},', "\n";
	print '  address   = {San Diego, California},', "\n";
	print '  publisher = {Association for Computational Linguistics},', "\n";
	print '}', "\n\n";
}
