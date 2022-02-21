function parseTerms(urlToFile, _callback){
    d3.csv(urlcsv, function(data) {
        var tList = []
        for(var i = 0; i<data.length;i++){
            tList[i] = data[i]
        };
    _callback()
    return tList
})
}