var getJSON = function (url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function () {
        var status = xhr.status;
        if (status === 200) {
            callback(null, xhr.response);
        } else {
            callback(status, xhr.response);
        }
    };
    xhr.send();
};

let rLabels = []
let rValues = []

getJSON("/getstatistic",
    function (err, d) {
        if (err !== null) {

        } else {
            let rLabels = d.labels;
            let rValues = d.values;

            let nResultLabels = [rLabels[0]]
            let nResultValues = [0]

            for(i in rLabels){
                let isEqual = false;
                let indexEqual = 0;
                for(r in nResultLabels){
                    if(nResultLabels[r] === rLabels[i]){
                        isEqual = true;
                        indexEqual = r;
                    }
                }
                if (isEqual){
                    nResultValues[indexEqual] += 1;  
                }else{
                    nResultLabels.push(rLabels[i]); 
                    nResultValues.push(1); 
                }
            }
            
            nResultLabels.reverse()
            nResultValues.reverse()
            
  
            // chart.js
            const labels = nResultLabels;

            const data = {
                labels: labels,
                datasets: [{
                    label: 'Quantidade de novos posts por dia',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: nResultValues,
                }]
            };

            const config = {
                type: 'line',
                data,
                options: {}
            };

            const myChart = new Chart(
                document.getElementById('myChart'),
                config
            );
        }
    });

