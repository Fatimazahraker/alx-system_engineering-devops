#!/usr/bin/env ruby
#rgx expression that accept one arg then pass it to regular expression matching method

puts ARGV[0].scan(/hbt{2,5}n/).join
