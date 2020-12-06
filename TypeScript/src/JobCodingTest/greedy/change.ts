function change() {
    const readline = require('readline');
    const { stdin, stdout } = process;

    let input: number = 0;
    const rl = readline.createInterface({
        input: stdin,
        output: stdout,
    });
    rl.on('line', (line) => {
        input = parseInt(line);
    }).on('close', solution);

    function solution() {
        let N: number = input;
        console.log(getMinCoins(N));
    }

    const getMinCoins = (N: number) => {
        const coins: number[] = [500, 100, 50, 10];
        return coins.reduce((count: number, coin: number) => {
            const addition: number = Math.floor(N / coin);
            N %= coin;
            return count + addition;
        }, 0);
    };
}

change();
