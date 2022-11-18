const solution = (my_string) => my_string.split("").map(str => {
    const isLowerCase = str.toLowerCase() === str;
    return isLowerCase ? str.toUpperCase() : str.toLowerCase()
}).join("");
