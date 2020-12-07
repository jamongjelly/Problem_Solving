function maxCard() {
    const readline = require('readline');
    const { stdin, stdout } = process;

    let input: number[][] = [];
    const rl = readline.createInterface({
        input: stdin,
        output: stdout,
    });
    rl.on('line', (line: string) => {
        const numbers: number[] = line.split(' ').map((num) => Number(num));
        input.push(numbers);
    }).on('close', solution);

    function solution() {
        const [N, M] = input[0];

        const minArr = input
            .slice(1, N + 1)
            .reduce(
                (acc, cur) =>
                    acc.concat(cur.reduce((min, num) => (min < num ? min : num))),
                []
            );
        const maxVal = minArr.reduce((max, num) => (max > num ? max : num));

        console.log(maxVal);
    }
}

maxCard();
