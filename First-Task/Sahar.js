//Sort numbers in an array in ascending order:

const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a-b});

//Sort numbers in an array in descending order:

const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return b-a});

////////////// - OR the lowest value in an array -///////////////

const points = [40, 100, 1, 5, 25, 10];

// Sort the numbers in ascending order
points.sort(function(a, b){return a-b});

// points[0] = 1 (the lowest value)
