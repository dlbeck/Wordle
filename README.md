# Wordle
Use this script to generate gueses for Wordle.

Run like:
```
python3 wordle.py "outline" "includeLetters" "discludeLetters"
```

* outline: outline of word that includes the known (green) letters and underscores for the unknown letters
  * Ex) If my first and third letters were green 'a' and 'b' respectively: "a_b__"
  * Do not include letters that are known to be in the word with unknown positions (yellow) in the outline
  * If no letters are known, outline should be all underscores: "_____"
* includeLetters: These are the letters that are known to be in the word with unknown positions (yellow). These should be passed in as a single string in any order
  * Ex) If 'm' and 'e' are known with unknown positions: "me" or "em"
  * If there are no known with unknown positions, pass in the empty string: ""
* discludeLetters: These are the letters that are known not to be in the word. These should be passed in as a single string in any order
  * Ex) If 's','t', and 'n' are known not to be in the word: "stn" or "tsn", etc.
  * If there are no letters known not to be in the word, pass in the empty string: ""
