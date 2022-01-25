function weekdayText(weekdays) {
    //Implement your code here
    return function (num) {
        if (Number(num) === -1 || Number(num) > 6) {
            throw new Error("Invalid weekday number")
        }
        if (Number(num) > weekdays.lengt) {
            throw new Error("Invalid weekday number")
        }
        return weekdays[Number(num)]
    }
}