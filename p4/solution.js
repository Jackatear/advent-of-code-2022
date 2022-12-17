const fs = require('fs');
let count = 0;
let first, second;
let firstRange = [];
let secondRange = [];

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    };
    data.split(/\r?\n/).forEach(line => {
        line = line.split(',');
        first = line[0];
        second = line[1];
        firstRange = first.split('-');
        secondRange = second.split('-');
        for (let i = 0; i < firstRange.length; i++) {
            firstRange[i] = Number(firstRange[i]);
            secondRange[i] = Number(secondRange[i]);
        }
        if (firstRange[0] < secondRange[0]) {
            if (firstRange[1] > secondRange[1] || firstRange[1] == secondRange[1]){
                count = count + 1;
            }
        } 
        if (secondRange[0] < firstRange[0]) {
            if (firstRange[1] < secondRange[1] || firstRange[1] == secondRange[1]){
                count = count + 1;
            } 
        }
        if (firstRange[0] == secondRange[0]) {
            count = count + 1;
        }
    });
    console.log(count)
});

