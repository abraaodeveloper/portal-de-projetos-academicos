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

            const orderList = []
            for (const i in nResultLabels) {
                let dat = nResultLabels[i].split("-");
                orderList.push([parseInt(dat[0] + dat[1] + dat[2]), parseInt(i)]);
            }

            let bubbleSort = (inputArr) => {
                let len = inputArr.length;
                let swapped;
                do {
                    swapped = false;
                    for (let i = 0; i < len-1; i++) {
                        if (inputArr[i][0] > inputArr[i + 1][0]) {
                            let tmp = inputArr[i];
                            inputArr[i] = inputArr[i + 1];
                            inputArr[i + 1] = tmp;
                            swapped = true;
                        }
                    }
                } while (swapped);
                return inputArr;
            };

            let ordenado = bubbleSort(orderList);

            const nLabl = [];
            const nResl = [];
            for(i of ordenado){
                nLabl.push(nResultLabels[i[1]]);
                nResl.push(nResultValues[i[1]]);
            }

            // chart.js
            const labels = nResultLabels;

            const data = {
                labels: nLabl,
                datasets: [{
                    label: 'Quantidade de novos projetos por dia',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: nResl,
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