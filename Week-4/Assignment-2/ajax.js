function ajax(src, callback){
  fetch(src)
  .then(function(response) {
      return response.json();
  })
  .then(function (json) {
      callback (json)
  });
}

function render(json){ 
  // Get the container element where the table will be inserted
  let container = document.getElementById("container");
  
  // Create the table and header element
  let table = document.createElement("table");
  let thead = document.createElement("thead");
  let tr = document.createElement("tr");

  // Get the keys (column names) of the first object in the JSON data
  let cols = Object.keys(json[0]);
  
  // Loop through the column names and create header cells
  cols.forEach((item) => {
      let th = document.createElement("th");
      th.innerText = item; // Set the column name as the text of the header cell
      tr.appendChild(th); // Append the header cell to the header row
  });
  
  thead.appendChild(tr); // Append the header row to the header
  table.append(tr) // Append the header to the table
  
  // Loop through the JSON data and create table rows
  json.forEach((item) => {
      let tr = document.createElement("tr");
      
      // Get the values of the current object in the JSON data
      let vals = Object.values(item);

      // Loop through the values and create table cells
      vals.forEach((elem) => {
          let td = document.createElement("td");
          td.innerText = elem; // Set the value as the text of the table cell
          tr.appendChild(td); // Append the table cell to the table row
      });
      
      table.appendChild(tr); // Append the table row to the table
  });
  
  container.appendChild(table) // Append the table to the container element
}

ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products", function(response){
  render(response);
});

//ref: https://www.tutorialspoint.com/how-to-convert-json-data-to-a-html-table-using-javascript-jquery