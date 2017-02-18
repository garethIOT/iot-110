[LAB6 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/setup.md)

## Part D - Finally!  The Web appeared
**Synopsis:** Finally we will tie all of this together and have all of our sensor
values both plotable and graphed on our Morris JS Chart.

## Objectives
* Test that we can receive data from the Driver and Main
* Add code to display Environmental Data in a Table in real-time
* Add code to display Inertial Data in a Table in real-time
* Add code to display Environmental Data in a in a Chart Form
* Add code to display Inertial Data in a Chart Form

### Step D1: Let's test the incoming data
```Javascript
$(document).ready(function() {

  // the key event receiver function
  iotSource.onmessage = function(e) {
    // must convert all single quoted data with double quote format
    var double_quote_formatted_data = e.data.replace(/'/g, '"');
    // now we can parse into JSON
    parsed_json_data = JSON.parse(double_quote_formatted_data);
    console.log(parsed_json_data);
  }
    ...more to come
```    

### Step D2:

![Inertial  Table Data](https://gitlab.com/iot110/iot110-student/raw/master/Resources/Images/InertialTable.png)

![Inertial Chart Data](https://gitlab.com/iot110/iot110-student/raw/master/Resources/Images/InertialChart.png)

[PART C](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartC.md) SenseHat Driver and Main WebApp Python Code

[LAB6 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/setup.md)
