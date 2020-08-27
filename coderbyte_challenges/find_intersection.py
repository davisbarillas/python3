function FindIntersection(strArr) { 
    let a = strArr[0].split(', ');
    let b = strArr[1].split(', ');
    let result = [];
    b.forEach(function(e) {
        if(a.includes(e)){
            result.push(e);
        }
    });
    return result.length ? result.join(',') : false;
}
// keep this function call here 
console.log(FindIntersection(readline()));
