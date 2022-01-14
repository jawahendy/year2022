function gradingStudents(grades) {
    var multipleToRoundTo = 5;
    var numberToRoundAt = 2;
    for (var i = 0; i < grades.length; i++) {
        if (grades[i] >= 38 && grades[i] % multipleToRoundTo > numberToRoundAt) {
            grades[i] = grades[i] + (multipleToRoundTo - (grades[i] % multipleToRoundTo));
        }
    }
    return grades;
}