async function yval(link) {
    try {
      const response = await fetch(link);
      const data = await response.json();
  
      const yValues = [];
      
  
      Object.values(data).forEach(innerObj => {
        Object.values(innerObj).forEach(value => {
          yValues.push(Number(value.alt));
          
        });
      });
      
      return yValues;
      
    } catch (error) {
      console.error('Error:', error);
      throw error;
    }
  }
  
  
  function getRandomColor() {
    // Generate a random color using any desired method
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }