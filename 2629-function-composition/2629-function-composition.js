var compose = function(functions) {
    return function(x) {
        return functions.reduceRight(function(result, fn) {
            return fn(result);
        }, x);
    };
};