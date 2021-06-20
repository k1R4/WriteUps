phrase = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f';
flag = [];

i = 0;
while (i<8){
    flag[i] = phrase.charAt(i);
    i = i + 1;
}

while (i<16){
    flag[i] = phrase.charAt(23-i)
    i = i + 1;
}

while (i<32){
    flag[i] = phrase.charAt(46-i);
    i = i + 2;
}

i = 31;
while (i>=17){
    flag[i] = phrase.charAt(i);
    i = i - 2;
}

console.log(flag.join(""));
