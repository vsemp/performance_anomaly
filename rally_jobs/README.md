# No performance anomaly observed in these Rally jobs

I used Devstack with a single node. Performance variation when running Rally jobs sevel times was with standard deviation of no more than 10%. This performance variation behaved according to 1/sqrt("times" parameter) as expected.

I checked Cinder create-and-delete that was mentioned on Trello. I didn't see any abnormal variation there.
