#!/usr/bin/env ruby
# output of this script: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(.*)\] \[to:(.*)\] \[flags:(.*?)\]/).join(",")
