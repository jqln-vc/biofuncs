# Biofuncs: Biology Functions 

Miscellanea of functions related to biological analysis, mostly genomics oriented.

*  <b>pattern_count (text, pattern)</b> : <i>returns the number of occurrences of a given pattern within the text.</i>  
       <b>input</b>&emsp;|  text (str) : the text in which to search for the pattern.  
   &emsp;&emsp;&emsp;&ensp;|  pattern (str) : the pattern to search for.  
       <b>output</b>&nbsp;|  occurrences (int) : the number of occurrences of the pattern in the text.
<br>

*   <b>frequency_map (text, k)</b> : <i>returns a frequency map of all k-mers in the given text.</i>  
       <b>input</b>&emsp;|  text (str) : the text in which to search for the k-mers.  
   &emsp;&emsp;&emsp;&ensp;|  k (int) : the length of k-mers to search for.  
       <b>output</b>&nbsp;|  frequency (dict) : a dictionary with k-mers as keys and their occurrence counts as values.
   
## References 

<b>Biopython Documentation 1.84.</b> Updated on 2024. Available at [biopython.org/docs](https://biopython.org/docs/1.84/).  
COMPEAU, Phillip; PEVZNER, Pavel. <b>Bioinformatics Algorithms: An Active Learning Approach Vol.1</b>, 2ed. La Jolla: Active Learning Publishers, 2015.
