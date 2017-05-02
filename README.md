# Search President
### About
This python project took wikipedia page of all the US presidents. The purpose of this is to explore basic information retrieval techniques.

### Feature
Implement the BM25 scoring function.
Implement skip-bigrams on words.

### I/O
Input: a query, eg: issued emancipation proclamation
Output: the list of related president, eg: Lincoln

### The expect input and outputs are:
1. lincoln -> Lincoln
2. taft -> Taft
3. nobel prize -> Teddy Roosevelt, Wilson, Carter, Obama
4. patent -> Lincoln
5. oxford sholar -> Clinton
6. war time president -> Jefferson, Madison, Monroe, Jackson, Polk, Pierce, Lincoln, Grant, Cleveland, Harrison, McKinley, Wilson, Franklin Roosevelt, Truman, Eisenhower, Lyndon Johnson, Nixon, George H. W. Bush, Clinton, George W. Bush, and Obama
7. johnson -> Andrew Johnson, Lyndon B. Johnson
8. bush -> George H. W. Bush, George W. Bush
9. adams -> John Adams, John Quincy Adams
10. harrison -> William Henry Harrison
11. vice president -> John Adams, Thomas Jefferson, Martin van Buren, John Tyler, Millard Fillmore, Andrew Johnson, Chester Arthur, Theodore Roosevelt, Calvin Coolidge, Harry Truman, Richard Nixon, Lyndon Johnson, Gerald Ford, Georg H W Bush
12. died in office -> William Henry Harrison, Zachary Taylor, Warren Harding, Franklin Roosevelt
13. assassinated -> Abraham Lincoln, James Garfield, William McKinley, John Kennedy
14. abraham lincoln born -> February 12, 1809
15. issued emancipation proclamation -> Lincoln
16. author declaration independence -> Jefferson
17. founding father -> John Adams, Thomas Jefferson, James Madison, George Washington
