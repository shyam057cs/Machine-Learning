This program produces segmentation of Domain Names and Social Media HashTags, into English Language words. For example,

www.nicedomains.com => [nice domains]

www.50apples50domains.in => [50 apples 50 domains]

#beinghuman => [being human]

#30secondstomars => [30 seconds to mars]

The segmentation is based on the list of 5000 most common words found in 'words.txt'. Also it pick up numbers (both integer and decimal) 
like 100, 200.10 etc.

For cases where it might be possible to split an input string into tokens in multiple possible ways. 
For example,

    thisisinsane => [this is insane] and [this is in sane]
    
In such cases it select the longest possible string from the left side, such that the remaining string can be split into valid tokens. 
So,
    thisisinsane => [this is insane]
    
    
Sample Input

4
www.fast20company.ru
www.banananation.org
#takeyour30books
#20.5secondstolife 

Sample Output

fast 20 company
banana nation
take your 30 books
20.5 seconds to life


Note: If it is not able to produce a valid segmentation, then it just output the original string itself, after scrubbing
out the # for hashtags, the ‘www’ and extensions for domain names.
