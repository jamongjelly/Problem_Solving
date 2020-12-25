function untilOne2() {
    const readline = require('readline');
    const { stdin, stdout } = process;

    let input: number[] = [];
    const rl = readline.createInterface({
        input: stdin,
        output: stdout,
    });
    rl.on('line', (line: string) => {
        const numbers = line.split(' ').map((num: string) => Number(num));
        input = [...input, ...numbers];
    }).on('close', solution);

    function solution() {
        let N = input[0];
        const K = input[1];
        let count = 0;

        while (N > 1) {
            const quotient = Math.floor(N / K);
            const kMultiple = quotient * K;
            if (N === kMultiple) {
                N = quotient;
                count++;
            } else {
                const diff = N - kMultiple;
                N -= diff;
                count += diff;
            }
        }
        console.log(count);
    }
}

untilOne2();
