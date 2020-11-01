const fs = require('fs');

fs.readFile('Downloads/whitepages.txt', 'hex', async (err, data) => {
    flag = String(data);
    flag = flag.replace(/e28083/g, "0");
    flag = flag.replace(/20/g, "1");
    console.log(flag);
});
