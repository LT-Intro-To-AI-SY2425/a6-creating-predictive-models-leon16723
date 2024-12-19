# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
It is 0.84, meaning it is bassicaly 84% accurate or at least thats how much the gap is.
2. Is your model accurate? Why or why not?
It is most definently te most acurate model we have had yet. But it is still not the most accurate it porably can be.
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
For a car that is twenty years old with 150000 miles the predicted price is around $3,300, while the car that is ten years old and has 89000 is predicted to be around $10,500.
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening? yes when i went into my code and put specifically a car that is 25 years old and has 300000 miles it predicted that it would be $-153,800. i asumme because the algroathim i wrote belives that a car so old with such hig milage would not be worth anything, this can obviously be wrong as some cars can be collectors ect. but the algorthim does not understnad this and sees it as something that is very cheap, and eventually not worth anything making it negative. this can proably be fixed.