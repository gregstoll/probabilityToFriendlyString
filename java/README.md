Built against JDK 11

Usage:

    FriendlyProbability friendly = FriendlyProbability.fromProbability(.723);    

`friendly` is a class of type `FriendlyProbability` with getters
- `getFriendlyString()`: a string representing the probability (in this case "5 in 7")
- `getFriendlyDescription()`: a string representing a qualitative description of the probability (in this case "Good chance")
- `getNumerator()`: the numerator of the probability (in this case 5)
- `getDenominator()`: the denominator of the probability (in this case 7)

Note that passing a value less than 0 or greater than 1 to `FriendlyProbability.fromProbability()` will throw an `IllegalArgumentException`.
