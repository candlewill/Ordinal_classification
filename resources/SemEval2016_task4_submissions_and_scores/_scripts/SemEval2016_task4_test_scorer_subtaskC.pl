#!/usr/bin/perl
#
#  Author: Veselin Stoyanov and Preslav Nakov
#  
#  Description: Scores SemEval-2016 task 4, subtask C
#               Calculates macro-averaged mean absolute error,
#               and also simple mean average error
#
#  Last modified: Feb. 25, 2016
#
#

use warnings;
use strict;
use utf8;
binmode (STDIN,  ":utf8");
binmode (STDOUT, ":utf8");

my $GOLD_FILE          =  $ARGV[0];
my $INPUT_FILE         =  $ARGV[1];
my $OUTPUT_FILE        =  $INPUT_FILE . '.scored';


########################
###   MAIN PROGRAM   ###
########################

my %dist = ();
my %count = ();

### 1. Read the files and get the statsitics
open INPUT, '<:encoding(UTF-8)', $INPUT_FILE or die;
open GOLD,  '<:encoding(UTF-8)', $GOLD_FILE or die;

foreach my $label ('-2', '-1', '0', '1', '2') {
    $dist{$label} = 0.0;
    $count{$label} = 0;
}

for (; <GOLD>; ) {
	s/^[ \t]+//;
	s/[ \t\n\r]+$//;

	### 1.1. Check the input file format
	#1234	michael jackson 1
	die "Wrong file format!" if (!/^(\d+)\t[^\t]+\t(\-?[012])/);
	my ($pid, $trueLabel) = ($1, $2);

	### 1.2	. Check the prediction file format
	#14114531	michael jackson 0
	$_ = <INPUT>;
	die "Wrong file format!" if (!/^(\d+)\t[^\t]+\t(\-?[012])/);
	my ($tid, $proposedLabel) = ($1, $2);

        die "Ids mismatch!" if ($pid ne $tid);

	### 1.3. Update the statistics
	$dist{$trueLabel} += abs($trueLabel - $proposedLabel);
	$count{$trueLabel}++;
}

close(INPUT) or die;
close(GOLD) or die;

#print "Format OK\n";

### 2. Calculate macro-averaged mean absolute error
print "$INPUT_FILE\t";
open OUTPUT, '>:encoding(UTF-8)', $OUTPUT_FILE or die;

my ($absErr, $examplesCnt) = (0, 0);
my $MAE_M = 0.0;
foreach my $class ('-2', '-1', '0', '1', '2') {
    my $classDistance = 1.0 * $dist{$class} / $count{$class};
    $MAE_M += $classDistance;

    $absErr += $dist{$class};
    $examplesCnt += $count{$class};

    printf OUTPUT "\t%8s: %0.3f\n", $class, $classDistance;
}
$MAE_M /= 5.0;
my $MAE_mu = 1.0 * $absErr / $examplesCnt;
printf OUTPUT "\tOVERALL SCORE : MAE_M=%0.3f, MAE_mu=%0.3f\n", $MAE_M, $MAE_mu;
printf "%0.3f\t%0.3f\t", $MAE_M, $MAE_mu;

print "\n";
close(OUTPUT) or die;
