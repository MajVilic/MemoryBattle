var request = new XMLHttpRequest()

request.open('get', 'http://Mega:8100/rezultati', true)

request.onload = function () {
    var data = JSON.parse(this.response)
    console.log(data)
    arr = []
    if (request.status >= 200 && request.status < 400) {
        data.forEach((element) => {
        arr.push([element.id,element.diff,element.nof,element.score])
      })
	  
      addTable(arr)
    } else {
      console.log('error')
    }
	
}


// send request
request.send()


function addTable(names) {
  var myTableDiv = document.getElementById("tbl");
  // myTableDiv.height = '400';
  
  var table = document.createElement('TABLE');
  table.border = '1.5';
  // table.height = '400';
  
  var tableHead = document.createElement('THEAD');
  table.appendChild(tableHead);
  
  var tableBody = document.createElement('TBODY');
  table.appendChild(tableBody);
  

  var tr = document.createElement('TR');
  tableHead.appendChild(tr);
  var th1 = document.createElement('TH');
  th1.appendChild(document.createTextNode('Username'))
  th1.width = '218';
  tr.appendChild(th1);
  var th1 = document.createElement('TH');
  th1.appendChild(document.createTextNode('Diffculty'))
  th1.width = '215';
  tr.appendChild(th1);
  var th1 = document.createElement('TH');
  th1.appendChild(document.createTextNode('Number of players'))
  th1.width = '208';
  tr.appendChild(th1);
  var th1 = document.createElement('TH');
  th1.appendChild(document.createTextNode('Score'))
  th1.width = '220';
  tr.appendChild(th1);
 
  for (var i = 0; i < names.length; i++) {
    var tr = document.createElement('TR');
    tableBody.appendChild(tr);
	

    for (var j = 0; j < 4; j++) {
      var td = document.createElement('TD');
      td.width = '270'
	  
	  td.appendChild(document.createTextNode(names[i][j]));
      tr.appendChild(td);
    }
  }
  myTableDiv.appendChild(table);
}