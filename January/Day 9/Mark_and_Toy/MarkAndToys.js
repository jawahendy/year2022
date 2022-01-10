function maximumToys(prices, k) {
    // Write your code here
        // sorting the array by price low to high
    let sortedPrices = prices.sort((a,b) => a - b);

    // to save the number of toys
    let counter = 0;

    // To go to every element of the prices array
    sortedPrices.forEach(price => {

        // comparing if my $ is greather than every element of the array (price)
        if (k > price) { // if true
            // then decrement my money $
            k = k - price;
            // counter increments means another toy
            counter++;
        }
    });

    // returning the number of toys that I can buy
    return counter;
}
