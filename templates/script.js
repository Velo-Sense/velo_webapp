async function fetchData() {
  try {
    const check=document.getElementById('variable')
    //var headingValue = check.textContent;
    var headingValue = check.innerText;
    console.log(headingValue)
    const response = await fetch(headingValue);
    
    const jsonData = await response.json();
    console.log(jsonData);

    const dynamicContentElement = document.getElementById('dynamicContent');
    
    for (const [key, value] of Object.entries(jsonData)) {
      const row = document.createElement('tr');
      const keyCell = document.createElement('td');
      const valueCell = document.createElement('td');
      keyCell.textContent = key;
      valueCell.textContent = value;
      row.appendChild(keyCell);
      row.appendChild(valueCell);
      dynamicContentElement.appendChild(row);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();