function largeNumber() {
    const readline = require('readline');
    const { stdin, stdout } = process;

    const input: number[][] = [];
    const rl = readline.createInterface({
        input: stdin,
        output: stdout,
    });
    rl.on('line', (line: string) => {
        const numbers: number[] = line.split(' ').map((num) => Number(num));
        input.push(numbers);
    }).on('close', solution);

    function solution() {
        const [N, M, K]: number[] = input[0];
        const [first, second]: number[] = getFirstSecondMax();

        let secondCount = Math.floor(M / (K + 1));
        let result = (M - secondCount) * first + secondCount * second;

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
