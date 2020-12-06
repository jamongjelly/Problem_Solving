function largeNumber() {
    const readline = require('readline');
    const { stdin, stdout } = process;

    let input = [];
    const rl = readline.createInterface({
        input: stdin,
        output: stdout,
    });
    rl.on('line', (line) => {
        const numbers = line.split(' ').map((num) => Number(num));
        input.push(numbers);
    }).on('close', solution);

    function solution() {
        const [N, M, K]: number[] = input[0];
        const [first, second]: number[] = getFirstSecondMax();

        let multiple = Math.floor(M / (K + 1)) * K + (M % (K + 1));
        let result = multiple * first + (M - multiple) * second;

        console.log(result);
    }

    function getFirstSecondMax() {
        let first: number = 0;
        let second: number = 0;

        input[1].forEach((num: number) => {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second) {
                second = num;
            }
        });

        return [first, second];
    }
}

largeNumber();
