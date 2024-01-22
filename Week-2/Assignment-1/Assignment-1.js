
function max(numbers) {
    let max_num = 0;
    if ( numbers.length === 0 ) {
        return "None"
    } else {
        for ( let index = 0; index < numbers.length ; index++ ) {
            if ( numbers[index] > max_num ) {
                max_num = numbers[index];
            }
        }
    return max_num
    }
}

console.log( max([1, 2, 4, 5]) ); // should print 5
console.log( max([5, 2, 7, 1, 6]) ); // should print 7
console.log( max([]) ); // should print None

// -------------------------------------------------------------

function findPosition(numbers, target) {
    let result = -1;
    let index = 0;
    for ( index === 0; index < numbers.length ; index++ ) {
        if ( numbers[index] === target ) {
            result = index;
            break
        } else {
            index += 1
        }
    }
    return result
}

console.log( findPosition([5, 2, 7, 1, 6], 5) ); // should print 0
console.log( findPosition([5, 2, 7, 1, 6], 7) ); // should print 2
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) ); // should print 2 (the first one)
console.log( findPosition([5, 2, 7, 1, 6], 8) ); // should print -1

