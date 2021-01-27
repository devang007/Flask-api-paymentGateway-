# Flask-api-paymentGateway-
#Payment Details Validation rules
1) Credit card number

-validation includes

-Visa (length 16, prefix 4)
-Mastercard (length 16, prefix 51-55)
-Discover (length 16, prefix 6011)
-American Express (length 15, prefix 34 or 37)
-All 16 digit formats accept optional hyphens (-) between each group of four digits.

-Limitation 

4444-4444-4444-4444 where it starts with 4 which determines it as a visa card but there is no other number in it

2) Card holder name

-Takes name and lastname space separated.
-It should have atleast two letter in name and surname
-It can include { . , ' }

-Limitation
Person can enter Example : aaaa aaaa or abc abc 

3) Expiration date 

-format MM/YY
-It will not accept month greater thab 12
-It will not accept month and year as 00
-It will check weather the date entered is from past , if yes than it will get rejected.

4) Security code
- it can be any 3 digit code

5) Amount
- It can be any positive decimal value greater than 0.
